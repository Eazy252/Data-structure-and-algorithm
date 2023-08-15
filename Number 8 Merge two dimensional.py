def merge_sandwiched_arrays(array1, array2):
    merged_array = []
    prev_value = float('-inf')  # Initialize with negative infinity as the previous value

    for i in range(len(array1)):
        for j in range(len(array1[i])):
            if prev_value < array1[i][j] < array2[i][j]:
                merged_array.append(array1[i][j])
                prev_value = array1[i][j]

        for j in range(len(array2[i])):
            if prev_value < array2[i][j] < array1[i][j]:
                merged_array.append(array2[i][j])
                prev_value = array2[i][j]

    return merged_array


# Example arrays
array1 = [[10, 15], [30, 50]]
array2 = [[20, 40], [5, 10]]
merged_array = merge_sandwiched_arrays(array1, array2)

print("Merged array:", merged_array)
