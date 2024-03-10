from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
# Create your views here.

def addTask(request):
    data=request.POST['newtask']
    Task.objects.create(mission=data)
    return redirect('home')
    
def markdone(request,pk):
    is_comp=get_object_or_404(Task,pk=pk)
    is_comp.status =True
    is_comp.save()
    return redirect('home')


def markundone(request,id):
    data3=get_object_or_404(Task,id=id)
    data3.status=False
    data3.save()
    return redirect('home')

def edit_task(request,pk):
    get_task =get_object_or_404(Task,pk=pk)
   
    if request.method == 'POST':
        new_task = request.POST['task']
        get_task.mission=new_task
        get_task.save()
        return redirect('home')
        
    else:
        context ={
            'get_task' : get_task,
        }

        return render(request,'edit-task.html',context)
    

def delete_task(request,pk):
    get_task = get_object_or_404(Task,pk=pk)
    get_task.delete()
    return redirect('home')