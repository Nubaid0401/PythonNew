def OddOccuring(arr):
    res = 0
    for element in arr:
        res = res^element
    return res

arr = []
n = int(input("Enter Array Size: "))

while (n):
    num = int(input("Enter Number: "))
    arr.append(num)
    n -= 1

print("Odd Occuring Element is: ", OddOccuring(arr))