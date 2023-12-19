print( 'Thirty '+ 'Days ' + 'Of ' + 'Python' )

print( 'Coding', 'For' , 'All')

company =  "Coding For All"

print(company)

print(len(company))

print(company.upper())

print(company.lower())

g = "Coding For All"
print(g.capitalize())
print(g.title())
print(g.swapcase())

print(g[0:6])

print(g.find("Coding"))

print(g.replace("Coding", "Python"))

p = "Python for Everyone"
print(p.replace("Everyone", "All"))

ch = 'Coding For All'
print(ch.split()) 

ch = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(ch.split(','))

r = "Coding For All" 
print(r[0]) #C

print(r[-1]) #l

print(r[10]) #" "

acc = 'Python For Everyone'
print(".".join(word[0] for word in acc.split()))

acc = 'Coding For All'
print(".".join(word[0] for word in acc.split()))

text = "Coding For All"
print(text.index("C"))

text = "Coding For All"
print(text.index("F"))

text = "Coding For All People"
position = text.rfind("l")
print(position)

sentence = "You cannot end a sentence with because because because is a conjunction"
position = sentence.index("because")
print(position)

sentence = "You cannot end a sentence with because because because is a conjunction"
position = sentence.rindex("because")
print(position)

sentence = "You cannot end a sentence with because because because is a conjunction"
phrase = sentence[31:54]
print(phrase)

sentence = "You cannot end a sentence with because because because is a conjunction"
position = sentence.index("because")
print(position)

phrase = sentence[31:54]
print(phrase)

text = 'Coding For All' 
print(text.startswith('Coding')) #True

text = 'Coding For All' 
print(text.startswith('coding')) #False

challenge = '   Coding For All      '
print(challenge.strip(' '))

ch = '30DaysOfPython'
print(ch.isidentifier()) # False
challenge = 'thirty_days_of_python'
print(ch.isidentifier()) # True

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = '# '.join(libraries)
print(result)

print("I am enjoying this challenge.\nI just wonder what is next.")

print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

print('{} = {}'.format('radius', 10))
radius = 10
print('{} = {} * {} ** {}'.format('area', 3.14,  'radius', 2))
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

a=8
b=6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))