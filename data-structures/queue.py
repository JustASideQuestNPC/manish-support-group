from __future__ import annotations # for type hinting

'''
  A demo for an array-based queue.

  Note: Any class attributes or methods that start with an underscore are private.
'''

class Queue:
  _capacity: int
  _rear: int # position of the last item in the queue
  # all items in the queue - we're using a list here, but in C++ this would be an array on the heap
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
    if self._rear >= self._capacity:
      raise ValueError('Queue is full!')
    
    # insert the item and step to the next space
    self._items[self._rear] = item
    self._rear += 1

  def dequeue(self) -> any:
    ''' Removes and returns the next item in the queue. '''
    # crash if the queue is already empty
    if self._rear <= 0:
      raise ValueError('Queue is empty!')
    
    # store the item so we can return it later
    item = self._items[0]

    # shift all the other items forward
    for i in range(self._rear):
      self._items[i] = self._items[i + 1]

    self._rear -= 1
    return item

  def peek(self) -> any:
    ''' Returns the next item in the queue without removing it, or None if the queue is empty. '''
    if self._rear <= 0:
      return None
    return self._items[self._rear]

  def is_empty(self) -> bool:
    ''' Self-explanatory. '''
    return self._rear <= 0

  def is_full(self) -> bool:
    ''' Self-explanatory. '''
    return self._rear >= self._capacity
  

queue = Queue(10)
print('created queue')
queue.enqueue(10)
print('enqueued 10')
queue.enqueue(20)
print('enqueued 20')
queue.enqueue(30)
print('enqueued 30')

print(f'peek: {queue.peek()}')
print(f'dequeue: {queue.dequeue()}')
print(f'dequeue: {queue.dequeue()}')
print(f'dequeue: {queue.dequeue()}')
