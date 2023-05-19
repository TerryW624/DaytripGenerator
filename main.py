import random
generation_state = False
#Acts on whether the user wants to generate a Day Trip
while generation_state == False:
    user_input = input('''
Would you like to generate a Day Trip? Y or N
    ''')
    if user_input == "Y":
        generation_state = True
        print('''
Welcome please standby while we find you some fun!
        ''')
    else:
        print("We're sorry to see you go.")
#List Directory
destinations = ["New York", "Los Angeles", "Miami", "Tampa Bay", "Las Vegas"]
new_york_restaurants = ["Keens Steakhouse", "Don Peppe", "Balthazar", "Katz's Deli", "Bemelmans Bar at the Carlyle"]
new_york_entertainments = ["Visit the Statue of Liberty", "Catch a Show On Broadway", "SUMMIT One Vanderbilt Experience", "Manhattan Island Helicopter Tour", "1-Hour Cruise Around Statute of Liberty & Ellis Island"]  
los_angeles_restaurants = ["Philipe the Original", "Musso & Frank Grill", "Pacific Dining Car", "Tam O'Shanter", "El Paseo Inn"]
los_angeles_entertainments = ["Universal Studios Hollywood", "Disney Land", "Knott's Berry Farm", "Aquarium of the Pacific", "The Official Hollywood Sign Walking Tour"]
miami_restaurants = ["Stubborn Seed", "Itamae", "The Surf Club Restaurant", "Boia De", "Ariete"]
miami_entertainments = ["The Miami Experience Party Boat", "Miami Skyline Cruise", "Speedboat Sightseeing Tour of Miami", "Miami to Key West Day Trip", "Private Yacht Cruise with Champagne"]
tampa_bay_restaurants = ["Bern's Steak House", "Bob Heilman's Beachcomber", "Cafe Ponte", "Casa Tina", "The Chattaway"]
tampa_bay_entertainments = ["Tiki Boat", "Guided Tampa Tour", "Dolphin Sightseeing Cruise from Tampa", "Tiki Boat Tour", "Tampa Histry Cruise"]
las_vegas_restaurants = ["Eiffel Tower Restaurant", "Sterling Brunch at Bally's", "Guy Savoy", "Mizumi", "Joë Robuchon"]
las_vegas_entertainments = ["Cirque Du Soleil", "David Copperfield at the MGM Grand Hotel", "Big Bus Las Vegas Open Top Night Tour", "Shark Reef", "The High Roller"]
while generation_state == True:
    user_destination = random.choice(destinations)
    print(f"Your destination will be {user_destination}")
    # sets the variable user_restaurant based on a destination
    def get_restaurant_by_city(destination):
    #placeholder variable
        user_restaurant = ""
        if destination == "New York":
            user_restaurant = random.choice(new_york_restaurants)
        elif destination == "Los Angeles":
            user_restaurant = random.choice(los_angeles_restaurants)
        elif destination == "Miami":
            user_restaurant = random.choice(miami_restaurants)
        elif destination == "Tampa Bay":
            user_restaurant = random.choice(tampa_bay_restaurants)
        elif destination == "Las Vegas":
            user_restaurant = random.choice(las_vegas_restaurants)
        print(f"Your restaurant is {user_restaurant}")
    # sets the variable user_entertainment based on destination  
    def get_entertainment_by_city(destination):
    #placeholder variable
        user_entertainment = ""
        if destination == "New York":
            user_entertainment = random.choice(new_york_entertainments)
        elif destination == "Los Angeles":
            user_entertainment = random.choice(los_angeles_entertainments)
        elif destination == "Miami":
            user_entertainment = random.choice(miami_entertainments)
        elif destination == "Tampa Bay":
            user_entertainment = random.choice(tampa_bay_entertainments)
        elif destination == "Las Vegas":
            user_entertainment = random.choice(las_vegas_entertainments) 
        print(f"You should have fun at {user_entertainment}")
    transportations = ["Plane", "Train", "Car", "Bus"]
    user_transportation = random.choice(transportations)
    print(f"You should arrive and depart by {user_transportation}")
    get_restaurant_by_city(user_destination)
    get_entertainment_by_city(user_destination)
    reroll_state = False
    #End Greetings and user reroll
    while reroll_state == False:
        user_input_2 = input("Would you like to reroll? Y or N ")
        if user_input_2 == "N":
            if user_transportation == "Plane":
                print("Great! Enjoy your Flight!")
                generation_state = False
                break
            elif user_transportation == "Train" or user_transportation == "Bus":
                print("Great! Enjoy your Ride!")
                generation_state = False
                break
            else:
                print("Have a nice drive!")
                generation_state = False
                break
        else:
            reroll_state = True
            #Reroll options and cancel
            while reroll_state == True:
                user_input_3 = input('''
What would you like to reroll?
(1) Destination
(2) Restaurant
(3) Transportation
(4) Entertainment
(Type the number)
(Type "Back" to go back)
        ''')
                if user_input_3 == "1":
                    user_input_4 = input('''
This will reroll Restaurant and Entertainment. 
Are You Sure? 
Y or N
            ''')
                    if user_input_4 == "Y":
                        user_destination = random.choice(destinations)
                        print(f"Your destination will be {user_destination}")
                        get_restaurant_by_city(user_destination)
                        get_entertainment_by_city(user_destination)
                        print(f"You should arrive and depart by {user_transportation}")
                        reroll_state = False
                elif user_input_3 == "2":
                    get_restaurant_by_city(user_destination)
                    reroll_state = False
                elif user_input_3 == "3":
                    user_transportation = random.choice(transportations)
                    print(f"You should arrive and depart by {user_transportation}")
                    reroll_state = False
                elif user_input_3 == "4":
                    get_entertainment_by_city(user_destination)
                    reroll_state = False
                elif user_input_3 == "Back":
                    reroll_state = False