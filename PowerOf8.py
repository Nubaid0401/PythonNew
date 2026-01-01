def power8(number):
    if (number == 0):
        return 0
    if ((number & (~(number - 1))) == number):
        return 1
    while (number % 8 == 0):
        if (number == number // 8):
            break
        number = number // 8
    if (number == 1):
        return 1
    return 0

number = int(input("Enter a number: "))
if (power8(number)):
    print("\nThe number is power of 8")
else:
    print("\nThe number is not a power of 8")