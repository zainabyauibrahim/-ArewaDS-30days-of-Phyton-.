'Day 2: 30 Days of python programming'
first_name = 'Zainab'
last_name = 'Ibrahim'
full_name = 'Zainab yau'
country = 'Nigeria'
city = 'Zaria'
age = '100'
year = '2023'
is_married = True
is_true = True
is_light_on = False
first_name, last_name, country, age, is_married = 'Zainab', 'Ibrahim', 'Nigeria', '100', True

print('First name length: ', len(first_name))
print('First name length:' ,len(first_name), 'Last name length: ', len(last_name))

print('First name:', first_name)
print('Last name: ', last_name)
print('Full name: ', full_name)
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print("year: ", year )
print('Married: ', is_married)
print('is true: ', is_true)
print('is Light: ', is_light_on)

# Exercises: Level 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print(len(first_name))

print(f"lenght of first name is {len(first_name)} the last name is{len(last_name)}")
print(len(last_name) < len(first_name))

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two


radius = 30

area_of_circle = (22/7) * radius ** 2
print(area_of_circle)

circum_of_circle = 2 * (22/7) * radius
print(area_of_circle)

radius = float(input("Enter the radius: "))
area_of_circle = (22/7) * radius ** 22
print(area_of_circle)

first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
country = input("Enter Country: ")
age = input("Enter Age: ")