#Exercises Level 1

#1. 

def add_two_numbers(a,b):
  sum = a + b
  return sum

print(f'The sum of 3 and 5 is {add_two_numbers(3,5)}')

# 2.

def area_of_circle(r):
  import math
  area = math.pi * r **2
  return area

print(f'The area of a circle of radius 7cm is {area_of_circle(7)} cm2')

# 3.

def add_all_nums(*x):
  sum = 0
  for num in x:
    if type(num)==int or type(num)==float:
      sum +=num
    else:
      sum = 'Please enter a whole number'
  return sum
print(f'The sum of 6,7 and 8 is {add_all_nums(6,7,8)}')

# 4. 

def convert_celsius_to_fahrenheit(x):
  F = x * (9/5) + 32
  return F
print(f'32 degrees celsius is {convert_celsius_to_fahrenheit(32)} in Fahrenheits')

# 5.

def check_season(month):
  if month in ['September','October','November']:
    season = 'Autumn or Fall'
  elif month in ['December','January','February']:
    season = 'Winter'
  elif month in ['March','April','May']:
    season = 'Spring'
  else: 
    season = 'Summer'
  return season

print('March is in: ',check_season('March'))

#6.

def calculate_slope():
    try:
        # Get user input for y, m, and c values
        y_value = float(input("Enter the value of y: "))
        m_value = float(input("Enter the value of m: "))
        c_value = float(input("Enter the value of c: "))

        # Calculate the slope using the formula
        slope = (y_value - c_value) / m_value
        return slope
    except ZeroDivisionError:
        return "The line is vertical, and the slope is undefined."
    except ValueError:
        return "Please enter valid numerical values for y, m, and c."

# Calculate the slope of the linear equation using user input
result_slope = calculate_slope()
print(f"The slope of the linear equation is: {result_slope}")

# 7. 

def solve_quadratic_eqn(a,b,c):
  x1 = (-b + (b**2 - 4 *a*c)**2)/ (2*a)
  x2 = (-b - (b**2 - 4 *a*c)**2)/ (2*a)
  return x1,x2
print(f'The solution set of x2 - 6x + 9 is {solve_quadratic_eqn(1,-6,9)}')

# 8.

def print_list(x):
  for i in x:
    print(i)
print_list(['stem','root','leaf'])

# 9.

def reverse_list(list):
  rev_list = []
  for i in range(len(list)-1,-1,-1):
    rev_list.append(list[i])
  return(rev_list)

reverse_list([3,6,9,12])

# 10.

def capitalize_list_items(list):
  cap_list = []
  for i in range(len(list)):
    cap_list.append(list[i].upper())
  return cap_list

capitalize_list_items(['cup','plate','spoon'])


# 11. 
# food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
# numbers = [2, 3, 7, 9]
# print(add_item(numbers, 5))      [2, 3, 7, 9, 5]

def add_item(list,item):
  list.append(item)
  return list
print(add_item(['maize','rice'],'flour'))

# 12.
def remove_item(data, item):
    new_data = []
    for element in data:
        if element != item:
            new_data.append(element)
    return new_data        




# 13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
# print(sum_of_numbers(5))  # 15
# print(sum_all_numbers(10)) # 55
# print(sum_all_numbers(100)) # 5050

def sum_of_numbers(num):
  sum = 0
  for i in range(num+1):
    sum += i
  return sum
print(f' The sum of numbers upto 5 is {sum_of_numbers(5)}')

# 14.

def sum_of_odds(num):
  sum = 0
  for i in range(num+1):
    if i % 2 ==1:
      sum += i
  return sum

print(f'The sum of odd numbers upto 7 is {sum_of_odds(7)} ')

# 15.

def sum_of_evens(num):
  sum = 0
  for i in range(num+1):
    if i % 2 == 0:
      sum +=i
  return sum
print(f'The sum of even numbers upto 10 is {sum_of_evens(10)} ')



# 1. 
def evens_and_odds(int):
  num_even = 0
  num_odd = 0
  for i in range(int +1):
    if i % 2 == 0:
      num_even += 1
    else: 
      num_odd +=1
  return f'The number of odd are: {num_odd} \nThe number of even are: {num_even}'
