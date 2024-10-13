Python 3.12.5 (v3.12.5:ff3bc82f7c9, Aug  7 2024, 05:32:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Define a list of 15 numbers
... numbers = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
... 
... # Loop through each number in the list
... for number in numbers:
...     # Check if the number is even
...     if number % 2 == 0:
...         print(str(number) + " is even")  # Print message for even numbers
...     else:
...         print(str(number) + " is odd")   # Print message for odd numbers
