from __future__ import annotations # for type hinting

'''
  A demo for an array-based queue.

  Note: Any class attributes or methods that start with an underscore are private.
'''

class Queue:
  _capacity: int
  _rear: int # position of the last item in the queue
  # all items in the stack - we're using a list here, but in C++ this would be an array on the heap
  # that we create in the constructor
  _items: list[any]

  def __init__(self, capacity: int) -> None:
    if capacity < 1:
      raise ValueError('Queue size must be at least 1!')
    
    self._capacity = capacity
    # "allocate" an array of the correct size - make sure you also delete this at the end!
    self._items = [None] * self._capacity

    # set the rear to the start of the array
    self._rear = 0

  def enqueue(self, item: any) -> None:
    ''' Adds an item to the rear of the queue. '''
    # crash if the queue is already full
    if self._rear >= self._capacity - 1:
      pass

  def dequeue(self) -> any:
    ''' Removes and returns the next item in the queue. '''

  def peek(self) -> any:
    ''' Returns the next item in the queue without removing it, or None if the queue is empty. '''

  def is_empty(self) -> bool:
    ''' Self-explanatory. '''

  def is_full(self) -> bool:
    ''' Self-explanatory. '''
