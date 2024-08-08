from django.contrib import admin
from django.urls import path
from . import views
from .views import Enroll

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='home'),
    path('course/', views.Course, name='course'),
    path('login/', views.login, name='login'),
    path('enroll/', views.enroll, name='enroll'),
    path('enrollment_success/', views.enrollment_success, name='enrollment_success'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
