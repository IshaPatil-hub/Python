# 1. Counting Positive Numbers
# Problem: Given a list of numbers, count how many are posotive.

# Numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
# positive_number_count = 0
  
# for num in Numbers:
#     if num > 0:
#         positive_number_count += 1
# print("Final count of positive number is: ", positive_number_count)


# Sum of Even Numbers
# Problem: calculate the sum of even numbers up to a given number n.

# n = 10
# sum_even  = 0

# for i in range(1, n+1):
#     if i % 2 == 0:
#         sum_even += i
    
# print("Sum of even numbers is: ", sum_even)


# 3. Multiplication Table Printer
# Problem: Print the multiplication for a given number up to 10, but skip the fifth iteration.
    

# number = 3
# for i in range(1, 11):
#     if i == 5:
#         continue    # it removes specific iteration from the loop
#     print(number, 'x', i, '=', number * i)



# 4.Reverse a string
# Problem: Reverse a string using a loop.

# input_str = "Python"
# reversed_str = ""

# for char in input_str:
#     reversed_str = char + reversed_str

# print(reversed_str)


# 5.Find the first Non-Repeated Character.
# Problem: Given a string, find the first non-repeated character.

# input_str = "teeteracdacdbi"

# for char in input_str:
#     print(char)
#     if input_str.count(char) == 1:
#         print("char is: ", char)
#         break


# 6.Factorial Calculator
# Problem: Compute the factorial of a number usinh a while loop.

# number = 5
# factorial = 1

# while number > 0:
#     factorial = factorial * number
#     number = number - 1

# print("Factorial: ,factorial")


# 7. Validate Input
# Problem: Keep asking the user for input until they enter a number between 1 and 10.

# while True:
#     number = int(input("Enter value b/w 1 and 10: "))
#     if 1 <= number <= 10:
#         print("Thanks")
#         break
#     else:
#         print("Invalid number, Try again")


# 8. Prime number checker
# Problem: Check if a number is prime.

# number = 29

# is_prime = True

# if number > 1:
#     for i in range(2, number):
#         if (number % i) == 0:
#             is_prime = False
#             break

# print(is_prime)
  


# 9. List Uniqueness Checker
# Problem: Check if all elements in a list are unique. If a dupilcate is found, exit the loop and print the duplicate.
# items = ["apple", "banana", "orange", "apple", "mango"]

items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate: ", item)
        break
    unique_item.add(item)


# 10. Exponential backoff
# Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting form 1 sec, but stops after 5 retries.

# import time

# wait_time = 1
# max_retries = 5
# attempts = 0

# while attempts < max_retries:
#     print("Attempt", attempts + 1, "-waittime", wait_time)
#     time.sleep(wait_time)
#     wait_time *= 2
#     attempts += 1