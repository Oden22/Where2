from django.shortcuts import render, redirect
from django.http import Http404
from django.views.generic import TemplateView
from . import weather_itinerary, data_format, get_weather
import threading

itinerary_current = weather_itinerary.Itinerary('current')
itinerary_full = weather_itinerary.Itinerary('full')

def check_weather():
    #Checks the weather once per hour
    get_weather.write_weather_data()
    threading.Timer(3600, check_weather).start()

class HomeView(TemplateView):
    #Homepage view
    check_weather()
    template_name = 'itinerary/main.html'

def itinerary_current_view(request):
    #Weather Itinerary View
    weather = get_weather.get_weather_data()

    itinerary_current.getItinerary()
    
    if weather == True:
        weather_statement = 'Today is a nice Day'
    else:
        weather_statement = 'Today is a bad Day'

    context = {
        'Itinerary': itinerary_current.itinerary,
        'Weather': weather_statement,
        }

    return render(request, 'itinerary/itinerary_page.html', context=context)

def itinerary_full_view(request):
    #Weather Itinerary View
    weather = get_weather.get_weather_data()

    itinerary_full.getItinerary()
    
    if weather == True:
        weather_statement = 'Today is a nice Day'
    else:
        weather_statement = 'Today is a bad Day'

    context = {
        'Itinerary': itinerary_full.itinerary,
        'Weather': weather_statement,
        }

    return render(request, 'itinerary/itinerary_page.html', context=context)


def activity_view(request):
    #Activities page
    resturants, activities = data_format.format_data()
    weather = get_weather.get_weather_data()

    if weather == True:
        activities = activities[0]['Sunny']
    else:
        activities = activities[1]['Raining']

    context = {
        'Activities' : activities
        }

    return render(request, 'itinerary/activities.html', context=context)

def resturant_view(request):
    #Resturants Page
    resturants, activities = data_format.format_data()
    breakfast_resturants = resturants[0]['Breakfast']
    lunch_resturants = resturants[1]['Lunch']
    dinner_resturants = resturants[2]['Dinner']

    context = {
        'Resturant': resturants,
        'Breakfast_Resturants' : breakfast_resturants,
        'Lunch_Resturants' : lunch_resturants,
        'Dinner_Resturants' : dinner_resturants
        }


    return render(request, 'itinerary/resturants.html', context=context)


