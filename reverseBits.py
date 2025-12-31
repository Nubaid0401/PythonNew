
def reverse_bits(binary_str):
    decimal_output = int(binary_str, 2)
    n = decimal_output
    rev = 0
    while n > 0:
        rev = (rev << 1) | (n & 1)
        n >>= 1
    return rev

# Take binary input from user
user_input = input("Enter a binary number: ")
user_input_into_decimal = int(user_input, 2)
user_inputs = user_input, user_input_into_decimal

print(f"User Input: {user_inputs}, Reversed Bits: {reverse_bits(user_input)}")