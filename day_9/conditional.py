user_age = int(input('Enter your age: '))
if user_age >= 18:
    print('You are old enough to drive')
else:
    missing_years = 18 - user_age
    print(f'you need {missing_years} to learn to drive.')  




your_age = int(input('Enter your age: '))
my_age = 25

if your_age > my_age:
    age_difference = your_age - my_age
    if age_difference == 1:
        print(f"you are 1 year older than me")
    else:
        print(f"you are {age_difference} years older than me")
elif my_age < your_age:
    age_difference = my_age - your_age
    if age_difference == 1:
        print(f"i am 1 year older than you")
    else:
        print(f"i am {age_difference}years older than you")
else:
    print("we are the same age")




a = int(input('Enter number one: '))
b = int(input('Enter number two: '))
if a > b:
    print(f'{a} is greater than {b}')
elif a < b:
    print(f'{a} is smaller than {b}') 
else:
    print(f'{b} is equal to {a}')


def student_grade(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"            
    
month = input("Enter a month:")

if month in ["september", "October", "November"]:
    season = "Autum"
elif month in ["December", "January", "February"]:
    season = "Winter"
elif month in ["March", "April", "May"]:
    season = "Spring"
elif month in ["June", "July", "Auust"]:
    season = "Summer"
else:
    season = "invalid match"

print(f"The season for {month} in {season}.")
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_to_add = input("Enter a fruit to check and add: ")

if fruits_to_add in fruits:
    print(f"'{fruits_to_add.capitalize} already exists in the list")
else:
    fruits.append(fruits_to_add)
    print(f"'{fruits_to_add.capitalize()}' has been added to the list. Updated list: {fruits}")

person={
    'first_name': 'Adabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': "Finland",
    'is_married': True,
    'skills': ["Javascript", 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

person={
    'first_name': 'Adabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': "Finland",
    'is_married': True,
    'skills': ["Javascript", 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}


if person['skills']:
    print(person['skills'][2])

if 'Python' in person['skills']:
    print("The persons skills has only Python")
if 'Javascript' and "React" in person['skills']:
    print("He is a frontend developer")
if 'Node' and "MongoDB" and "Python" in person['skills']:
    print("He is a backend developer")
if 'React' and "Node" and "MongoDB " in person['skills']:
    print("He is a fullstack developer")
else:
 print("unknown title")


if person['is_married'] and person['country'] == 'Finland':
    print(f" {person['first_name']} lives in {person['country']}")