dog = {}

dog = {'name': 'mini', 'color':'black', 'breed':'local', 'legs':'brown', 'age': 1}

student = {'first_name':'Rabi', 'last_name':'muhammad', 'gender':'female', 'age':30, 'marital_status':'married', 'skills':['JavaScript', 'Node', 'MongoDB', 'Python'], 'country':'Nigeria', 'city':'Kaduna', 'address':'Zaria'}

print(len(student))

print(student['skills'])

student['skills'].append('HTML')
print(student)

print(student.keys())

print(student.values())

print(student.items())

student.pop('skills')
print(student)

del student