
from django.urls import path, include
from .import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', include('store.urls')),
    path('register/', views.register, name = "register"),
    path('login/', auth_view.LoginView.as_view(template_name = 'users/login.html'), name = "login"),
    path('profile/', views.profile, name='profile'),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name="logout"), 
]