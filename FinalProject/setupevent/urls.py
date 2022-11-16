from django.urls import path
from . import views

app_name = "setupevent"

urlpatterns = [
    path("home/", views.home, name="home"),
    path('add_event/',views.add_event , name="add_event"),
    path('view_events/', views.view_events , name="view_events"),
    path("view_events1/" , views.view_events1 , name="view_events1"),
    path('view_events2/', views.view_events2, name="view_events2"),
    path('event_details/<event_id>/', views.event_details, name="event_details"),
    path('sponsor_event/<event_id>/', views.sponser_event , name="sponser_event"),
    path('approve_event/<event_id>/', views.approve_event , name="approve_event"),
    path("about/", views.about , name="about"),
    path('contactus/', views.contactus , name="contactus"),
]