
def longest_consecutive_1s(n):
    binary_representation = bin(n)[2:]
    
    # Split the binary string by '0' to get groups of consecutive '1's
    groups_of_1s = binary_representation.split('0')
    longest_length = max(len(group) for group in groups_of_1s)

    return longest_length

number = int(input("Enter an integer to find the longest consecutive 1s in its binary representation: "))
result = longest_consecutive_1s(number)
print("The longest consecutive 1s in the binary representation of", number, "is:", result)