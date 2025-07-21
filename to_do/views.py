from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Todo
from django.shortcuts import get_object_or_404

# Create your views here.
@login_required(login_url='login')
def todo_home(request):
  if request.method == 'POST':
    task = request.POST.get('task')
    description = request.POST.get('desc')
    Todo.objects.create(tast = task , description = description, user = request.user)
    print('task added...')
    return redirect('todo_list')
  return render(request,'todo_form.html')

def display_todo(request):
  todos = Todo.objects.filter(user = request.user)
  return render(request,'todo_list.html',{'todos':todos,'user':request.user})

def delete_todo(request,id):
  todo = Todo.objects.get(id = id)
  todo.delete()
  return redirect('todo_list')

def update_todo(request,id):
  todo = get_object_or_404(Todo,id = id)
  if request.method == 'POST':
    task = request.POST['task']
    description = request.POST['desc']
    todo.tast = task
    todo.description = description
    todo.save()
    return redirect('todo_list')
  return render(request, 'update_todo.html',{'todo':todo})
