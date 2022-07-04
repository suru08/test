"""lab_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from.import views
from .views import Admin_details

urlpatterns = [
    path('', Admin_details, name='Admin_details'),
    path('save',views.save,name="save"),
    path('login',views.login,name="login"),
    path('admin_view',views.Admin_login,name="Admin_login"),
    path('Add_Book', views.Add_Book, name="Add_Book"),
    path('delete_book', views.delete_book, name="delete_book"),
    path('Update_Book', views.Update_Book, name="Update_Book"),



]
