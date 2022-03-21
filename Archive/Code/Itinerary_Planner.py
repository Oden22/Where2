import random
from Get_Weather import weather_forcast, current


#Where to eat
food = {
	'breakfast' : {
		'mermaids by the bay' : {
				'rating' : 4.4,
				'address' : '2 Bayview Terrace, Deception Bay QLD 4508',
				'description' : 'Fish & Chips takeaway with a magnificent waterfront dine in restaurant',
				'cost' : 'medium'
			},

		'Sea Salt and Vine' : {
				'rating' : 4.4,
				'address' : 'Reef Point Esplanade, Scarborough QLD 4020',
				'description' : "Our menu is contemporary Australian cuisine. " +
								"We have some café favourites combined with a " +
								"selection of modern affordable dishes. Enjoy our " +
								"delicious breakfast menu from 7AM and light meals " +
								"and lunch available from 11.30AM daily!",
				'cost' : 'medium'
			},

		'The Bold Bean Cafe' : {
				'rating' : 4.4,
				'address' : '49 Flinders Parade, North Lakes QLD 4509',
				'description' : 'boutique breakfast and coffee',
				'cost' : 'cheap'
			}
	},

	'lunch' : {
		'Moreton Bay Boat Club' : {
				'rating' : 4.2,
				'address' : "Bird O'Passage Parade, Scarborough QLD 4020",
				'description' : "Situated on the most northern tip of the Redcliffe " +
								"Peninsula, the Moreton Bay Boat Club has spectacular " +
								"views of the Glass House Mountains and overlooks our " +
								"118 berth marina.",
				'cost' : 'high'
			},

		'Tempest Seafood Restaurant and Teppanyaki Grill' : {
				'rating' : 4.5,
				'address' : 'Boat Harbour, Bird Opassage Parade, Scarborough QLD 4020',
				'description' : 'Fresh seafood and Teppanyaki down on the waterfront',
				'cost' : 'medium' 
			},

		'The Oasis On The Esplanade' : {
				'rating' : 4.5,
				'address' :  '163 Redcliffe Parade, Redcliffe QLD 4020',
				'description' : 'Serving great food and Genovese coffee in an alfresco ' +
								'setting with views across the bay and looking out to ' +
								'Moreton Island you can sit back, enjoy a glass of wine ' +
								'and soak in the views.',
				'cost' : 'low'
			}
	},

	'dinner' : {
		"What's in the Pot? Osteria" : {
			'rating' : 4.6,
			'address' : "133-137 Redcliffe Parade Shop 5 Cominos Arcade, Redcliffe QLD 4020",
			'description' : "A flavor that would respect the culinary traditions" +
							"of our beloved Italian Region: Tuscany",
			'cost' : 'high'
		},

		"Beardy's Bar and Kitchen" : {
			'rating' : 4.8,
			'address' : '405 Elizabeth Ave, Kippa-Ring QLD 4021',
			'description' : "Offering one of the best selections of Craft Beer in" +
							"the area coupled with awesome burgers and a chilled atmosphere" +
							", it is the perfect place to catch up, chill out or pig out.",
			'cost' : "medium"
		},

		"The Rustic Olive Italian Kitchen" : {
			'rating' : 4.5,
			'address' : "79 Redcliffe Parade, Redcliffe QLD 4020",
			'description' : "A bustling, compact BYO eatery with an outdoor dining area, serving classic Italian dishes",
			'cost' : 'medium'
		}
	},
}

#What to do
wet_activities = {
	"Westfield Shopping Centre" : {
    	"address" : "Gympie Rd, Chermside QLD 4032",
    	"description" : "Westfield is your one-stop destination for shopping, leisure and entertainment. " +
    					"Discover 1000s of popular retailers in fashion, home, decor and more.",
    	"cost": "medium"
	},

    "Snap Fitness" : {
        "address": "Tenancy 4 Market Square, Bay Ave, Deception Bay QLD 4508 ",
        "description": "If you looking for more than just a gym, Snap Fitness Deception Bay is that.",
        "Cost": "low"
    },
}

dry_activities = {
	"Apex Park" : {
    	"address": "2 Morayfield Road, Morayfield 4510",
    	"description": "Located adjacent to Centenary Lakes, Apex Park is a medium sized park with a" +
    					"covered fenced playground and many other facilities for the family to enjoy.",
    	"cost":"Free"
    },
	
    "Yoga at Lake Eden" : {
    	"address":"Lake Eden,  Lakefield Drive, North Lakes 4509",
        "description": "Yoga for all ages and genders, bring the whole family along and enjoy a relaxing" + 
				       "afternoon of stretching and flexing as well as the benefits of being" +
				       "in the outdoors and watching the beautiful wildlife on Lake Eden",
        "cost":"Free"
    }, 
}

activity_1 = ''
activity_2 = ''

previous_food = []
previous_activities = []

def where_to_eat():
	global previous_food
	# Get where to eat
	breakfast = random.choice(list(food['breakfast'].items()))
	lunch = random.choice(list(food['lunch'].items()))
	dinner = random.choice(list(food['dinner'].items()))

	while breakfast[0] in previous_food or lunch[0] in previous_food or dinner[0] in previous_food:
		breakfast = random.choice(list(food['breakfast'].items()))
		lunch = random.choice(list(food['lunch'].items()))
		dinner = random.choice(list(food['dinner'].items()))

	previous_food = [breakfast[0], lunch[0], dinner[0]]

	return breakfast, lunch, dinner

def get_activities(good_weather, for_itinerary):

	activity_1 = ''
	activity_2 = ''

	if good_weather != True:
	# Get activites
		while activity_1 == activity_2:
			activity_1 = random.choice(list(wet_activities.items()))
			activity_2 = random.choice(list(wet_activities.items()))

	else:
		while activity_1 == activity_2:
			activity_1 = random.choice(list(dry_activities.items()))
			activity_2 = random.choice(list(dry_activities.items()))

	if for_itinerary != True:
		return activity_1
	else:
		return activity_1, activity_2

def get_itinerary():
	''' Creates the Itinerary'''
	nice_day = weather_forcast()
	breakfast, lunch, dinner = where_to_eat()
	activity_1, activity_2 = get_activities(nice_day, True)

	itinerary = [breakfast, activity_1, lunch, activity_2, dinner]	
	return itinerary

first_itinerary = get_itinerary()

print(f"Todays weather is Sunny with {current['gust_kmh']}kmh winds and {current['rain_trace']}% chance of rain")

count = 0
options = ['Breakfast :', 'Activity 1 :', 'Lunch :', 'Activity 2 :', 'Dinner :']
for option in first_itinerary:
	print(f"\n{options[count]}")
	count += 1
	print(option[0].title())
	for key, value in option[1].items():
		print(f"\t{key} : {value}")
