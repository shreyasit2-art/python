

""" for n in range(1, 11):
    print(n) """

# 2. Print all even numbers between 1 and 20
# for x in range(1,21):
#     if x%2==0:
#         print(f"{x} is even")
#     """ else:
#         print(f"{x} is odd") """
    
# for y in range(1, 51):
#     if y%2!=0:
#         print(f"{y} is odd")

# # 3. Print the multiplication table of 5
# table= int(input("Enter number to get table="))
# for x in range(1, 11):
#     y= x*table
#     print(f"{table} * {x} = {y}")

# 4. Sum all numbers from 1 to 100
# tot = 0
# for x in range(1,101):
#     tot+= x
# print(tot)

# 5. Print each character of a string
# name = ("SHREYSHI")
# for x in name:
#     print(f"{x}")

# 6. Reverse a string using a for loop.
# name = "GRACY"
# print(name[: :-1])

# 7. Find the largest number in an array.
# num= [6, 8, 3, 9, 15]
# lar=num[0]
# for x in num:
#     if x>lar:
#         lar = x
# print(lar)

# 8.  Count vowels in a string.
# word = input("Enter a word=").lower()
# count= 0
# for x in word:
#     if x in "aeiou":
#         count += 1
# print("Number of vowels+", count)

# #9.  Print star pattern using for loop
# for r in range(1,6):
#     print("*" * r)

# # 10. Calculate factorial of a number
# n= int(input("Enter a number="))
# fact= 1
# for x in range(1, n+1):
#     fact= fact * x
# print("Factorial is=", fact)

# # 10. Remove duplicate values from an array.
# arr= [2, 3, 4, 2, 5, 3, 6]
# unique_arr= []
# for x in arr:
#     if x not in unique_arr:
#         unique_arr.append(x)
# print("Array with unique values=", unique_arr)

# 11. Create your own map() using a for loop.

# # 14. Find frequency of each element in array.
# arr= ("apple", "cherry", "banana", "cherry", "apple")
# frequency= {}
# for i in arr:
#     if i in frequency:
#         frequency[i] +=1
#     else:
#         frequency[i] = 1
# print(frequency)

# # 12.Rotate an array by one position.
# word= (1, 2, 3, 4, 5)
# temp=[]
# for x in range(1,5):
#     temp.append(word[x])
# temp.append(word[0])
# print(temp)

# #15. Check if a string is a palindrome
# word= input("Enter a word to check if it is a palindrome=")
# rev = word[ : :-1]
# if rev == word:
#     print("Entered word is a palindrome.")
# else:
#     print("Entered word is not a palindrome.")

