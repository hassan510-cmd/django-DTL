from django.urls import path,include
from .views import index , home,view_task,delete_task,update_task
app_name='todo'
urlpatterns=[
    # path('',index,name='home'),
    path('home/',home,name='index'),
    path('task/<task_id>',view_task,name='task'),
    path('task-del/<task_id>',delete_task,name='task-del'),
    path('task-edit/<task_id>',update_task,name='task-edit'),
]