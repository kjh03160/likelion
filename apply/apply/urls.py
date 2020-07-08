"""apply URL Configuration

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
from sheet.views import *
from testapp.views import *

urlpatterns = [
    path('manage/', admin.site.urls),
    path('', home, name='caution'),
    path('main/', main, name='home'),
    path('signup/', signup_page, name='signup'),
    path('apply/', create, name="create"),
    path('update/', update, name="update"),
    path('logout/', logout, name="logout"),
    path('accounts/login/', login, name='login'),
    path('complete/', complete, name='complete'),
    path('view/', view, name='view'),
    path('detail/<int:pk>', lookup, name='lookup'),
    path('eval/<int:pk>', assess, name='assess'),
    path('profile/', profile, name='profile'),
    path('recruit/', recruit, name='recruit'),
    path('users/', user_list, name='users'),
    path('result/', result, name='result'),
    path('phone/', phone, name='phone'),

]
