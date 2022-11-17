from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Event
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request : HttpRequest):
    return render(request, "setupevent/cover.html")


def about(request : HttpRequest):
    return render(request, "setupevent/about.html")

def contactus(request : HttpRequest):
    return render(request, "setupevent/contactus.html")


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
        new_event = Event(idea_owner=val, sponser=val1, autherity =val2, name=request.POST["name"], date = request.POST["date"], place=request.POST["place"] , city=request.POST["city"], status='non' ,description=request.POST["description"] )
        new_event.save()
    return render(request, "setupevent/add_event.html" , {"event" : Event})



@login_required(login_url="/account/login/")
def view_events(request : HttpRequest ):
    username=request.user.get_username

    try:
        if "search" in request.GET:
            event = Event.objects.filter(name__contains=request.GET["search"])
        else:
            event = Event.objects.all()
        
    except:
           return render(request , "setupevent/not_found.html")

    
    return render(request, "setupevent/view_events.html", {"event" : event , "username": username})


#events for authority
def view_events2(request : HttpRequest):
    username=request.user.get_username
    try:
        if "search" in request.GET:
            event = Event.objects.filter(name__contains=request.GET["search"])
        else:
            event = Event.objects.all()
        
    except:
           return render(request , "setupevent/not_found.html")

    
    return render(request, "setupevent/view_events2.html", {"event" : event  , "username": username})

#events for sponsor
def view_events1(request : HttpRequest):
    username=request.user.get_username
    try:
        if "search" in request.GET:
            event = Event.objects.filter(name__contains=request.GET["search"])
        else:
            event = Event.objects.all()
        
    except:
           return render(request , "setupevent/not_found.html")

    
    return render(request, "setupevent/view_events1.html", {"event" : event , "username": username})


def event_details(request : HttpRequest , event_id :int ):
        
    try:
        event = Event.objects.get(id=event_id)
        return render(request, "setupevent/event_details.html", {"event":event})
    

    except:
           return render(request , "setupevent/not_found.html")


def sponser_event(request : HttpRequest , event_id :int):
    msg=""
    try:
        event = Event.objects.get(id=event_id)

        if request.method == "POST":
            event.status='sponsered'
            event.save()
            msg="The event is sponsored successfully "
    except:

        return render(request , "setupevent/not_found.html")

    return render(request, "setupevent/sponser_event.html", {"event" : event , "msg": msg})


def approve_event(request : HttpRequest , event_id :int):
    msg=""
    try:
        event = Event.objects.get(id=event_id)

        if request.method == "POST":
            event.status='approved'
            event.save()
            msg="The event is approved successfully "
    except:

        return render(request , "setupevent/not_found.html")

    return render(request, "setupevent/approve_event.html", {"event" : event , "msg": msg})



