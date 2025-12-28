# 1. Write a program to check if a number is positive or negative
num= int(input("Enter a number="))
if num < 0:
    print("The number is negative.")
else:
    print("The number is positive.")

# 2. Write a Python program to check whether a number is even or odd using if-else
num= int(input("Enter a number="))
if num%2==0:
    print("The number is even.")
else:
    print("The number is odd.")

# 3. Write a program to input a person's age and print 'Minor' if less than 18, 'Adult' if between 18 and 60, and 'Senior' if 60 or above
age=int(input("enter your age="))
if age <18:
    print("Minor.")
elif 18<age<60:
    print("Adult.")
else:
    print("Senior.")

# 4. Write a program that checks if a character entered is a vowel or a consonant
ch= input("Enter an alphabet character=")
if ch in ("aeiou"):
    print("Entered character is a vowel.")
else:
    print("Entered character is a consonant.")

# 5.Write a Python program to check if a number is divisible by 3 and 5 both.
num= int(input("Enter a number="))
if num%15==0:
        print("The number is divisible by 3 and 5 both.")
else:
    print("The number is not divisible by 3 and 5 both.")

# 6. Write a Python program to input marks of a student and print the grade: 
marks= float(input("enter total marks obtained="))
sub= float(input("enter total number of subjects="))
avg= marks/sub
if 90<=avg<=100:
    print("Grade= A")
elif 80<=avg<90:
    print("Grade= B")
elif 70<=avg<80:
    print("Grade= C")
elif 60<=avg<70:
    print("Grade= D")
elif 40<=avg<60:
    print("Grade= E")
else:
    print("Grade= F")

# 7. Write a program that takes input for two numbers and prints which one is greater or if they are equal.
a = int(input("enter first number"))
b = int(input("enter second number"))
if a < b:
    print("b is greater than a.")
elif a == b:
    print("a is equal to b.")
else:
    print("a is greater than b.")

# 8.Write a program that checks whether a year is a leap year or not.
year= int(input("Enter a year="))
if (year%4==0 and year%100!=0) or (year%400==0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# 9. Write a Python program that simulates a simple login system with a stored username and password. Use if-else to check credentials.

username= "admin"
password= "pass123"
user= input("Enter username=")
pwd= input("Enter password=")
if user == username and pwd == password:
    print("Login successfull.") 
else:
    print(" Incorrect credentials.")

# 10. Write a calculator program that takes two numbers and an operator (+, -, *, /) from the user and performs the operation using if-elif-else

num1 = float(input("Enter first number="))
num2 = float(input("Enter second number="))
op = input("Enter any operator (from:+,-,*,/ )=")
if op== "+":
    print("The sum=", num1 + num2)
elif op == "-":
    print("The difference=", num1 - num2)
elif op== "*":
    print("The product=", num1 * num2)
elif op== "/":
    print("The quotient=", num1 / num2)
else:
    print("Please enter correct operator.")
