def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if both strings have the same characters with the same frequency
    return sorted(str1) == sorted(str2)


# Test cases
string1 = "listen"
string2 = "silent"

# string1 = "mean"
# string2 = "men"
if are_anagrams(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
