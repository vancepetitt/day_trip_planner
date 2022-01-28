#lists
from random import randrange,choice
from day_trip_generator import destination_list
from day_trip_generator import transportation_list
from day_trip_generator import restaurant_list
from day_trip_generator import entertainment_list

trip_components = [transportation_list, destination_list, restaurant_list, entertainment_list]

selected_trip = []

#random selector function
def select_random(list):
    list_length = len(list)
    randomly_selected = randrange(0,list_length)
    return list[randomly_selected]

#destination = choice(destination_list)
#print(destination)

#welcome message
user_name = input('Thank you for your interest in booking a day trip! Please enter your name: ')
print(f'Hello, {user_name}! Thank you for your interest in taking a day trip to the exciting St. Louis, MO - the Gateway to the West! We will generate a few options to make for a perfect day trip - but we will make sure to get your approval before booking! After your options are selected, we will put together an itinerary of your day trip. Now sit back and think about how you would like to spend your day!')
lets_do_this = input('Do we have your permission to get started? Please type "Yes": ')
if lets_do_this == 'Yes' or lets_do_this == 'yes':
    print('Here is your first opton:')
else:
    lets_do_this = input('Sorry - we need your permission to begin putting together a trip for you. Please type "Yes" to continue: ')

#random trip creation
def select_trip_options():
    for component in trip_components:
        selected = False
        while selected == False:
            new_option = select_random(component)
            print(new_option)
            approval = input('Would you like this to be a part of your day trip? Please enter "Yes" or "No": ')
            if approval == 'No' or approval == 'no':
                print("...Generating a new option for you.")
            elif approval == 'Yes' or approval == 'yes':
                selected = True
                selected_trip.append(new_option)
                print('Great! Here is the next component for your day trip:')
            else:
                selected = False
                approval = input('Please type "Yes" or "No": ')


#making the trip
select_trip_options()
#print(selected_trip)

#confirmation message
print(f"Thank you for confirming your day trip, {user_name}! You will start off the day by visiting {selected_trip[1]}, one of the most famous destinations the city has to offer! You will reach your destination via {selected_trip[0]}; always a great option for sightseeing in the city. After you have taken in the sights while {selected_trip[0]}, you'll satisfy your apetite at the popular restuarant '{selected_trip[2]}'. After dinner get excited: because you'll be ending the night by {selected_trip[3]}!")

