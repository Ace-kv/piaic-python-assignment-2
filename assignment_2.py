# 1. Add two numbers

# Write a Python program that takes two integer inputs from the user and calculates their sum. 
# The program should perform the following tasks:

# Prompt the user to enter the first number.
# Read the input and convert it to an integer.
# Prompt the user to enter the second number.
# Read the input and convert it to an integer.
# Calculate the sum of the two numbers.

# Print the total sum with an appropriate message.

print("\nProblem 1\n")

num_1: int = int(input("Enter the first number: "))
num_2: int = int(input("Enter the second number: "))

sum_of_nums: int = num_1 + num_2

print(f"Sum of {num_1} and {num_2} is:", sum_of_nums)

# 2. Agreement Boot

# Write a program which asks the user what their favorite animal is, and then always responds with 
# "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

# Here's a sample run of the program (user input is in bold italics - note the space between the prompt and the user input!):

# What's your favorite animal? cow

# My favorite animal is also cow!

print("\nProblem 2\n")

user_res: str = input("What's your favorite animal? ")

print(f"My favorite animal is also {user_res}!")

# 3. Fahrenheit to Celsius Write a program which prompts the user for a temperature in Fahrenheit 
# (this can be a number with decimal places!) and outputs the temperature converted to Celsius.

# The Celsius scale is widely used to measure temperature, but places still use Fahrenheit. 
# Fahrenheit is another unit for temperature, but the scale is different from Celsius -- 
# for example, 0 degrees Celsius is 32 degrees Fahrenheit!

# The equation you should use for converting from Fahrenheit to Celsius is the following:

# degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0

# (Note. The .0 after the 5 and 9 matters in the line above!!!)

# Here's a sample run of the program (user input is in bold italics):

# Enter temperature in Fahrenheit: 76

# Temperature: 76.0F = 24.444444444444443C

print("\nProblem 3\n")

degrees_fahrenheit: float = float(input("Enter temperature in Fahrenheit: "))
degrees_celsius: float = (degrees_fahrenheit - 32) * 5.0/9.0

print(f"Temperature: {degrees_fahrenheit}F = {degrees_celsius}C")

# 4. Triangle Perimeters Prompt the user to enter the lengths of each side of a triangle and 
# then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

# Here's a sample run of the program (user input is in bold italics):

# What is the length of side 1? 3

# What is the length of side 2? 4

# What is the length of side 3? 5.5

# The perimeter of the triangle is 12.5

print("\nProblem 4\n")

side_1: float = float(input("What is the length of side 1? "))
side_2: float = float(input("What is the length of side 2? "))
side_3: float = float(input("What is the length of side 3? "))

perimeter: float = side_1 + side_2 + side_3

print("\nThe perimeter of the triangle is", perimeter)

# 5. Square Number Ask the user for a number and print its square (the product of the number times itself).

# Here's a sample run of the program (user input is in bold italics):

# Type a number to see its square: 4

# 4.0 squared is 16.0

print("\nProblem 5\n")

num_to_square: float = float(input("Type a number to see its square: "))

print(f"{num_to_square} squared is {num_to_square ** 2}")

# 6. Delete a number Consider a list named numbers with the elements [1, 2, 3, 4, 5]. Use list method to delete the number 3?

print("\nProblem 6\n")

numbers: list[int] = [1, 2, 3, 4, 5]
numbers.remove(3)

print(numbers)

# 7. Creating a list You have two lists:

# list1 with elements [1, 2, 3]
# list2 with elements [4, 5, 6].
# Create a program using list method to add the elements of list2 to list1.

print("\nProblem 7\n")

list_1: list[int] = [1, 2, 3]
list_2: list[int] = [4, 5, 6]

list_1.extend(list_2)

print(list_1)

# 8. Pop method You have a list named items with the elements [10, 20, 30, 40]. 
# If you use the pop method without any arguments, what will the list look like and what value will be removed?

print("\nProblem 8\n")

items: list[int] = [10, 20, 30, 40]

print(f"Using pop() on items = [10, 20, 30, 40] without any arguments removes the last element i.e. {items.pop()}\n"
      f"Now items = {items}")

# 9. Index Method You have a list called colors with the elements ['red', 'blue', 'green', 'yellow']. 
# If you use the index method to find the position of 'green', what will the index be?

print("\nProblem 9\n")

colors: list[str] = ['red', 'blue', 'green', 'yellow']
index_of_green: int = colors.index('green') 

print("Using the index method to find the index of 'green' in colors = ['red', 'blue', 'green', 'yellow']\n"
      f"gives us the following result: {index_of_green}")

# 10. Get last element Fill out the function get_last_element(lst) which takes in a list lst as a parameter 
# and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.

print("\nProblem 10\n")

def get_last_element(lst: list[int | str]):
    """Takes in a non-empty list of either integer or string values and prints the last element in the list"""

    # Using try and except so that the program continues to run after the error
    try:
        if not lst:
            raise ValueError("ValueError: The list is empty, please provide a non-empty list.")
        print(f"Last item on the list = {lst} is {lst[-1]}")
    except ValueError as err:
        print(err)


get_last_element([])  # raises a value error and terminates the program file
get_last_element([1, 2, 3])

# 11. Get a List Write a program which continuously asks the user to enter values which are added one by one into a list.
# When the user presses enter without typing anything, print the list.

# Here's a sample run (user input is in blue):

# Enter a value: 1
# Enter a value: 2
# Enter a value: 3
# Enter a value:
# Here's the list: ['1', '2', '3']

print("\nProblem 11\n")

list_to_be_appended: list[str | int] = []

while(True):
   
    input_val = input("Enter a value: ")
    if not input_val: 
        print(f"Here's the list: {list_to_be_appended}")
        break
    else:
        list_to_be_appended.append(input_val)