from django.urls import path
from .import views

urlpatterns = [
    path('',views.index ,name='index'),
    path('login/',views.login, name = 'login'),
    path('register/',views.register, name='register'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handeLogin, name="handleLogin"),
    
]