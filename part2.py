'''
***PART 2***

Write a program that prompts the user to enter a number. The program then prints "Hunter" the number of times the user entered. Use a while loop.

Example of what should appear when the program runs:

Times to print: 3
Hunter
Hunter
Hunter

'''

printnum = int(input("times to print: "))
number = 0 
while number < printnum:
  number = number + 1
print("hunter " * number)