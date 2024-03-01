
from django.contrib import admin
from django.urls import path
from MYCOMPANY import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('adminhome/', views.adminhome, name='adminhome'),
]
