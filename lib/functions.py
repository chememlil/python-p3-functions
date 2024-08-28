#!/usr/bin/env python3

# Function to greet a programmer
def greet_programmer():
    print("Hello, programmer!")

# Function to greet a specific person
def greet(name):
    print(f"Hello, {name}!")

# Function to greet with a default name
def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

# Function to add two numbers
def add(num1, num2):
    return num1 + num2

# Function to halve a number, or return None if input is not a number
def halve(number):
    if not isinstance(number, (int, float)):
        return None
    return number / 2

# Call the functions to demonstrate their functionality

# Calling greet_programmer
greet_programmer()

# Calling greet with a specific name
greet("Naureen")

# Calling greet_with_default with no arguments
greet_with_default()

# Calling greet_with_default with a specific name
greet_with_default("Sunny")

# Calling add and printing the result
sum_result = add(1, 2)
print(sum_result)

# Calling halve with a numeric argument and printing the result
result = halve(4)
print(result)

# Calling halve with a non-numeric argument and printing the result
result = halve("two")
print(result)
