#We have to convert binarty number to decimal number and take input form users
def binary_to_decimal(binary_string):
    decimal_value = 0
    # Iterate over the string from right to left (least significant bit to most significant bit)
    # enumerate(reversed(...)) gives us both the index (power) and the digit
    for index, digit in enumerate(reversed(binary_string)):
        if digit == '1':
            # Add 2 raised to the power of the current index (position)
            decimal_value += 2 ** index
    return decimal_value

binary_input = input("Enter a binary number: ")
decimal_output = binary_to_decimal(binary_input)
print(f"The decimal equivalent of binary {binary_input} is {decimal_output}.")