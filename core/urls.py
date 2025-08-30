from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.profile, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('explore/', views.explore, name='explore'),
    path('events/', views.events, name='events'),
    path('post_create/', views.post_create, name='post_create'),
    path('about/', views.about, name='about'),
]