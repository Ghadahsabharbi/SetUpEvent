from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Event

# Create your views here.
def home(request : HttpRequest):
    return render(request, "setupevent/home.html")


def add_event(request : HttpRequest):
    if request.method == "POST":
        new_event = Event(idea_owner='ghadah', sponser='ghadah1', autherity ='ghadah2', name=request.POST["name"], date = request.POST["date"], place=request.POST["place"] , city=request.POST["city"], status='ignore')
        new_event.save()
    return render(request, "setupevent/add_event.html" , {"event" : Event})


def view_events(request : HttpRequest ):
        try:
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