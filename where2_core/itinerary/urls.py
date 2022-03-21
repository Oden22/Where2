from django.urls import path, include
from itinerary import views
from itinerary.views import HomeView, itinerary_current_view, itinerary_full_view, resturant_view, activity_view

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('itinerary_current/', views.itinerary_current_view, name='itinerary_current'),
    path('itinerary_full/', views.itinerary_full_view, name='itinerary_full'),
    path('resturants/', views.resturant_view, name='resturants'),
    path('activities/', views.activity_view, name='activities')
]
