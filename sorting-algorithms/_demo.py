'''
  Demo for all sorting algorithms, with execution timing. The underscore in the file name is to keep
  it at the top of the list in my editor.
'''

# must be at most 14,855
TEST_LIST_SIZE = 5000

from selection_sort import selection_sort
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort

SORT_FUNCTIONS = (
  ('Selection Sort', selection_sort),
  ('Bubble Sort', bubble_sort),
  ('Insertion Sort', insertion_sort)
)


from random import gauss, shuffle
def slight_shuffle(arr: list[any], orderliness: float=0.75) -> list[any]:
  ''' Returns a copy of a list that is in mostly the same order as the original. '''
  tuplify = lambda x, y: (orderliness * y + gauss(0,1), x)
  pairs = list(map(tuplify, arr, range(len(arr))))
  pairs.sort()
  return [p[1] for p in pairs]


import timeit
def get_execution_time(fn, args: tuple[any]|list[any]=()) -> float:
  start = timeit.default_timer()
  fn(*args)
  return timeit.default_timer() - start


# relative path hack
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'wordle_words.txt')

print(f'Building test data ({TEST_LIST_SIZE} items)...', end='')

# get test lists
base_list = []
with open(filename) as file:
  for i in range(min(TEST_LIST_SIZE, 14855)):
    base_list.append(file.readline())

sorted_list = base_list[:] # the file is already sorted
mostly_sorted_list = slight_shuffle(base_list)
reversed_list = base_list[::-1]
random_list = base_list[:]
shuffle(random_list)

print('done\nRunning benchmarks...\n')


for sort_fn in SORT_FUNCTIONS:
  # copy each list because all of these sort in place
  random_time = get_execution_time(sort_fn[1], [random_list[:]])
  mostly_sorted_time = get_execution_time(sort_fn[1], [mostly_sorted_list][:])
  already_sorted_time = get_execution_time(sort_fn[1], [sorted_list][:]) # best-case time
  reversed_time = get_execution_time(sort_fn[1], [reversed_list[:]]) # worst-case time

  print(f'{sort_fn[0]}:')
  print(f'Random list: {random_time:.6f} seconds')
  print(f'Mostly sorted list: {mostly_sorted_time:.6f} seconds')
  print(f'Already sorted list (best-case): {already_sorted_time:.6f} seconds')
  print(f'Reversed list (worst-case): {reversed_time:.6f} seconds')
  print('')