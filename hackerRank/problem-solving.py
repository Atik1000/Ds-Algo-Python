# def array_sum(arr, n):
#     sum = 0
#     for i in range(n):
#         sum += arr[i]
#     return sum

# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     result = array_sum(arr, n)
#     print(result)

# def compareTriplets(a, b):
#     alice = 0
#     bob = 0
#     for i in range(len(a)):
#         if a[i] > b[i]:
#             alice += 1
#         elif a[i] < b[i]:
#             bob += 1
#         else:
#             pass
#     return alice, bob


# def aVeryBigSum(ar):
#     sum = 0
#     for i in range(len(ar)):
#         sum += ar[i]
#     return sum


def diagonalDifference(arr):
    n = len(arr)
    sum1 = 0
    sum2 = 0
    for i in range(n):
        sum1 += arr[i][i]
        sum2 += arr[i][n-i-1]
    return abs(sum1-sum2)
print(diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))


