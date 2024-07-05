"""
Author: suzibo
Date: 2024/7/5
Description: NeuroMesh test3
"""


import statistics


# calculate the average value of subsequence
def mean(subset):
    return sum(subset) / len(subset)


# calculate the val of subsequences
def val(S):
    return mean(S) - statistics.median(S)


# traversal of all subsequence and calculate each val by bit manipulation
def maximum_subsequence(n, S):
    maximum = float('-inf')
    for i in range(1, 1 << n):
        subset = [S[j] for j in range(n) if (i & (1 << j))]
        if subset:
            maximum = max(maximum, val(subset))
    return maximum


# test
n = 4
S = [1, 3, 5, 9]
result = maximum_subsequence(n,S)
print(result)