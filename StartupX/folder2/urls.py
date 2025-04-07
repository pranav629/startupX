from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.firstpage,name="firstpage"),
    path('home/',views.home,name='home'), 
    path('home/mentor',views.mentor,name='mentor'),
    path('home/mentor-login/',views.mentor_login,name='mlogin'),
    path('home/mentor-login/mentor-signup/',views.mentor_signup,name='mentorsignup'),
    path('home/entrepreneur-login/entrepreneur-signup/',views.entrepreneur_signup,name='entrepreneursignup'),

    path('home/mentor-login/mentor-signup/mentor-login/',views.redirectments),
    path('home/entrepreneur-login/entrepreneur-signup/entrepreneur-login/',views.redirectents),
    path('home/verify-mentor-email/<str:token>/', views.verify_email, name='verify_email'),
    path('home/verify-entrepreneur-email/<str:token>/', views.verify_entrepreneur_email, name='verify_entrepreneur_email'),
    path('home/entrepreneur-login/',views.entrepreneur_login,name='entlogin'),
    path('home/entrepreneur',views.entrepreneur,name='entrepreneur')

]
