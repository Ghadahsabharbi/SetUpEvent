from django.urls import path
from . import views

app_name = "setupevent"

urlpatterns = [
    path("home/", views.home, name="home"),
    path('add_event/',views.add_event , name="add_event"),
    path('view_events/', views.view_events , name="view_events"),
    path('event_details/<event_id>/', views.event_details, name="event_details")
]