"""
Author: suzibo
Date: 2024/7/5
Description:NeuroMesh test1
"""


def subsequences_num(source, target):
    # initialization
    source_len, target_len = len(source), len(target)
    i, j = 0, 0
    count = 0

    while j < target_len:
        start = j

        # traverse the source
        while i < source_len and j < target_len:
            if source[i] == target[j]:
                j += 1
            i += 1

        # can not construct the target
        if start == j:
            return -1

        # record the number of subsequences
        count += 1
        i = 0

    return count


# test
print(subsequences_num("abc", "abcbc"))
print(subsequences_num("abc", "acdbc"))
print(subsequences_num("xyz", "xzyxz"))
