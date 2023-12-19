age = 35
height = 30
complex = 1+4j

base = float(input("Enter Base: "))
height = float(input("Enter height: "))
area = 0.5 * base * height
print(f"The area of the triangle is {area}")

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
perimeter = a + b + c
print(f"The perimeter of the triangle is {perimeter}")

length = float(input("Enter Length: "))
width = float(input("Enter Width: "))
area = length * width
perimeter = 2 * (length + width)
print(f"the area of the rectangle is {area}, and the perimeter is {perimeter} ")

r = float(input("Enter Radius: "))
pi = 3.14
area = pi * r ** 2
circumference = 2 * pi * r
print(f"the area of the circle is {area} a3nd the circumference is {circumference}")

#slope
y = lambda x: 2 * x - 2
slope1 = (y(1) - y(0)) / (1 - 0)
print("The slope is", slope1)

import math
a1 = 2
b1 = 2
a2 = 6
b2 = 10
slope2 = (b2-y1)/(b2-a1)
print(f"the slope is {slope2}")
dst = math.sqrt((a2 - a1)**2 + (b2 - b1)**2)
print(f"The Euclidian distance between (2, 2) and (6, 10) is {dst}")

if slope1 == slope2:
    print("the slopes are the same")
elif slope1 > slope2:
    print("the first slope is greater")
else:
    print("the second slope is greater")

def y(x):
    return x**2 + 6*x + 9

print("y(0) =", y(0))
print("y(-1) =", y(-1))
print("y(-2) =", y(-2))
print("y(-3) =", y(-3))
print("y(-4) =", y(-4))
print("y(-5) =", y(-5))

print("You can see that y is 0 when x is -3. This means that -3 is the root of the equation y = x^2 + 6x + 9")

x_1,x_2 = len("python"), len("dragon")
print(x_1 != x_2 )

print("on" in "python" and "dragon")

print("jargon" in "I hope this course is not full of jargon")

print("on" not in "python" and "dragon")

n = len("python")
n = float(n)
n = str(n)
print(f"{n} and {type(n)}")

even = float(input("Enter no:"))
if even % 2 == 0:
    print("this is an even number")
else:
    print("this is an odd number")
    
print(7 // 3 == int(2.7))

print(type('10') == type(10))

print(int(9.8) == 10)

hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
weekly = hours * rate
print(f"Your weekly earning is {weekly}")

yrs = float(input("Enter number of years you have lived: "))
sec = yrs * 365 * 24 * 60 * 60
print(f"You have lived for {sec}seconds.")

print(1 1 1 1 1)
print(2 1 2 4 8)
print(3 1 3 9 27)
print(4 1 4 16 64)
print(5 1 5 25 125)