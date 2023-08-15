def get_middle_characters(s):
    length = len(s)

    if length % 2 == 1:  # Odd length
        middle_index = length // 2
        middle_characters = s[middle_index]
    else:  # Even length
        middle_index = length // 2 - 1
        middle_characters = s[middle_index:middle_index + 2]

    return middle_characters


input_string = "Amazon"
middle_chars = get_middle_characters(input_string)
print("Middle characters:", middle_chars)
