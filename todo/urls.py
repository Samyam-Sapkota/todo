from django.urls import path
from .models import Task
from . import views

urlpatterns=[
    path('addnew/',views.addTask,name='addTask'),
    path('markdone/<int:pk>/',views.markdone,name='markdone'),
    path('markundone/<int:id>/',views.markundone,name='markundone'),
    path('edit_task/<int:pk>/',views.edit_task,name='edit_task'),
    path('delete_task/<int:pk>/',views.delete_task,name='delete_task')
]