print(f'For 100, {evens_and_odds(100)}')

# 2. 
def factorial(x):
  fact = 3
  for i in range(3,x+3):
    fact *= i
  return fact
print(f'The factorial of 8 is {factorial(8)} ')

# 3. 
def is_empty(x):
  if len(x) == 0:
    state = 'Empty'
  else:
    state = 'Not empty'
  return state
print(is_empty(()))

# 4. 
def calculate_mean(list):
  sum = 0
  for i in range(len(list)):
    sum += list[i]
  mean = sum / len(list)
  return mean
print(f'The mean of [1,2,3,4,5]: {calculate_mean([1,2,3,4,5])}')

def calculate_median(list):
  list_length = len(list)
  list.sort()
  if list_length % 2 == 0:
    median = (list[list_length//2] + list[list_length//2 - 1])/2
  else:
    median = list[list_length//2]
  return median

print(f'The median of [1,3,4,5,2]: {calculate_median([1,3,4,5,2])}')
print(f'The median of [1,4,3,2]: {calculate_median([1,4,3,2])}')

def calculate_mode(list):
  dic = {}
  for item in list:
      dic[item] = dic.get(item,0) + 1
  return [i for  i,j in dic.items() if j == max(dic.values()) ]
    
print(f'The mode of [1,1,1,3,4,5,6,6,6,8,8,1,1]: {calculate_mode([1,1,1,3,4,5,6,6,6,8,8,1,1])}')

def calculate_range(list):
  list.sort()
  range = list[len(list)-1] - list[0]
  return range
print(f'The range of [10,90,5,3,6,7]: {calculate_range([10,90,5,3,6,7])}')

def calculate_variance(list):
  sum = 0
  sum_of_diffs = 0
  for i in range(len(list)):
    sum += list[i]
  mean = sum / len(list)
  for i in range(len(list)):
    sum_of_diffs +=  (list[i] - mean ) ** 2
  variance = sum_of_diffs/(len(list) - 1)
  return variance

print(f'The variance of [1,2,4,5,6,7,8]: {calculate_variance([1,2,4,5,6,7,8])}')

def calculate_std(list):
  sum = 0
  sum_of_diffs = 0
  for i in range(len(list)):
    sum += list[i]
  mean = sum / len(list)
  for i in range(len(list)):
    sum_of_diffs +=  ((list[i] - mean ) ** 2)
  sd = (sum_of_diffs/(len(list)-1)) ** (1/2)
  return sd

print(f'The sd of [1,2,4,5,6,7,8] : {calculate_std([1,2,4,5,6,7,8])}')

# 1. 
def is_prime(x):
  div = []
  for i in range(2,x):
     if  x % i == 0:
       div.append(i)
  if len(div) == 0:
    prime = 'Prime'
  else:
    prime = 'Not Prime'
  return prime

print(f'7: {is_prime(7)}')

# 2. 
def check_unique(list):
  if len(list) == len(set(list)):
    result = 'All items are unique'
  else:
    result = 'Some items are duplicated'
  return result
print(f'are items in [Z,Y,X,W,V] unique? : {check_unique([Z,Y,X,W,V])}')

# 3. 
def same_data_type(list):
  types = []
  for i in range(len(list)):
    types.append(type(list[i]))
  types_set = set(types)
  if len(types_set) == 1:
    data = "All items in the list are of the same data type"
  else:
    data = "Items in the list are not of the same data type"
  return data
print(same_data_type([12.4,'foes']))

# 4. 
import re

def is_valid_variable(variable_name):
    # Define the pattern for a valid variable name using regular expression
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'

    # Check if the variable name matches the pattern
    if re.match(pattern, variable_name):
        return True
    else:
        return False

# Test cases
variables_to_check = ['valid_variable', '_valid', '9invalid', 'invalid!']

for variable in variables_to_check:
    print(f"Variable '{variable}': {is_valid_variable(variable)}")

# 5. 
#  the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order.
# the most_populated_countries. It should return 10 or 20 most populated countries in descending order.