import random


destinations = ["New York", "Los Angeles", "Miami", "Tampa Bay", "Las Vegas"]
user_destination = random.choice(destinations)
#list directory for entertainment and food by city
new_york_restaurants = ["Keens Steakhou se", "Don Peppe", "Balthazar", "Katz's Deli", "Bemelmans Bar at the Carlyle"]
new_york_entertainments = ["Visit the Statue of Liberty", "Catch a Show On Broadway", "SUMMIT One Vanderbilt Experience", "Manhattan Island Helicopter Tour", "1-Hour Cruise Around Statuteof Liberty & Ellis Island"]
los_angeles_restaurants = ["Philipe the Original", "Musso & Frank Grill", "Pacific Dining Car", "Tam O'Shanter", "El Paseo Inn"]
los_angeles_entertainments = ["Universal Studios Hollywood", "Disney Land", "Knott's Berry Farm", "Aquarium of the Pacific", "The Official Hollywood Sign Walking Tour"]
miami_restaurants = ["Stubborn Seed", "Itamae", "The Surf Club Restaurant", "Boia De", "Ariete"]
miami_entertainments = ["The Miami Experience Party Boat", "Miami Skyline Cruise", "Speedboat Sightseeing Tour of Miami", "Miami to Key West Day Trip", "Private Yacht Cruise with Champagne"]
tampa_bay_restaurants = ["Bern's Steak House", "Bob Heilman's Beachcomber", "Cafe Ponte", "Casa Tina", "The Chattaway"]
tampa_bay_entertainments = ["Tiki Boat", "Guided Tampa Tour", "Dolphin Sightseeing Cruise from Tampa", "Tiki Boat Tour", "Tampa Histry Cruise"]
las_vegas_restaurants = ["Eiffel Tower Restaurant", "Sterling Brunch at Bally's", "Guy Savoy", "Mizumi", "Joë Robuchon"]
las_vegas_entertainments = ["Cirque Du Soleil", "David Copperfield at the MGM Grand Hotel", "Big Bus Las Vegas Open Top Night Tour", "Shark Reef", "The High Roller"]
# sets the variables user_restaurant and user_entertainement based on a destination
def get_restaurant_and_entertainment_by_city(destination):
    #placeholder variables
    user_restaurant = ""
    user_entertainment = ""
    if destination == "New York":
        user_restaurant = random.choice(new_york_restaurants)
        user_entertainment = random.choice(new_york_entertainments)
    elif destination == "Los Angeles":
        user_restaurant = random.choice(los_angeles_restaurants)
        user_entertainment = random.choice(los_angeles_entertainments)
    elif destination == "Miami":
        user_restaurant = random.choice(miami_restaurants)
        user_entertainment = random.choice(miami_entertainments)
    elif destination == "Tampa Bay":
        user_restaurant = random.choice(tampa_bay_restaurants)
        user_entertainment = random.choice(tampa_bay_entertainments)
    elif destination == "Las Vegas":
        user_restaurant = random.choice(las_vegas_restaurants)
        user_entertainment = random.choice(las_vegas_entertainments)
transportations = ["Plane", "Train", "Car", "Bus"]
user_transportation = random.choice(transportations)
get_restaurant_and_entertainment_by_city(user_destination)

