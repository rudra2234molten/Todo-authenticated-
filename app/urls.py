from django.urls import path
from . import views

urlpatterns = [
    path('',views.Auth,name='login'),
    path('login/',views.log_in,name='login_main'),
    path('logout/',views.log_out,name='logout')
]
