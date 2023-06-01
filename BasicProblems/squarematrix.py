#Given a square matrix, calculate the absolute difference between the sums of its principal and secondary diagonals.


def diagonalDifference(arr):
    n = len(arr)
    diagonal1 = sum(arr[i][i] for i in range(n))
    diagonal2 = sum(arr[i][n - i - 1] for i in range(n))
    return abs(diagonal1 - diagonal2)

arr = [[11, 2, 4],
       [4, 5, 6],
       [10, 8, -12]]

print(diagonalDifference(arr))
