it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises: Level 1

print(len(it_companies))

it_companies.add('Twitter')
print(it_companies)

it_companies.update(['Cisco', 'NITDA', 'NCAIR'])
print(it_companies)

it_companies.remove('NCAIR')
print(it_companies)

# What is the difference between remove and discard
# If the item is not found remove() method will raise errors,
# However, discard() method doesn't raise any errors.

# Exercises: Level 2

C = A.union(B)
print(C)

print(A.intersection(B))

print(A.issubset(B))

print(A.isdisjoint(B))

print(A.union(B) & B.union(A))

A.symmetric_difference(B)

del A, B

ages = set(age)
print(ages)
print(len(age) > len(ages))


# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people'
sentence = sentence.split(' ')
print(sentence)
print(sentence[8], " and ", sentence[10])