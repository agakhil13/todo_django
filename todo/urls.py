from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name="home"),
    path('login',views.login, name="login"),
    path('register',views.register, name="register"),
    path('logout',views.logout, name="logout"),
    path('delete/<str:pk>',views.delete, name="delete"),
    path('status/<str:pk>',views.status, name="status"),
    path('clearall',views.clearall, name="clearall"),
]
