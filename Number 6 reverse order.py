def reverse_sentence(input_string):
    words = input_string.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

input_string = "Hello Good Morning"
reversed_output = reverse_sentence(input_string)
print(reversed_output)
