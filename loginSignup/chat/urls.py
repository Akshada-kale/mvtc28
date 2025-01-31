from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.homepage, name='homepage'),
    path('<str:room>/', views.room, name='room'),
    path('chat/checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]