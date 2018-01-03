# coding:utf-8

from django.http import HttpResponse
from django.shortcuts import render
from dice import models
import random

# Create your views here.

# coding=utf-8

def func(request):
    # 如果Ajax使用了GET方法，把下面的POST换成GET即可
    name = request.POST['name']
    age = request.POST['age']
    
def home(request):
    p1 = models.Player.objects.get(id=1)
    p2 = models.Player.objects.get(id=2)
    p3 = models.Player.objects.get(id=3)
    p4 = models.Player.objects.get(id=4)
    p5 = models.Player.objects.get(id=5)
    p6 = models.Player.objects.get(id=6)
    return render(request, 'home.html',{"p1":p1,"p2":p2,"p3":p3,"p4":p4,"p5":p5,"p6":p6,})
 
def index(request):
    return render(request, 'index.html')
     
def add(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a+b))

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
