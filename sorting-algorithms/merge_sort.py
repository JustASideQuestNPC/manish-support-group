'''
  A basic merge sort implementation.

  Do not run this file directly! Use _demo.py instead.
'''

def merge_arrays(array: list[any], start: int, middle: int, end: int) -> None:
  ''' Merges two subarrays. '''
  pass

def recursive_sort(array: list[any], start: int, end: int) -> None:
  ''' Recursively splits and sorts a subarray. '''
  # if the subarray has at least 1 element, 
  pass

def merge_sort(array: list[any]) -> None:
  ''' External interface for the algorithm. '''
  recursive_sort(array, 0, len(array) - 1)
  pass


# for debugging
from random import shuffle
demo_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(demo_list)
print(demo_list)
merge_sort(demo_list)
print(demo_list)