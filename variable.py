# """ print("hello! Shreya")
# name = "Shreyshi"
# print(name)
# num1 = 8.9
# num2 = 10
# sum = num1 + num2
# print(sum)
# print(type(num1))
# print(type(num2))
# l = 4
# b = 5
# area = l * b
# print(area)
# x = 10
# print(x)


# x = 10
# x = 20
# #x = 50
# x = 80
# x = 90
# print(x)
# a, b, c = 1, 2, 3
# print(a, b, c)
# x = y = z = 5
# print(x, y, z)
# name = "Shreyshi"
# print(name)
# age = 25
# height = 5.9
# print(age, height)
# is_active = True
# print(is_active)
# fruits = ["apple", "banana", "cherry"]
# print(fruits)
# x = 100
# y = "hundred"
# print(type(x))
# print(type(y))
# print(len(y))
# """
# """
# # 1. Simple Interest: SI = (P * R * T) / 100
# p = 3
# r = 4
# t = 5
# SI = (p* r* t)/100
# print(SI)

# # 2. Area of Rectangle: A = length * breadth
# l, b = 2.5, 7.25
# A = (l* b)
# text = "Area of rectangle= "
# print(text, A)

# # 3. Perimeter of Rectangle: 2 * (length + breadth)
# l, b = 25, 14
# P = 2* (l * b)
# text = "Perimeter of rectangle="
# print(text, P)

# # 4. Swap Two Variables using a third variable

# a = "juice"
# b = "water"
# temp  = a
# a = b
# b = temp
# print("a =", a)
# print("b =", b)

# # 5. Convert Celsius to Fahrenheit: F = (C * 9/5) + 32

# print("Conversion of celsius to fahrenheit:")
# C = 15
# F = (C * 9/5) + 32
# print("F=", F)


 # 6. Calculate Square and Cube of a Number
#  a = 2
# sq = a**2
# print("Square is", sq)
# b = 2
# cu = b**3
# print("Cube is", cu)

# # 7. Calculate Total and Average of 3 Marks
# a = 2
# b = 3
# c = 4
# t = (a + b + c)
# Avg = (t)/3
# print("total:", t, "and average:", Avg)

# # 8. Convert Minutes to Seconds
# m = 7
# sec = m*60
# print("7 min in sec=", sec)

# # 9. Calculate GST Amount: price + 18%
# amt = 100
# Gst = (amt * 18/100)
# GstAmt = Gst + amt
# print("GST on amount=", GstAmt)

# # 10. Area of Circle: π * r * r
# pi=3.14
# r = int(input("enter the value of radius:"))
# a = (pi*r*r)
# print("area of circle=", a)
# """  """
# # 11. Compound Interest: A = P (1 + r/100)^t
# p= int(input("enter principle"))
# r= int(input("enter rate"))
# t= int(input("enter time"))
# A= p*(1 + r/100)**t
# print("compound interest is=", A) """


# # 12. BMI Calculator: weight / (height * height)
# w = float(input("enter weight in kg:"))
# h = float(input("enter your height in m:"))
# bmi = (w / h**2)
# print("BMI:", bmi)

# 13. Total Salary = Basic + HRA(20%) + DA(40%)
# b= int(input("Enter your basic salary:"))
# hra= b*20/100
# d= b*40/100
# tot= (b + hra + d)
# print("Your total salary is:", tot)

# # 14. Calculate Discount on a Product
# mrp= int(input("Enter MRP:"))
# dis= mrp*20/100
# dm= mrp - dis
# print("Discount:", dis)
# print("discounted prince:", dm)

# 15. Fahrenheit to Celsius: C = (F − 32) * 5/9
# print("Conversion of fahrenheit to celcius:")
# F = 15
# C = (F-32)*5/9
# print("F=", C)

# 16. Electricity Bill Calculator (slab wise)
# unit=float(input("Enter total unit:"))
# bill= 0
# if unit<=100:
#     bill= unit*1
# elif unit<=200:
#     bill= (100*1) + (unit - 100)*2
# else:
#     bill= (100*1) + (100*2) + (unit-200)*3
#     print("Total electricity bill= ", bill)

 # 17. Calculate Speed = distance / time
# d= float(input("enter distance in meter"))
# t= float(input("enter time in sec"))
# s= d/t
# print("Speed=", s, "m/s")

# 18. Grading System based on average marks
# marks= float(input("enter total marks obtained="))
# sub= float(input("enter total number of subjects="))
# avg= marks/sub
# if 90<=avg<=100:
#     print("Grade= A")
# elif 80<=avg<90:
#     print("Grade= B")
# elif 70<=avg<80:
#     print("Grade= C")
# elif 60<=avg<70:
#     print("Grade= D")
# elif 40<=avg<60:
#     print("Grade= E")
# else:
#     print("Grade= F")

