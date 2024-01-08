# 1. Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. Call the function, and make sure the message displays correctly

def display_message():
    print("I am learning funtions")
    
display_message()


# 2. Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as One of my favorite books is Alice in Wonderland. Call the function, making sure to include a book title as an argument in the function call.

def favorite_book(title):
    print(f"One of my favorite books is {title}")
    
favorite_book("The rich also cry")
favorite_book("The good the bad and the ugly")


# 3. T-Shirts:

def make_shirt(size, message):
    print(f"Shirt size: {size.upper()}, Message: '{message}'")

# Call the function using positional arguments
make_shirt("medium", "Bright Day!")

# Call the function using keyword arguments
make_shirt(size="large", message="Life is Good!")


# 4. # Large shirts:
  # Medium shirt

def make_shirt(size="large", message="I love Python"):
    print(f"Shirt size: {size.capitalize()}, Message: '{message}'")

# Make a large shirt with default message
make_shirt()

# Make a medium shirt with default message
make_shirt(size="medium")

# Make a custom-sized shirt with a different message
make_shirt(size="small", message="Data Science!")


# 5. 
# Cities:

def describe_city(city, country="default country"):
    print(f"{city.capitalize()} is in {country.capitalize()}.")

# Call the function for three different cities
describe_city("Reykjavik", "Iceland")
describe_city("Abuja", "Nigeria")
describe_city("Madinah")


# 6.
# City Names:

def city_country(city, country):
    return f"{city.capitalize()}, {country.capitalize()}"

# Call the function with three city-country pairs
result1 = city_country("santiago", "chile")
result2 = city_country("rabat", "morocco")
result3 = city_country("accra", "ghana")

# Print the returned values
print(result1)
print(result2)
print(result3)


# 7. Albums:
def make_album(artist, title, songs=None):
    album = {'artist': artist, 'title': title}
    if songs:
        album['songs'] = songs
    return album

# Make three dictionaries representing different albums
album1 = make_album("Mariah Carey", "Butterfly")
album2 = make_album("Hamisu Breaker", "Da rai nake sonki")
album3 = make_album("Rema", "Calm Down", songs=12)

# Print each return value
print(album1)
print(album2)
print(album3)

# 8.
# User Albums:

def make_album(artist, title, songs=None):
    album = {'artist': artist, 'title': title}
    if songs:
        album['songs'] = songs
    return album

while True:
    artist_input = input("Enter the artist's name (or 'quit' to exit): ")
    if artist_input.lower() == 'quit':
        break

    title_input = input("Enter the album title: ")

    # Call make_album with user input and print the dictionary
    album_info = make_album(artist_input, title_input)
    print(album_info)


# 9.
# Messages:

def show_messages(messages):
    for message in messages:
        print(message)

# List of short text messages
text_messages = [
    "Good Afternoon, how are you?",
    "I would be waiting at home!",
    "Welcome to the world! 🎉",
    "Learning Python is fun!",
]

# Call the function to print each text message
show_messages(text_messages)


# 10. 
#Sending Messages:

def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

# List of short text messages
text_messages = [
    "Good Afternoon, how are you?",
    "I would be waiting for you at home!",
    "Welcome to the World! 🎉",
    "Learning Python is fun!",
]

# Empty list to store sent messages
sent_messages = []

# Call the function to send and print messages
send_messages(text_messages, sent_messages)

# Print both lists to verify
print("Original messages:")
show_messages(text_messages)

print("\nSent messages:")
show_messages(sent_messages)


# 11. 
# Archived Messages: 
def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

# List of short text messages
text_messages = [
    "Hello, how are you?",
    "Don't forget to pick up groceries!",
    "Happy birthday! 🎉",
    "Learning Python is fun!",
]

# Create a copy of the list to pass to send_messages
messages_copy = text_messages.copy()

# Empty list to store sent messages
sent_messages = []

# Call the function to send and print messages using the copy
send_messages(messages_copy, sent_messages)

# Print both lists to verify
print("Original messages:")
show_messages(text_messages)

print("\nSent messages:")
show_messages(sent_messages)


# 12.
# Sandwiches:

def make_sandwich(*items):
    print("Making a sandwich with the following items:")
    for item in items:
        print(f"- {item.capitalize()}")

# Call the function three times with different numbers of arguments
make_sandwich("lettuce", "cheese", "chicken")
make_sandwich("beef", "rolls" , "butter")
make_sandwich("bread", "jam", "peanut butter")


# 13.
# User Profile: 

def build_profile(first_name, last_name, **additional_info):
    profile = {'first_name': first_name, 'last_name': last_name}
    profile.update(additional_info)
    return profile

# Create a profile for yourself
my_profile = build_profile(
    first_name="YourFirstName",
    last_name="YourLastName",
    age=40,
    occupation="Free Lancer",
    location="City, Country"
)

print(my_profile)


# 14.
# Cars: 

def make_car(manufacturer, model, **car_info):
    car = {'manufacturer': manufacturer, 'model': model}
    car.update(car_info)
    return car

# Call the function with required and additional information
car = make_car('subaru', 'outback', color='blue', tow_package=True)

# Print the dictionary to verify the stored information
print(car)


# 15.
# Printing Models: 

from printing_functions import print_models, show_completed_models

# Sample data
unprinted_designs = ['t-shirts', 'car keys', 'rings']
completed_models = []

# Using imported functions
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


'''In this example, the functions print_models and show_completed_models are defined in printing_functions.py, and they are imported into printing_models.py using the import statement. '''

# 16.
# Imports: 
# - import module_name
# - from module_name import function_name
# - from module_name import function_name as fn
# - import module_name as mn
# - from module_name import *

import module

module.my_function()


from module import my_function

my_function()


from module import my_function as fn

fn()


import module as mn

mn.my_function()


from module import *

my_function()


# 17.
# Styling Functions: 

def describe_city(city, country='default country'):
    """Prints a simple sentence describing the city and country."""
    print(f"{city.capitalize()} is in {country.capitalize()}.")

# Example usage
describe_city("Reykjavik", "Iceland")
describe_city("Abuja", "Nigeria")
describe_city("Madina")

