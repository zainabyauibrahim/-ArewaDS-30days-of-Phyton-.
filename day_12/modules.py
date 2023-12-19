# 1. 
#   print(random_user_id());

import random
import string
def random_user_id():
    return "".join(str(random.choice(string.ascii_letters + string.digits)) for i in range(6))

print(random_user_id()) 

# 2.
# print(user_id_gen_by_user()) # user input: 5 5
#output:
#kcsy2
#SMFYb
#bWmeq
#ZXOYh
#2Rgxf
   
# print(user_id_gen_by_user()) # 16 5
#1GCSgPLMaBAVQZ26
#YD7eFwNQKNs7qXaT
#ycArC5yrRupyG00S
#UbGxOFI7UXSWAyKN
#dIV0SSUTgAdKwStr

def user_id_gen_by_user():
    try:
        # Get user input for number of characters and number of IDs
        char_count, id_count = map(int, input("Enter number of characters and number of IDs (separated by space): ").split())
        
        # Define the characters to choose from for the random ID
        characters = string.ascii_letters + string.digits  # letters (uppercase and lowercase) and digits
        
        # Generate user-specified number of IDs each with specified number of characters
        for _ in range(id_count):
            user_id = ''.join(random.choices(characters, k=char_count))
            print(user_id)
    except ValueError:
        print("Please enter valid numbers for characters and IDs.")


# 3. 

def list_of_rgb_colors(num_colors):
    colors = []
    for _ in range(num_colors):
        # Generate random values for RGB components (0-255)
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        
        # Append the RGB tuple to the colors list
        colors.append((red, green, blue))
    
    return colors

# Generate a list of 5 RGB colors
num_of_colors = 5
rgb_colors = list_of_rgb_colors(num_of_colors)
print(rgb_colors)

# Write a function generate_colors which can generate any number of hexa or rgb colors.
# generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
# generate_colors('hexa', 1) # ['#b334ef']
# generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
# generate_colors('rgb', 1)  # ['rgb(33,79, 176)']


def rgb_color_gen():
    a = ','.join(str(random.randint(0,255)) for i in range(3))
    return 'rgb('+ a + ')'
print(rgb_color_gen())


# 1. 
def list_of_hexa_colors(x):
     a= ["".join(str(random.choice('abcdef' + string.digits)) for i in range(6)) for j in range(x)]
     b =['#' + item for item in a]
     return b
list_of_hexa_colors(6) 

# 2. 

def list_of_rgb_colors(x):
    return [rgb_color_gen() for i in range(x)]

list_of_rgb_colors(7)

string.digits

# 3. 

def generate_colors(fun,x):
    if fun == 'hexa':
        result = list_of_hexa_colors(x)
    elif fun == 'rgb':
        result = list_of_rgb_colors(x)

    return result

generate_colors('hexa',3)
generate_colors('rgb',1)



# 1.

def shuffle_list(list):
    random.shuffle(list)
    return list
print(shuffle_list([10,11,12,13,14,]))
    
# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def unique_random_nums():
    return random.sample([0,1,2,3,4,5,6,7,8,9],k=7)
print(unique_random_nums())