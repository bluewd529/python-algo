import random
from typing import List


def in_order(numbers: List[int]) -> List[int]:
    return all([numbers[i] < numbers[i+1] for i in range(len(numbers)-1)])


# def bubble_sort(numbers: List[int]) -> List[int]:
#     limit = len(numbers) - 1
#     while limit > 1:
#         for i in range(limit):
#             a = numbers[i]
#             b = numbers[i+1]
#             if a > b:
#                 numbers[i] = b
#                 numbers[i+1] = a
#         limit -= 1
#     return numbers

def bubble_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        for j in range(len_numbers - 1 - i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers


if __name__ == '__main__':
    numbers = [random.randint(0, 100) for i in range(10)]
    print(bubble_sort(numbers))
