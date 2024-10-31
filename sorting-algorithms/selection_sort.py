'''
  A basic selection sort implementation.

  Do not run this file directly! Use demo.py instead.
'''

def selection_sort(array: list[any]) -> list[any]:
  # selection sort sorts in place
  array = array[:]

  n = len(array)
  for i in range(n - 1):
    # assume the current position holds the minimum unsorted element
    min_index = i

    # find the actual minimum element
    for j in range(i + 1, n):
      if array[j] < array[min_index]:
        min_index = j

    # swap in the actual minimum element
    array[i], array[min_index] = array[min_index], array[i]

  return array


# for debugging
# from random import shuffle
# demo_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# shuffle(demo_list)
# print(selection_sort(demo_list))