import random 
from . import data_format as df
from . import get_weather
import datetime
from pytz import timezone  


class Itinerary:
    ''' Class for itinerary object '''
    def __init__(self, itinerary_size):
        self.itinerary = []
        self.previous_food = []
        self.previous_activity = []
        self.current_time = 0
        self.get_local_time()
        if itinerary_size == 'current':
            self.resturant_dict, self.activity_dict = df.format_data(int(self.current_time[0:2]))
        elif itinerary_size == 'full':
            self.resturant_dict, self.activity_dict = df.format_data(0)
    
    def get_local_time(self):
        ''' Gets the local time when itinerary is created. '''
        brisbane_tz = timezone('Australia/Brisbane')
        time = datetime.datetime.now(brisbane_tz)
        self.current_time = time.strftime('%H %M')

    def getWhereToEat(self):
        ''' Creates a list of three places to eat '''
        # Get where to eat
        resturant_choices = []

        if len(self.resturant_dict) == 1:
            new_choice = False
            while new_choice == False:
                choice = random.choice(self.resturant_dict['Dinner'])
                if choice not in self.previous_food:
                    resturant_choices.append(choice)
                    new_choice = True
        else:
            #Selects a unique random choice by comparing to previous food.
            for dict in self.resturant_dict:
                new_choice = False
                key = list(dict.keys())[0]
                while new_choice == False:
                    choice = random.choice(list(dict[key]))
                    if choice not in self.previous_food:
                        resturant_choices.append(choice)
                        new_choice = True

        self.previous_food = resturant_choices
        return resturant_choices

    def getActivities(self, good_weather, for_itinerary):
        ''' Get the two weather based activities '''
        activity_choices = []

        #Chooses the two activities
        def loop_activities(type_of_day, index):
            x=0
            while x <= 1:
                x += 1
                new_choice = False
                while new_choice == False:
                    activity = random.choice(list(self.activity_dict[index][type_of_day]))
                    if activity not in self.previous_activity and activity not in activity_choices:
                        activity_choices.append(activity)
                        new_choice = True
                    else:
                        pass

        if good_weather != True:
            # Get wet activites
            loop_activities('Raining', 1)
        else:
            # Get dry activites
            loop_activities('Sunny', 0)

        self.previous_activity = activity_choices  

        # If a single activity should be choosen
        if for_itinerary != True:
            return activity_choices[0]
        else:
            return activity_choices[0], activity_choices[1]

    def getItinerary(self):
        ''' Creates the Itinerary'''
        weather = get_weather.get_weather_data()
        activity_1, activity_2 = self.getActivities(weather, True)
        resturant_choices = self.getWhereToEat()

        if len(resturant_choices) == 3:
            self.itinerary = [
                resturant_choices[0],
                activity_1, 
                resturant_choices[1], 
                activity_2, 
                resturant_choices[2]]
        elif len(resturant_choices)	== 2:
            self.itinerary = [
                resturant_choices[0], 
                activity_2, 
                resturant_choices[1]]
        elif len(resturant_choices) == 1:
            self.itinerary = [resturant_choices[0]]