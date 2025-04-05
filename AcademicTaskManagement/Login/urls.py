from django.urls import path
from Login import views

urlpatterns =[

    path('logIn_page/', views.logIn_page, name = "logIn_page"),
    path('signUp_page/', views.signup_page, name = "signUp_page"),
    path('home_page/', views.home_page, name = "home_page"),
    path('calender_page/', views.calender_page, name="calender_page"),
    path('logout/',views.logout,name="logout"),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),

]