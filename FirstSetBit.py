#We have to write a program to check the position of the rightmost set bit of a input number.

def rightmost_set_bit_position(n):
    if n == 0:
        return 0  # No set bits in 0

    position = 1
    while (n & 1) == 0:
        n = n >> 1
        position += 1
    return position
# Example usage:
number = int(input("Enter a number: "))
position = rightmost_set_bit_position(number)
if position:
    print(f"The position of the rightmost set bit is: {position}")
else:
    print("The number has no set bits.")