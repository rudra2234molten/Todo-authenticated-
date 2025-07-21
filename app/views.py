from django.shortcuts import render,redirect
from .forms import RegisterForm,RecaptchaForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def Auth(request):
  form = RegisterForm()
  if request.method == 'POST':
    form = RegisterForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login_main')
    else:
      print(form.errors)
  return render(request,'login.html',{'form':form})

def log_in(request):
  form = RecaptchaForm()
  errormsg = ''
  if request.method == 'POST':
    form = RecaptchaForm(request.POST)
    if form.is_valid():
      username = request.POST['username']
      password = request.POST['password']
      try:
        user = User.objects.get(username = username)
      except:
        print('user name is invalid')
      user = authenticate(request, username = username, password = password)
      if user is not None:
        login(request,user)
        print('login done')
        errormsg = ''
        return redirect('todo_list')
      else:
        if not User.objects.filter(username=username).exists():
          errormsg='User Name Does Not Exists.'
        else:
          errormsg='Incorrect Password.'
  return render(request,'login_main.html',{'form':form,'errormsg':errormsg})

@login_required(login_url='login')
def dashboard(request):
  return render(request, 'index.html',{'user':request.user})

def log_out(request):
  logout(request)
  return redirect('login')