#!/usr/bin/python3.7

"""
Objective:
    In this challenge we practice the mean, median, and mode.

Task:
    Given an array, X, of N integers, calculate and print the respective mean, median and mode on separate lines.
    If your array contains more than one modal value, choose the numerically smallest one.

Constraints:
    10 <= N <= 2500
    0 < x_i < 10^5, where x_i is the ith element of the array

Output Format:
    Print 3 lines of output in the following order:
    1. Print the mean on a new line,  to a scale on 1 decimal place (i.e., 12.3, 7.0)
    2. Print the median on a new line,  to a scale on 1 decimal place (i.e., 12.3, 7.0)
    3. Print the mode of a new line; if more than one such value exists, print the numerically smallest one.

Note:
    Since this problem is from hackerrank.com, The beginning portion of the code will contain reading the stdin method.
However, since here we do not have any stdin, we will create a generator that satisfies the constraints of the problem.
"""

# import sys
# size = sys.stdin.read()
# data = sys.stdin.read()

# class Solution:
#     def __init__(self, size=None, data=None):
#         self.size = size
#         self.data = [int(num) for num in data.split()]


from random import randint
import collections


class Generator:
    def __init__(self):
        self.size = 0
        self.data = []

    def gen_size(self):
        self.size = randint(10, 2500)

    def gen_data(self):
        for _ in range(self.size):
            self.data.append(randint(0, 1000000))


class Solution:
    def __init__(self, size=None, data=None):
        self.size = size
        self.data = data

    def mean(self):
        return round(sum(self.data) / self.size, 1)

    def median(self):
        self.data = sorted(self.data)
        lower, mid, upper = (int(round(self.size / 2, 0)) - 1,
                             int(round(self.size / 2, 0)),
                             int(round(self.size / 2, 0)) + 1)
        if not self.size % 2:
            return round(sum(self.data[lower:upper]) / 2, 0)
        else:
            return round(self.data[mid:upper][0], 0)

    def mode(self):
        data = collections.Counter(self.data)
        data_dict = dict(data)

        max_value = max(list(data.values()))
        mode_value = [num for num, freq in data_dict.items() if freq == max_value]
        if len(mode_value) == self.size:
            return min(self.data)
        else:
            return min(mode_value)

    def print_ans(self):
        print(f'Mean: {self.mean()}')
        print(f'Median: {self.median()}')
        print(f'Mode: {self.mode()}')


if __name__ is "__main__":
    generator = Generator()
    generator.gen_size()
    generator.gen_data()

    solution = Solution(generator.size, generator.data)
    solution.print_ans()
