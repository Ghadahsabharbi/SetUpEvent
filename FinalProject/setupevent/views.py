from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Event
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request : HttpRequest):
    return render(request, "setupevent/home.html")


def add_event(request : HttpRequest):
    user : User = request.user

    if not (user.is_authenticated and user.has_perm("setupevent.add_event")):
        return redirect("accounts:login_user")

    val = val1 = val2='non'
    
    if request.user.groups.filter(name='idea_owner').exists():
        val=request.user.get_username()

    elif request.user.groups.filter(name='sponsor').exists():
        val1=request.user.get_username()

    elif request.user.groups.filter(name='autherity').exists():
        val2=request.user.get_username()
      
    if request.method == "POST":
        new_event = Event(idea_owner=val, sponser=val1, autherity =val2, name=request.POST["name"], date = request.POST["date"], place=request.POST["place"] , city=request.POST["city"], status='ignore')
        new_event.save()
    return render(request, "setupevent/add_event.html" , {"event" : Event})



@login_required(login_url="/account/login/")
def view_events(request : HttpRequest ):

    try:

        if "search" in request.GET:
            event = Event.objects.filter(name__contains=request.GET["search"])
        else:
            event = Event.objects.all()
        
    except:
           return render(request , "setupevent/not_found.html")

    return render(request, "setupevent/view_events.html", {"event" : event})
        

def event_details(request : HttpRequest , event_id :int ):
        try:
            event = Event.objects.get(id=event_id)
        
        except:
           return render(request , "setupevent/not_found.html")

        return render(request, "setupevent/event_details.html", {"event" : event})


def sponser_event(request : HttpRequest , event_id :int):
    
    user : User = request.user

    if not (user.is_authenticated and user.has_perm("setupevent.sponser_event")):
        return redirect("accounts:login_user")   
    try:
        event = Event.objects.get(id=event_id)

        if request.method == "POST":
            event.status='sponsered'
            event.save()
    except:

        return render(request , "setupevent/not_found.html")

    return render(request, "setupevent/sponser_event.html", {"event" : event})


def approve_event(request : HttpRequest , event_id :int):
    user : User = request.user

    if not (user.is_authenticated and user.has_perm("setupevent.approve_event")):
        return redirect("accounts:login_user")  
    try:
        event = Event.objects.get(id=event_id)

        if request.method == "POST":
            event.status='approved'
            event.save()
    except:

        return render(request , "setupevent/not_found.html")

    return render(request, "setupevent/approve_event.html", {"event" : event})



