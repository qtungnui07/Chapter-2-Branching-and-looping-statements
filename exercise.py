# # Exercise 1: Write a program that asks the user to enter an integer and
# # prints whether the number is positive, negative, or zero.

# print("1. ")
# n = int(input())
# if n == 0:
#     print("zero")
# elif n > 0:
#     print("positive")
# else:
#     print("negative")

# # Exercise 2: Write a program that prints all numbers from 1 to 10, each on a
# # new line.
# print()
# print("2. ")
# for i in range(1, 11):
#     print(i)

# # Exercise 3: Ask the user to input a positive integer n, then calculate and
# # print the sum of all numbers from 1 to n.
# print()
# print("3. ")
# n = int(input())
# sum = 0
# for i in range(1, n + 1):
#     sum += i
# print(sum)

# # Exercise 4: Ask the user to enter an integer and determine whether it is
# # even or odd.
# print()
# print("4. ")
# n = int(input())
# if n % 2 == 0:
#     print("even")
# else:
#     print("odd")

# # Exercise 5: Write a program that prints all even numbers from 2 to 20. 
# print()
# print("5. ")
# for i in range(2, 21, 2):
#     print(i)

# # Assignment
# # Exercise 6: Ask the user to enter a positive integer and count how many
# # digits the number has.
# print()
# print("6. ")
# n=int(input())
# count=0
# while n>0:
#     n=n//10
#     count+=1
# print(count)

# # Exercise 7: Ask the user to input a number n and calculate n! (factorial of n)
# # using a loop.

# print()
# print("7. ")
# n=int(input())
# i=1
# fact=1
# while i<=n:
#     fact*=i
#     i+=1
# print(fact)

# # Exercise 8: Ask the user to input a number between 1 and 9, then display its
# # multiplication table from 1 to 9

# print()
# print("8. ")
# n=int(input())
# if n<=0 or n>9:
#     print("Invalid input")
# else:
#     for j in range(1, 11):
#         print(f"{n} x {j} = {n*j}")
#     print()

# # Exercise 9: Write a program that prints numbers from 1 to 100, skipping
# # those that are divisible by 3.
# print()
# print("9. ")
# for i in range(1,101):
#     if i % 3 !=0:
#         print(i)


# # Exercise 10: Find and print the first integer greater than 100 that is divisible
# # by 7. #cau nay nen input thi ok hon hoac la neu k can input (tu dong tim so chia het cho 7 sau 100 thi
# #  n = 101
# # while True:
# #     if n % 7 == 0:
# #         print(n)
# #         break
# #     n += 1)


# print()
# print("10. ")
# n = int(input())
# if n <= 100:
#     print("Put greater than 100")
# else:
#     if n % 7 == 0:
#         print(f"{n} divisible by 7")
#     else:
#         print(f"{n} can't divisible by 7")


# # Exercise 11: Ask the user to enter a positive number and check whether it is
# # a prime number.

# print()
# print("11. ")
# n=int(input())
# flag = False
# if n < 0:
#     print("enter a positive number")
# elif n == 0 or n == 1:
#     print("is not a prime number")
# elif n > 1:
#     for i in range(2,n):
#         if n % i == 0:
#             flag = True
#             break
#     if flag:
#         print(f"{n} is not a prime number")
#     else:
#         print(f"{n} is a prime number")

# Exercise 12: Ask the user to enter a number n, then print the first n numbers
# in the Fibonacci sequence.
# print()
# print("12. ")
# n=int(input())
# a, b=0,1
# for _ in range(n):
#     print(a, end=" ")
#     a, b = b, a+b
# print()

# # Exercise 13: Ask the user to enter a number and compute the sum of all its
# # digits.
# n=int(input())
# sum =0 
# while n !=0:
#     last_digit=n%10
#     sum +=last_digit
#     n//=10
# print(sum)
    


# # Exercise 14: Ask the user to input a string and a character, then count how
# # many times the character appears in the string.
# s=input()
# c=input("chon chu cai bat ky")
# t=0
# for i in s:
#     if i == c:
#         t+=1
# print(t)
    

# # Exercise 15: Write a recursive function to compute the factorial of a number
# # entered by the user.

# # n = int(input())
# # res = 1
# # if n == 0 or n == 1:
# #     res = 1
# # else:
# #     for i in range(2, n + 1):
# #         res = res * i
# # print(res)
# # 
# n=int(input())

# def fac(x):
#     res = 1
#     if x == 0 or x == 1:
#         return 1
#     else:
#         for i in range(2, x+1):
#             res = res * i
#         return res
# print(fac(n))


# # Exercise 16: Ask the user to enter two positive integers and compute their
# # greatest common divisor (GCD) using a loop.

# a,b=map(int,input().split())
# while b!=0:
#     a,b=b,a%b
# print(a)


# # Exercise 17: Write a program to print all perfect numbers between 1 and
# # 1000. A perfect number equals the sum of its proper divisors.
# # 
# # 
# # 
# # ap dung tu bai 13
# # # Exercise 13: Ask the user to enter a number and compute the sum of all its
# # # digits.
# # n=int(input())
# # sum =0 
# # while n !=0:
# #     last_digit=n%10
# #     sum +=last_digit
# #     n//=10
# # print(sum)

# x=int(input())
# def perfetch_number(n):
#     if n <1 or n>1000:
#         print("Invaild Number, try again")
#     else:
#         sum = 0
#         for i in range (1,n):
#             if n%i==0:
#                 sum+=i
#         return sum == n
# print("true" if perfetch_number(x) else "false")
        
# Exercise 18: Ask the user to input a positive number and reverse its digits
# (e.g., input 1234 → output 4321).


# Exercise 19: Ask the user to enter a positive integer and find the largest
# digit in that number.
# Exercise 20: Write a recursive function to compute the sum of all integers
# from 1 to n, where n is input by the user
