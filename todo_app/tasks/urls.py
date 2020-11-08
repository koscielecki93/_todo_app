from django.urls import path
from . import views
app_name = "tasks"
urlpatterns = [
    path('', views.index, name="index"),
    path('list', views.task_list, name="tasks_list"),
    path('form', views.create_task, name="form"),
    path('update_task/<str:pk>/', views.updateTask, name="update_tasks"),
    path('delete/<str:pk>/', views.deleteTask, name="delete_task")

]