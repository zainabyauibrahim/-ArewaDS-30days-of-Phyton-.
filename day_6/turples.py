# Exercise: Level 1

empty = ()

brothers = ('Walid', 'hajara') 
sisters = ('Hajara', 'Saadatu')

siblings = brothers + sisters

print(len(siblings))

family_members = siblings + ('Musa', 'Hadiza')
print(family_members)


# Exercise: Level 2
*siblings, father, mother = family_members
print(siblings)
print( father, mother)

fruits = ('mango', 'banana', 'orange', 'pawpaw', 'watermelon')
vegetables = ('carrot', 'cabbage', 'onions')
animal = ('dogs', 'cats', 'lizard', 'eagles')

food_stuff_tp = fruits + vegetables + animal
print(food_stuff_tp)

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

print(len(food_stuff_lt))
print(food_stuff_lt[5:7])

print(food_stuff_lt[:3])

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)

print('Iceland' in nordic_countries)