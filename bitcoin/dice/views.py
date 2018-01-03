# coding:utf-8

from django.http import HttpResponse
from django.shortcuts import render
from dice import models
import random

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
            win.append(models.Player.objects.get(id=(i+1)))
        else:
            lose_num += 1
            lose.append(models.Player.objects.get(id=(i+1)))
    win_coin = lose_num / win_num
    for i in range(6):
        if p[i].result == False:
            p[i].transaction = -1
            p[i].balance -= 1
        else :
            p[i].transaction = win_coin
            p[i].balance -= p[i].transaction
    for i in range(len(win)):
        for m in range(len(lose)):
            send_transaction(p[i],p[m],1)

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
    else: message = "结果已经出来了，点击下方按钮查看"
    return render(request, 'loading.html', {"status":message})
 
def player(request):
    return render(request, 'player.html')
