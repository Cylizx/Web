"""bitcoin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
# from bitcoin import settings

from django.urls import path
from django.contrib import admin
from dice import views as dice_views

admin.autodiscover()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_URL = '/static/'

# 当运行 python manage.py collectstatic 的时候
# STATIC_ROOT 文件夹 是用来将所有STATICFILES_DIRS中所有文件夹中的文件，以及各app中static中的文件都复制过来
# 把这些文件放到一起是为了用apache等部署的时候更方便
STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')
 
# 其它 存放静态文件的文件夹，可以用来存放项目中公用的静态文件，里面不能包含 STATIC_ROOT
# 如果不想用 STATICFILES_DIRS 可以不用，都放在 app 里的 static 中也可以
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "common_static"),
    '/path/to/others/static/',  # 用不到的时候可以不写这一行
)
 
# 这个是默认设置，Django 默认会在 STATICFILES_DIRS中的文件夹 和 各app下的static文件夹中找文件
# 注意有先后顺序，找到了就不再继续找了
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder"
)

urlpatterns = [
    path('', dice_views.home),
    path('result/', dice_views.result, name='result'),
    path('loading/', dice_views.loading, name='loading'),
    path('player/', dice_views.player, name='player'),
    path('judge/', dice_views.judge, name='judge'),
    path('player_CXY/', dice_views.player_CXY, name='player_CXY'),
    path('judge_CXY/', dice_views.judge_CXY, name='judge_CXY'),
    path('player_LJS/', dice_views.player_LJS, name='player_LJS'),
    path('judge_LJS/', dice_views.judge_LJS, name='judge_LJS'),
    path('player_LQS/', dice_views.player_LQS, name='player_LQS'),
    path('judge_LQS/', dice_views.judge_LQS, name='judge_LQS'),
    path('player_SN/', dice_views.player_SN, name='player_SN'),
    path('judge_SN/', dice_views.judge_SN, name='judge_SN'),
    path('player_XC/', dice_views.player_XC, name='player_XC'),
    path('judge_XC/', dice_views.judge_XC, name='judge_XC'),
    path('player_ZZX/', dice_views.player_ZZX, name='player_ZZX'),
    path('judge_ZZX/', dice_views.judge_ZZX, name='judge_ZZX'),
    path('admin/', admin.site.urls),
]