import numpy as np
import itertools
import math


def all_ways_to_make_change(amount):
    # American currency:
    all_denominations = [0.01, 0.05, 0.25, 0.5, 1, 2, 5, 10, 20, 50, 100]
    # E.g., the maximum possible number of nickels will be amount / 0.05:
    possible_counts_for_each_denomination = [np.arange(
        int(np.ceil(amount / coin_or_note))) for coin_or_note in all_denominations]
    for config in itertools.product(*possible_counts_for_each_denomination):
        total = sum([num * val for num, val in zip(config, all_denominations)])
        # if the coins actually add up to the goal amount:
        if total == amount:
            print('solution: ')
            for num, val in zip(config, all_denominations):
                # only print when actually using this coin or note:
                if num > 0:
                    print(num, 'x', val)
            print()


class Stack:
    def __init__(self):
        self._data = []

    # push runs in O(1) under the assumptions listed:
    def push(self, item):
        # assume O(1) append (this can be guaranteed using a linked
        # list implementation):
        self._data.append(item)

    # pop runs in O(1) under the assumptions listed:
    def pop(self):
        item = self._data[-1]
        # assume O(1) list slicing (this can be guaranteed using a
        # linked list implementation):
        self._data = self._data[:-1]
        return(item)

    # push runs in worst-case O(n) where n=len(self._data);
    # however, the worst-case amortized runtime is in O(1)
    def pop_all(self):
        while self.size() > 0:
            self.pop()

    def size(self):
        return(len(self._data))

# costs r(n) = 2r(n/2) + \Theta(n) \in \Theta(n log(n))


def merge_sort(arr):
    n = len(arr)
    # any list of length 1 is already sorted:
    if n <= 1:
        return arr
    # make copies of the first and second half of the list:
    first_half = list(arr[:math.floor(n / 2)])
    second_half = list(arr[math.floor(n / 2):])
    first_half = merge_sort(first_half)
    second_half = merge_sort(second_half)
    # merge
    result = [None] * n
    i_first = 0
    i_second = 0
    i_result = 0
    while i_first < len(first_half) and i_second < len(second_half):
        if first_half[i_first] < second_half[i_second]:
            result[i_result] = first_half[i_first]
            i_first += 1
            i_result += 1
        elif first_half[i_first] > second_half[i_second]:
            result[i_result] = second_half[i_second]
            i_second += 1
            i_result += 1
        else:
            # both values are equal:
            result[i_result] = first_half[i_first]
            result[i_result + 1] = second_half[i_second]

            i_first += 1
            i_second += 1
            i_result += 1
    # insert any remaining values:
    while i_first < len(first_half):
        result[i_result] = first_half[i_first]
        i_result += 1
        i_first += 1

    while i_second < len(second_half):
        result[i_result] = second_half[i_second]
        i_result += 1
        i_second += 1

    return result


print(merge_sort([10, 1, 9, 5, 7, 8, 2, 4]))
