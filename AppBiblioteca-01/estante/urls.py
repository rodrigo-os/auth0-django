from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('callback/', views.callback, name='callback')
]