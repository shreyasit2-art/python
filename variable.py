""" print("hello! Shreya")
name = "Shreyshi"
print(name)
num1 = 8.9
num2 = 10
sum = num1 + num2
print(sum)
print(type(num1))
print(type(num2))
l = 4
b = 5
area = l * b
print(area)
x = 10
print(x)


x = 10
x = 20
#x = 50
x = 80
x = 90
print(x)
a, b, c = 1, 2, 3
print(a, b, c)
x = y = z = 5
print(x, y, z)
name = "Shreyshi"
print(name)
age = 25
height = 5.9
print(age, height)
is_active = True
print(is_active)
fruits = ["apple", "banana", "cherry"]
print(fruits)
x = 100
y = "hundred"
print(type(x))
print(type(y))
print(len(y))
"""
"""
# 1. Simple Interest: SI = (P * R * T) / 100
p = 3
r = 4
t = 5
SI = (p* r* t)/100
print(SI)

# 2. Area of Rectangle: A = length * breadth
l, b = 2.5, 7.25
A = (l* b)
text = "Area of rectangle= "
print(text, A)

# 3. Perimeter of Rectangle: 2 * (length + breadth)
l, b = 25, 14
P = 2* (l * b)
text = "Perimeter of rectangle="
print(text, P)

# 4. Swap Two Variables using a third variable

a = "juice"
b = "water"
temp  = a
a = b
b = temp
print("a =", a)
print("b =", b)

# 5. Convert Celsius to Fahrenheit: F = (C * 9/5) + 32

print("Conversion of celsius to fahrenheit:")
C = 15
F = (C * 9/5) + 32
print("F=", F)
a = 2
sq = a**2

# 6. Calculate Square and Cube of a Number
print("Square is", sq)
b = 2
cu = b**3
print("Cube is", cu)

# 7. Calculate Total and Average of 3 Marks
a = 2
b = 3
c = 4
t = (a + b + c)
Avg = (t)/3
print("total:", t, "and average:", Avg)

# 8. Convert Minutes to Seconds
m = 7
sec = m*60
print("7 min in sec=", sec)

# 9. Calculate GST Amount: price + 18%
amt = 100
Gst = (amt * 18/100)
GstAmt = Gst + amt
print("GST on amount=", GstAmt)

# 10. Area of Circle: π * r * r
pi=3.14
r = int(input("enter the value of radius:"))
a = (pi*r*r)
print("area of circle=", a)
"""  """
# 11. Compound Interest: A = P (1 + r/100)^t
p= int(input("enter principle"))
r= int(input("enter rate"))
t= int(input("enter time"))
A= p*(1 + r/100)**t
print("compound interest is=", A) """

# 12. BMI Calculator: weight / (height * height)
w = float(input("enter weight in kg:"))
h = float(input("enter your height in m:"))
bmi = (w / h**2)
print("BMI:", bmi)