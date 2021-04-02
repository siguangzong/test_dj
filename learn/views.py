from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import *
from django.views import generic
# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from learn.serializer import UserSerializer, GroupSerializer, BookSerializer
import django_redis


class UserViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    允许组查看或编辑的API路径。
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


def index(request):
    print('index')
    return HttpResponse("Hello 这是我的第一个DJANGO 项目")


def detail(request, question_id):
    try:
        obj = Question.objects.get(pk=question_id)
    except Exception as e:
        print(e)
        raise Http404("Question does not exist")
    print(11111)
    return HttpResponse("你正在访问第" + str(question_id) + "个问题")


class IndexView(generic.ListView):
    print(11111)


class BookViewSet(viewsets.ModelViewSet):
    """
    允许组查看或编辑的API路径。
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


def test_redis(request):
    # 建立连接
    conn = django_redis.get_redis_connection("default")
    print(conn)
    # 开始设置数据
    conn.set('wml', "333", ex=10)
    return HttpResponse("redis config is ok 111222")