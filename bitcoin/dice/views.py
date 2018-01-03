# coding:utf-8

from django.http import HttpResponse
from django.shortcuts import render
from dice import models

# Create your views here.
def home(request):
    p1 = models.Player.objects.get(id=1)
    p2 = models.Player.objects.get(id=2)
    p3 = models.Player.objects.get(id=3)
    p4 = models.Player.objects.get(id=4)
    p5 = models.Player.objects.get(id=5)
    p6 = models.Player.objects.get(id=6)
    return render(request, 'home.html',{"p1":p1,"p2":p2,"p3":p3,"p4":p4,"p5":p5,"p6":p6,})