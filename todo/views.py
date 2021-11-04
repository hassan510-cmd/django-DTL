from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
tasks = [
    {'id': 1, 'content': 'lorem', 'priority': 1, 'desc': 'lorem lorem'},
    {'id': 2, 'content': 'lorem2', 'priority': 2, 'desc': 'lorem lorem'},
    {'id': 3, 'content': 'lorem3', 'priority': 5, 'desc': 'lorem lorem'},
    {'id': 4, 'content': 'lorem3', 'priority': 5, 'desc': 'lorem lorem'},
    {'id': 5, 'content': 'lorem3', 'priority': 5, 'desc': 'lorem lorem'},
    {'id': 6, 'content': 'lorem3', 'priority': 5, 'desc': 'lorem lorem'},
]
def index(request):
    return HttpResponse("hello")

def home(request):

    return render(request,template_name='index.html',context={'tasks':tasks})
def view_task(request,task_id):
    task=''
    for i in tasks:
        if i['id'] == int(task_id):
            task=i
    return render(request,template_name='task.html' ,context={'task':task})
def update_task(request,task_id):
    task=''
    for i in tasks:
        if i['id'] == int(task_id):
            i['desc']+="updated"
    return render(request, template_name='index.html', context={'tasks': tasks})
def delete_task(request,task_id):
    task=''
    for i in tasks:
        if i['id'] == int(task_id):
            tasks.remove(i)
    return render(request, template_name='index.html', context={'tasks': tasks})
