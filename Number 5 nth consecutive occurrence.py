def find_nth_consecutive_occurrence(input_string, character, n):
    count = 0
    prev_char = ''

    for char in input_string:
        if char == character:
            if char == prev_char:
                count += 1
                if count == n:
                    return character
            else:
                count = 1
        else:
            count = 0
        prev_char = char

    return None


input_string = "Amazon is a great company as it has AtoooZzz"
character = "o"
n = 3

result = find_nth_consecutive_occurrence(input_string, character, n)

if result:
    print(f"The {n}rd consecutive occurrence of '{character}' is: {result}")
else:
    print(f"There is no {n}rd consecutive occurrence of '{character}' in the input string.")
