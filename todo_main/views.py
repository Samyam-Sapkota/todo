from django.shortcuts import render
from todo.models import Task


def home(request):
    cdata=Task.objects.filter(status=True)
    udata=Task.objects.filter(status=False)
    return render(request,'home-todo.html',context={'cdata':cdata,'udata':udata})