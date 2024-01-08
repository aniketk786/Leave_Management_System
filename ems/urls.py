"""
URL configuration for ems project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from signup.views import signupAction
from login.views import loginAction
from login.views import *
from leaves.views import home, logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signupAction),
    path('login/', loginAction, name='login'),
    path('employee_dashboard/', employeAction, name='employee_dashboard'),
    path('manager_dashboard/', managerAction, name='manager_dashboard'),
    path('', signupAction),
    #path('emp_login', emp_login, name='emp_login'),
    path('home',home, name='home'),
    path('logout',logout, name='logout')

]
