def roman_to_integer(roman_numeral):
    #maps Roman numeral symbols to their corresponding integer values.
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0
    #it represents the index of characters in the roman_numeral string as we iterate.
    #'len' returns the length of the roman_numeral string.
    for i in range(len(roman_numeral)):
        if roman_numeral[i] not in roman_numerals:
            raise ValueError("Invalid Roman numeral")
    #statement checks if the current character is not the last character in the roman_numeral string.
    #'-1' is to check it don't go out of bounds
    #comparing to check the values of the current and next characters.

        if i < len(roman_numeral) - 1 and roman_numerals[roman_numeral[i]] < roman_numerals[roman_numeral[i+1]]:
            # Add and subtracts the value of the current character from the result variable.
            result -= roman_numerals[roman_numeral[i]]
        else:
            result += roman_numerals[roman_numeral[i]]

    return result
result = roman_to_integer("X")
print(result)