'''
  A basic insertion sort implementation.

  Do not run this file directly! Use _demo.py instead.
'''

def insertion_sort(array: list[any]) -> None:
  length = len(array)

  # assume the first element is sorted and start at index 1
  for i in range(1, length):
    insert_index = i
    current_value = array[i]
    # loop backward from i to the start of the array and find where to insert the value
    for j in range(i - 1, -1, -1):
      if array[j] > current_value:
        array[j + 1] = array[j] # shift everything up to make space for the inserted value
        insert_index = j
      else:
        break
    array[insert_index] = current_value


# for debugging
# from random import shuffle
# demo_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# shuffle(demo_list)
# print(demo_list)
# insertion_sort(demo_list)
# print(demo_list)
