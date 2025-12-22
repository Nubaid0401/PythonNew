def SieveOfEratosthenes(num):
    prime = [True for _ in range(num + 1)]

    p = 2
    while (p * p <= num):
        if (prime[p] == True):
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1

    for i in range(2, num):
        if prime[p]:
            print(p)

num = int(input("Enter a number: "))
print("Following are the prime numbers smaller than or equal to", num)
SieveOfEratosthenes(num)