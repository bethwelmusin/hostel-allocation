from django.urls import path, include
from . import views

appname = 'hostel'
urlpatterns=[
    path('index/', views.dashboard, name='index'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('', views.dashboard, name='index'),
    path('register/',views.register_view,name='register'),
    path('user_login/',views.user_login,name='loginpage'),
    path("logout", views.logout_request, name="logout"),

]                                                             
