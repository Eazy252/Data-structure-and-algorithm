def getSmallestIntegerPosition(A):
    left, right = 0, len(A) - 1

    while left < right:
        mid = left + (right - left) // 2

        if A[mid] > A[right]:
            left = mid + 1
        else:
            right = mid

    return left


# Test cases
test_cases = [
    [3, 4, 5, 1, 2],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5],
    [9],
    [5, 1],
    [100, 90, 80, 55, 9],
    [20, 21, 25, 27, 30, 1, 5, 7, 10, 15],
    [-10, -5, -3, -1, -2],
    [5, 5, 5, 1, 5],
    [],
    [4, 4, 4, 4, 4, 4]
]

for arr in test_cases:
    position = getSmallestIntegerPosition(arr)
    print(f"Input: {arr}, Smallest Integer Position: {position}")
