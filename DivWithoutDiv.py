def divide(our_dividend, our_divisor):
    sign = (-1 if ((our_dividend < 0) ^ (our_divisor < 0)) else 1)

    our_dividend = abs(our_dividend);
    our_divisor = abs(our_divisor);

    quotientNumber = 0
    tempNumber = 0

    for i in range(31, -1, -1):
        if (tempNumber + (our_divisor << i) <= our_dividend):
            tempNumber += our_divisor << i
            quotientNumber |= 1 << i

    if sign == -1:
        quotientNumber = -quotientNumber
    return quotientNumber

a = int(input("Enter a for a/b: "))
b = int(input("Enter b for a/b: "))
print("The result of ",a,"/",b, "is: ", divide(a, b))

