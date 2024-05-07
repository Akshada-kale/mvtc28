from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.decorators import login_required


# @login_required
def homeAk(request):
    return render(request, "index.html",{})


def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
    else:
     form =  UserCreationForm()
    return render(request,"registration/signup.html", {"form": form})


def IT(request):
   return render(request,"it.html")

def Art(request):
   return render(request,"art.html")

def Graphic(request):
   return render(request,"graphic.html")

def Python(request):
   return render(request,"python.html")

def Connect(request):
   return render(request,"connect.html")

def Teacher(request):
   return render(request,"teacherpage.html")

def Student(request):
   return render(request,"studentchat.html")

def About(request):
   return render(request,"about.html")

def Contact(request):
   return render(request,"contact.html")