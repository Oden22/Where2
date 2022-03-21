from .models import Resturant, Activity

def format_data(time=0):
    '''Format the data into two dictionaries'''
    resturant_list = [
            {'Breakfast': []},
            {'Lunch': []},
            {'Dinner': []}
        ]
    activities_list = [
            {'Sunny': []},
            {'Raining': []}
        ]

    resturants = Resturant.objects.order_by('time_scene')
    
    #Sorts the resturant instances
    for resturant in resturants:
        if resturant.time_scene == 'BR':
            resturant_list[0]['Breakfast'].append(resturant)
        elif resturant.time_scene == 'LU':
            resturant_list[1]['Lunch'].append(resturant)
        else:
            resturant_list[2]['Dinner'].append(resturant)

    #Stores the activity model
    activities = Activity.objects.order_by('weather')

    #Sorts the activity instances
    for activity in activities:
        if activity.weather == 'SU':
            activities_list[0]['Sunny'].append(activity)
        else:
            activities_list[1]['Raining'].append(activity)

    if time < 11:
        return resturant_list, activities_list
    elif time < 15:
        return resturant_list[1:], activities_list
    elif time < 21:
        return resturant_list[2], activities_list