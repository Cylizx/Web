# coding:utf-8

from django.http import HttpResponse
from django.shortcuts import render
from dice import models

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