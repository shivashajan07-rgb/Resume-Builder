from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, gen_resume, register

urlpatterns = [
    path('', home, name='home'),
    path('resume/', gen_resume, name='resume'),
    # CRITICAL: Use 'registration/login.html' (not 'auth/login.html')
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', register, name='register'),
]