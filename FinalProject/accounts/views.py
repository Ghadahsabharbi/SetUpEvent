from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.models import User , Group
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def register_user(request : HttpRequest):
    
    if request.method == "POST":

        new_user = User.objects.create_user(username=request.POST["username"], email= request.POST["email"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], password=request.POST["password"])
        new_user.save()
        

        if request.POST["group"] == 'idea_owner':
            group=Group.objects.get(name='idea_owner')
            new_user.groups.add(group)


        elif request.POST["group"] == 'sponsor':
            group=Group.objects.get(name='sponsor')
            new_user.groups.add(group)

        else:
            group=Group.objects.get(name='authority')
            new_user.groups.add(group)
            
        return redirect("accounts:login_user")

    return render(request, "accounts/register.html")

def login_user(request : HttpRequest):
    msg = ""
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
    
        if user.groups.filter(name='sponsor').exists():
            login(request, user)
            return redirect("setupevent:view_events1")

        elif user.groups.filter(name='authority').exists():
            login(request, user)
            return redirect("setupevent:view_events2")

        elif user.groups.filter(name='idea_owner').exists():
            login(request, user)
            return redirect("setupevent:view_events")
            
        else:
            msg = "User Not Found , check your credentials"

    return render(request, "accounts/login.html", {"msg" : msg})


def logout_user(request: HttpRequest):

    logout(request)

    return redirect("setupevent:home")

