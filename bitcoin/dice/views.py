# coding:utf-8

from django.http import HttpResponse
from django.shortcuts import render
from dice import models

from pow.fullnode import *
import network,_thread,time
from messages import *

import random
_thread.start_new_thread(network.init,(10084,))
person_account={0:'A',1:'B',2:'D',3:'E',4:'F',5:'G'}

wallet={}
for p in ['A','B','D','E','F','G']:
	with open (p+'_addr.json','r') as f:
		wallet[p] = json.load(f)[0]

def get_next_header():
    old = ""
    with open('block/head.json','r') as f:
        old = json.load(f)[0]
    while True:
        time.sleep(1)
        with open('block/head.json','r') as f:
             curr = json.load(f)[0]
             if old != curr:
                 return curr

def get_addr_value(addr):
    m = Fullnode()
    m.load_latest_block()
    return m.get_addr_value(addr)

def send_transaction(dst_addr,value,key):
    m = Fullnode()
    m.load_key(key)
    tr = m.create_transaction(dst_addr,value)
    network.broadcast_message(TxMessage(tr))

# Create your views here.

def home(request):
    return render(request, 'home.html')

def result(request):
    p = []
    win = []
    lose = []
    win_num = 0
    lose_num = 0
    win_coin = 0
    for i in range(6):
        p.append(models.Player.objects.get(id=(i+1)))
    for i in range(6):
        if p[i].result == True:
            win_num += 1
            win.append(i)
        else:
            lose_num += 1
            lose.append(i)
    if win_num == 0 or lose_num == 0:
        return render(request, 'result.html',{"player":p})
        for i in range(6):
            models.Player.objects.filter(id=i+1).update(status=False)

    win_coin = 1.0 /win_num

    for i in range(6):
        models.Player.objects.filter(id=i+1).update(status=False)
        if p[i].result == False:
            p[i].transaction = -1
            p[i].balance = get_addr_value(wallet[person_account[i]])
        else :
            p[i].transaction = win_coin * lose_num
            p[i].balance = get_addr_value(wallet[person_account[i]])

    for i in win:
        for m in lose:
            send_transaction(wallet[person_account[i]],win_coin,person_account[m]+'.json')

    return render(request, 'result.html',{"player":p})

def loading(request):
    flag = True
    message = ""

    # TBD: judge if there is already a gambling number

    prev_url = request.META['HTTP_REFERER']
    user_id = prev_url.split('/')[3]
    if (user_id != 'loading'):
        user_id = int(user_id)
        models.Player.objects.filter(id=user_id).update(status=True)
        if 'big' in request.GET:
            models.Player.objects.filter(id=user_id).update(result=True)
        if 'small' in request.GET:
            models.Player.objects.filter(id=user_id).update(result=False)

    for i in range(6):
        p = models.Player.objects.get(id=i+1)
        if p.status == False:
            flag = False
            break

    if flag==False:
        message = "正在等待开奖，请稍后……"
    else: 
        message = "结果已经出来了，点击下方按钮查看"
        if get_next_header()[-1]<'8':
            for i in range(6):
                models.Player.objects.filter(id=i+1).update(result=not models.Player.objects.get(id=i+1).result)

    return render(request, 'loading.html', {"status":message})
 
def player(request):
    return render(request, 'player.html')
