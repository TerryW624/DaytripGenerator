import random


destinations = ["New York", "Los Angeles", "Miami", "Tampa Bay", "Las Vegas"]

    new_york_restaurants = [""]
    new_york_entertainments = [""]
    los_angeles_restaurants = [""]
    los_angeles_entertainments = [""]
    miami_restaurants = [""]
    miami_entertainments = [""]
    tampa_bay_restaurants = [""]
    tampa_bay_entertainments = [""]
    las_vegas_restaurants = [""]
    las_vegas_entertainments = [""]
transportations = ["Plane", "Train", "Car", "Bus"]
user_destination = random.choice(destinations)
user_transportation = random.choice(transportations)

    
#These are lists that should be localized to the destinations on destinations lists
#restaurants = [] 
#entertainment_items = []
#I need a function that will take a destination and give me possible restaurants and entertainment.
#We need at least 3 local restaurants per destination
#We need at least 3 local entertainment types per destination.
