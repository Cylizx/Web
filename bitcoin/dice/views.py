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
    i = 0
    print (type(models.Player.objects.get(id=1)))
    for i in range(6):
        p.append(models.Player.objects.get(id=i+1))
        models.Player.objects.filter(id=i+1).update(status=False)
    return render(request, 'result.html',{"p1":p[0],"p2":p[1],"p3":p[2],"p4":p[3],"p5":p[4],"p6":p[5],})

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
