numberLargest = int(input("Enter the largest number to consider for LCM calculation: ")) 
numberSmallest = int(input("Enter the smallest number to consider for LCM calculation: ")) 

def GCD(numberLargest, numberSmallest):
    while (numberSmallest):
        numberStore = numberSmallest
        numberSmallest = numberLargest % numberSmallest
        numberLargest = numberStore
    return numberLargest

def LCM(numberLargest, numberSmallest):
    gcd = GCD(numberLargest, numberSmallest)
    numberStore = (numberLargest * numberSmallest) // gcd
    return numberStore


numberStore = LCM(numberLargest, numberSmallest)
print("The LCM is:", numberStore)
