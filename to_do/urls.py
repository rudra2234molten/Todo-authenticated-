from django.urls import path
from . import views

urlpatterns = [
    path('create_to_do/',views.todo_home,name='todo_form'),
    path('display_to_do/',views.display_todo,name='todo_list'),
    path('delete_to_do/<int:id>/',views.delete_todo,name='delete_todo'),
    path('update_todo/<int:id>/',views.update_todo, name='update_todo'),
]
