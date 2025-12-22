#Program to convert romal numerals to integers

def RomanToInt(romanInput):
    roman_map = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    resultInteger = 0
    for i in range(0, len(romanInput) -1):
        if roman_map[romanInput[i]] < roman_map[romanInput[i + 1]]:
            resultInteger -= roman_map[romanInput[i]]
        else:
            resultInteger += roman_map[romanInput[i]]
    resultInteger += roman_map[romanInput[-1]]
    return resultInteger
roman = input("Input roman numeral: ")
print("Integer Equivalent:", RomanToInt(roman))
print("Interger Equivalent: ", RomanToInt(roman))