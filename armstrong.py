#Program to find if a number is armstrong number

#take input from the user
number = int(input("Enter a number: "))

#Calculate the number of digits
digits = len(str(number))

#initialize result variable
resultNumber = 0

#find the sum of the a^digits of each digit
temp = number
while temp > 0:
    digit = temp % 10
    resultNumber += digit ** digits
    temp //= 10

#Display the results
if number == resultNumber:
    print(number, "is an Armstrong number")

else:
    print(number, "is not an Armstrong number")