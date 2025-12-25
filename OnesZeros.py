#Functions taking our number as input

def numberOfBits(n):
    ones = 0
    zeros = 0

    #While our number is greater than zero check last bit and right shift
    while(n):
        if(n&1 == 1):
            ones += 1
        else:
            zeros += 1

        n = n >> 1
        print("\n \nOnes = ",ones,"\nZeros",zeros)

number = int(input("Enter a number: "))
numberOfBits(number)