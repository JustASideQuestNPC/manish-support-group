from __future__ import annotations # for type hinting

'''
  A demo for an array-based stack.

  Note: Any class attributes or methods that start with an underscore are private.
'''

class Stack:
  _capacity: int
  _top: int # position of the top item in the stack
  # all items in the stack - we're using a list here, but in C++ this would be an array on the heap
  # that we create in the constructor
  _items: list[any]

  def __init__(self, capacity: int) -> None:
    if capacity < 1:
      raise ValueError('Stack size must be at least 1!')
    
    self._capacity = capacity
    # "allocate" an array of the correct size - make sure you also delete this at the end!
    self._items = [None] * self._capacity

    # set the top to the start of the array
    self._top = 0

  def push(self, item: any) -> None:
    ''' Adds an item to the top of the stack. '''
    # crash if the stack overflows
    if self._top >= self._capacity:
      raise RuntimeError('Stack overflow!')
    
    # insert the item and step to the next open space
    self._items[self._top] = item
    self._top += 1

  def pop(self) -> any:
    ''' Removes and returns the top item on the stack. '''
    # crash if the stack underflows
    if self._top <= 0:
      raise RuntimeError('Stack underflow!')
    
    # we don't need to remove the item from the array (by setting it to None) because the only way
    # we can return that index in the array is if something was added there, which would overwrite
    # the item we just removed
    self._top -= 1
    return self._items[self._top]

  def peek(self) -> any:
    ''' Returns the top item on the stack without removing it, or None if the stack is empty. '''
    if self._top <= 0:
      return None
    return self._items[self._top - 1]

  def isEmpty(self) -> bool:
    ''' Self-explanatory. '''
    return self._top <= 0

  def isFull(self) -> bool:
    ''' Self-explanatory. '''
    return self._top <= self._capacity
  
stack = Stack(10)
print('created stack')
stack.push(10)
print('pushed 10')
stack.push(20)
print('pushed 20')
stack.push(30)
print('pushed 30')

print(f'peek: {stack.peek()}')
print(f'pop: {stack.pop()}')
print(f'pop: {stack.pop()}')
print(f'pop: {stack.pop()}')
print(f'pop (underflow): {stack.pop()}')