# 19. Convert Days to Years, Months, Days
# td= int(input("Enter number of days="))
# y= td//365
# rd= td%365
# m= rd//30
# d= rd%30
# print(y, "years,", m, "months,", d, "days.")

# 20. SI with different rates for each year
# p= float(input("Enterprinciple amount="))
# si = 0
# year = int(input("Enter year:"))
# for x in range(1,year+1):
#     r1= float(input(f"Enter rate for {x} year="))
#     si = p*r1*year/100
# print(si)

# 21. EMI Calculator


# 22. Profit & Loss % Calculator
# cp= float(input("Enter cost price="))
# sp= float(input("Enter selling price="))
# profit= sp - cp
# if profit>0:
#     pperc= (profit / (cp + sp))*100
#     print("The profit percent=", pperc)
# else:
#     perc= (profit / (cp + sp))*100
#     print("The loss percent=", perc)

# # 23. Distance Between Two Points
# #  taking coordinates of A
# x1= float(input("Enter point A cordinate 'x1'="))
# y1= float(input("Enter point A cordinate 'y1'="))
# # taking coordinates of B
# x2= float(input("Enter point B cordinate 'x2'="))
# y2= float(input("Enter point B cordinate 'y2'="))

# # distance travelled horizontally
# x=0
# if x1>x2:
#     x= x1-x2
# else:
#     x= x2-x1

# # distance travelled vertically
# y=0
# if y1>y2:
#     y= y1-y2
# else:
#     y= y2-y1
# # squaring  both values
# X = x**2
# Y = y**2

# # the slope squared
# S= X+Y
# # slope value
# s= S**(0.5)
# print("The distance between the two points is=", s)

# # 24. Loan Eligibility Checker
# age= int(input("Enter your age="))
# income= input("Enter your monthly income")
# emptype= input("Enter your employment (SL= Salaried, SE= Self employed, NA= Not applicable)").lower()
# emi= int(input("Enter total emi percent of income, if applicable, else enter 0="))

# loan="Not applicable"
# if 18>=age<65:
#     loan="Is applicable"
# elif int(income)<20000:
#     loan="Is applicable"
# elif emptype=="sl" and emptype=="se":
#     loan="Is applicable"
# elif emi<=40:
#     loan="Is applicable"
# else:
#     loan="Not applicable"

# print("Loan eligibility=", loan)

# # 25. Percentage Calculator for 5 Subjects
# s1= float(input("Enter marks of subject 1="))
# s2= float(input("Enter marks of subject 2="))
# s3= float(input("Enter marks of subject 3="))
# s4= float(input("Enter marks of subject 4="))
# s5= float(input("Enter marks of subject 5="))
# total= s1+s2+s3+s4+s5
# avg= total/5
# print("Percentage=", avg)

# # 26. Volume of Cylinder: π * r² * h
# pi=3.14
# r= float(input("Enter radius of cylinder in cm="))
# h= float(input("Enter height of cylinder in cm="))
# vol= pi*r**2*h
# print("Volume of cylinder=", vol, "cm^3")

# # 27. Currency Converter (INR to USD/EUR)
# inr= float(input("Enter amount in INR="))
# usd= inr*0.01113
# eur= inr*0.0095
# print("Amount in USD=", usd, "USD")
# print("Amount in EUR=", eur, "EUR")

# # 28. GST Split: CGST + SGST
# amt= float(input("Enter amount="))
# G= float(input("Enter GST percentage (e.g., 18 for 18%)="))
# cgst= amt*(G/2)/100
# sgst= amt*(G/2)/100
# tot= amt + cgst + sgst
# print("GST=", tot,)

# # 29. CAGR: (End/Start)^(1/n) - 1
# start= float(input("Enter initial amount="))
# end= float(input("Enter final amount="))
# n= int(input("Enter number of years="))
# cagr= (end/start)**(1/n) - 1
# print("CAGR=", cagr)
# print("CAGR%=", cagr*100, "%")

# # 30. Working Hours Salary with Overtime
# hrs= float(input("Enter total number of hours worked in a week="))
# hw= float(input("Enter your hourly wage="))
# otr= float(input("Enter overtime rate="))
# nwh=9*5
# ot=nwh - hrs
# if hw>nwh:
#     sal= (nwh*hw) + ((hrs -nwh)*otr)
# else:
#     sal= hrs*hw

# print("Total salary= Rs.", sal)
