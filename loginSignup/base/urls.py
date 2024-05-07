from django.urls import path,include
from .views import authView, homeAk,IT,Art,Graphic,Python,Connect,Teacher,Student,About,Contact

urlpatterns = [
    path("", homeAk, name="home"),
    path("it/",IT,name='it'),
    path("art/",Art,name='artpage'),
    path("python/",Python,name='pythonpage'),
    path("graphic/",Graphic,name='graphicpage'),
    path("connect/",Connect,name='connectpage'),
    path("teacher/",Teacher,name='teacherpage'),
    path("student/",Student,name='studentpage'),
    path("About/",About,name='aboutpage'),
    path("contact/",Contact,name='contactpage'),
    path("signup/", authView, name="authView"),
    path("accounts/", include("django.contrib.auth.urls")),
]
