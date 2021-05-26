"""attendance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from sheets import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('date_page/<date>', views.dates_page,name='dates'),
    path('student_pageedit/<qp>', views.student_pageedit,name='studentsedit'),
    path('student_page/<qp>', views.student_page,name='student'),
    path('save_page', views.save_page,name='barcode'),
    path('registerpage', views.registerpage,name='register'),
    path('', views.login_page,name='login'),
]
