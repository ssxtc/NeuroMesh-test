"""
Author: suzibo
Date: 2024/7/5
Description:NeuroMesh test2
"""


def brackets_check(strings):
    results = []

    for string in strings:
        pointer = [' '] * len(string)

        # record the index of left brackets
        stack = []

        for i, char in enumerate(string):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()  # brackets pairing
                else:
                    pointer[i] = '?'  # mark for additional right brackets

        # mark for additional left brackets
        for index in stack:
            pointer[index] = 'x'

        results.append(''.join(pointer))

    return results


# test
input_strings = ["bge)))))))))", "((IIII))))))", "()()()()(uuu", "))))UUUU((()"]
output_strings = brackets_check(input_strings)

for input_string, output_string in zip(input_strings, output_strings):
    print(input_string)
    print(output_string)
