from django.urls import path

from .import views

urlpatterns =[
    #when thye come to home directory it goes to views.py and it go for function
    path('', views.home, name='home'),
    #passing varibale in this room 
    #below slash is look automatically for rooms (create function name of room in views.py)
    path('<str:room>/', views.room, name='room'), #it go to room.html-> again come to this below function
   #string with name room (slash /anything want to add it)
    #below one check wheter the room is exist or not 
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'), 
    #this url print all the message which we snet or reload
    #storing the messages of particalr/differnet rooms
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'), #it go view.py
  



]