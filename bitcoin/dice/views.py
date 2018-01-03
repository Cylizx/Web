# coding:utf-8

from django.http import HttpResponse
from django.shortcuts import render
from dice import models
import random

# Create your views here.

def home(request):
    return render(request, 'home.html')

def result(request):
    p1 = models.Player.objects.get(id=1)
    p2 = models.Player.objects.get(id=2)
    p3 = models.Player.objects.get(id=3)
    p4 = models.Player.objects.get(id=4)
    p5 = models.Player.objects.get(id=5)
    p6 = models.Player.objects.get(id=6)
    return render(request, 'result.html',{"p1":p1,"p2":p2,"p3":p3,"p4":p4,"p5":p5,"p6":p6,})

def loading(request):
    flag = False
    message = ""
    p1 = models.Player.objects.get(id=1)
    p2 = models.Player.objects.get(id=2)
    p3 = models.Player.objects.get(id=3)
    p4 = models.Player.objects.get(id=4)
    p5 = models.Player.objects.get(id=5)
    p6 = models.Player.objects.get(id=6) 
    if p1.status == True and p2.status == True and p3.status == True and p4.status == True and p5.status == True and p6.status == True:
        flag = True
    else: flag = False
    if flag==False:
        message = "正在等待开奖，请稍后……"
    else: message = "结果已经出来了，点击下方按钮查看"
    return render(request, 'loading.html',{"status":message})
 
def player(request):
    return render(request, 'player.html')

def player_CXY(request):
    return render(request, 'player_CXY.html')

def player_LJS(request):
    return render(request, 'player_LJS.html')

def player_LQS(request):
    return render(request, 'player_LQS.html')

def player_SN(request):
    return render(request, 'player_SN.html')

def player_XC(request):
    return render(request, 'player_XC.html')

def player_ZZX(request):
    return render(request, 'player_ZZX.html')

def judge(request):

    if 'big' in request.GET:
        a = [8, 15]
        message = '你赌的是大'
    if 'small' in request.GET:
        a = [0, 7]
        message = '你赌的是小'
    c = random.randint(0,15)
    if c in a:
        result = 1

    else:
        result = 0

    return HttpResponse(message)

def judge_CXY(request):

    if 'big' in request.GET:
        a = [8, 15]
        message = 'CXY赌的是大'
    if 'small' in request.GET:
        a = [0, 7]
        message = 'CXY赌的是小'
    c = random.randint(0,15)
    if c in a:
        result = 1

    else:
        result = 0

    return HttpResponse(message)

def judge_LJS(request):

    if 'big' in request.GET:
        a = [8, 15]
        message = 'LJS赌的是大'
    if 'small' in request.GET:
        a = [0, 7]
        message = 'LJS赌的是小'
    c = random.randint(0,15)
    if c in a:
        result = 1

    else:
        result = 0

    return HttpResponse(message)

def judge_LQS(request):

    if 'big' in request.GET:
        a = [8, 15]
        message = 'LQS赌的是大'
    if 'small' in request.GET:
        a = [0, 7]
        message = 'LQS赌的是小'
    c = random.randint(0,15)
    if c in a:
        result = 1

    else:
        result = 0

    return HttpResponse(message)

def judge_SN(request):

    if 'big' in request.GET:
        a = [8, 15]
        message = 'SN赌的是大'
    if 'small' in request.GET:
        a = [0, 7]
        message = 'SN赌的是小'
    c = random.randint(0,15)
    if c in a:
        result = 1

    else:
        result = 0

    return HttpResponse(message)

def judge_XC(request):

    if 'big' in request.GET:
        a = [8, 15]
        message = 'XC赌的是大'
    if 'small' in request.GET:
        a = [0, 7]
        message = 'XC赌的是小'
    c = random.randint(0,15)
    if c in a:
        result = 1

    else:
        result = 0

    return HttpResponse(message)

def judge_ZZX(request):

    if 'big' in request.GET:
        a = [8, 15]
        message = 'ZZX赌的是大'
    if 'small' in request.GET:
        a = [0, 7]
        message = 'ZZX赌的是小'
    c = random.randint(0,15)
    if c in a:
        result = 1

    else:
        result = 0

    return HttpResponse(message)


