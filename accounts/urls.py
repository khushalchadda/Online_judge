
from django.contrib import admin
from django.urls import path,include
from accounts.views import user_login,user_register,user_logout

urlpatterns = [
    path('register/', user_register,name="user_register"),
    path('login/', user_login,name="user_login"),
    path('logout/', user_logout,name="user_logout"),
]
