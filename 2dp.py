#Program to check if the given number is prime or not

from math import sqrt
number = int(input("Enter a number of 2 digits: "))
print("\n")

#If given number is greater than 1
    #Check for factors from 2 to square root of the number
for number in number:
    if number < 100:
     for i in range(2, int(sqrt(number)) + 1):
        if (number % i) == 0:
            print(f"{number} is not a prime number")
            break
    else:
        print(f"{number} is a prime number")

else:
    print(f"{number} please enter a valid 2 digit number")
