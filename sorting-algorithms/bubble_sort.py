'''
  A basic bubble sort implementation.

  Do not run this file directly! Use demo.py instead.
'''

def bubble_sort(array: list[any]) -> list[any]:
  # bubble sort sorts in place
  array = array[:]
  length = len(array)

  # walk down the array and sort every element
  for i in range(length):
    swapped = False

    # we know the last i elements are already sorted
    for j in range(length - i - 1):
      # swap each element with the next one if they're in the wrong order. at the end of the
      # loop, this will have moved the maximum unsorted element into the correct place
      if array[j] > array[j + 1]:
        array[j], array[j + 1] = array[j + 1], array[j]
        swapped = True

    # if we didn't swap any elements on this loop, the array is already sorted
    if not swapped:
      break

  return array

# for debugging
# from random import shuffle
# demo_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# shuffle(demo_list)
# print(bubble_sort(demo_list))