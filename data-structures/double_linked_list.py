from __future__ import annotations # for type

'''
  A demo for a doubly-linked list. By the end of the semester you'll probably be able to write one
  of these in your sleep, because Manish spends 6 ******* weeks on lists and pretends that none
  of the other data structures exist. I don't know why he does this, but I suspect that it's
  because Manish has no idea how to write any other data structures.

  Note: Any class attributes or methods that start with an underscore are private.
'''

class Node:
  ''' A single node in the list. '''
  data: any
  next_node: Node # points to the node after this one
  prev_node: Node # points to the node before this one

  def __init__(self, data: any) -> None:
    self.data = data
    self.next_node = None
    self.prev_node = None


class Double_Linked_List:
  ''' A doubly-linked list made up of a chain of nodes. '''
  _head: Node # points to the first node in the chain
  _tail: Node # points to the last node in the chain
  _size: int  # the number of nodes in the list

  def __init__(self) -> None:
    self._head = None
    self._size = 0


  def size(self) -> int:
    ''' Self-explanatory. '''
    return self._size


  def push_front(self, data: any) -> None:
    ''' Adds an item to the front of the list. '''
    # create a node to hold the data
    new_node = Node(data)

    # if the list was empty, make both our head and our tail point to it
    if self._size == 0:
      self._head = new_node
      self._tail = new_node
    # otherwise, make the new node point to the old head and make our head point to the new node
    else:
      new_node.next_node = self._head
      self._head.prev_node = new_node
      self._head = new_node

    self._size += 1

  
  def pop_front(self) -> any:
    ''' Removes and returns the first item in the list '''
    # crash and burn if the list is empty
    if self._size == 0:
      raise RuntimeError('Cannot pop from an empty list!')

    # store the existing data so we can return it later
    data = self._head.data

    # if there's one node in the list, both our head and our tail will point to it, so we need to
    # make both of them point nowhere
    if self._size == 1:
      # if this were C++ we'd need to manually delete the old head to prevent a memory leak, but
      # in Python we can just throw it away and it'll get deleted for us
      self._head = None
      self._tail = None
    # otherwise, we remove the new head's pointer to the old node and update our head
    else:
      self._head = self._head.next_node
      self._head.prev_node = None

    self._size -= 1
    return data
  
  
  def push_back(self, data) -> None:
    ''' Adds an item to the end of the list. '''
    # create a node to hold the data
    new_node = Node(data)

    # if the list was empty, make both our head and our tail point to it
    if self._size == 0:
      self._head = new_node
      self._tail = new_node
    # otherwise, make the new node point to the old tail and make our tail point to the new node
    else:
      new_node.prev_node = self._tail
      self._tail.next_node = new_node
      self._tail = new_node

    self._size += 1


  def pop_back(self) -> any:
    ''' Removes and returns the last item in the list. '''
    # crash and burn if the list is empty
    if self._size == 0:
      raise RuntimeError('Cannot pop from an empty list!')

    # store the existing data so we can return it later
    data = self._tail.data

    # if there's one node in the list, both our head and our tail will point to it, so we need to
    # make both of them point nowhere
    if self._size == 1:
      # if this were C++ we'd need to manually delete the old head to prevent a memory leak, but
      # in Python we can just throw it away and it'll get deleted for us
      self._head = None
      self._tail = None
    # otherwise, we remove the new tail's pointer to the old node and update our tail
    else:
      self._tail = self._tail.prev_node
      self._tail.next_node = None

    self._size -= 1
    return data

  
  def insert_at(self, data: any, index: int) -> None:
    ''' Adds an item at an index in the list. '''
    # crash and burn if the index is out of range
    if index < 0 or index >= self._size:
      raise IndexError(f'The index {index} is out of range!')
    
    # if we're inserting at the first index, just use push_front
    if index == 0:
      self.push_front(data)
    # if we're inserting at the last index, just use push_back
    elif index == self._size:
      self.push_back(data)
    else:

      # create a new node to hold the data
      new_node = Node(data)

      # walk to the node before the index from whichever end is closer
      prev_node = None
      if index <= int(self._size / 2):
        # walk forward from the head
        prev_node = self._head
        for _ in range(index - 1):
          prev_node = prev_node.next_node
      else:
        # walk backward from the tail
        prev_node = self._tail
        for _ in range(index):
          prev_node = prev_node.prev_node

      # update everyone's pointers to splice in the new node
      next_node = prev_node.next_node

      new_node.next_node = next_node
      new_node.prev_node = prev_node

      next_node.prev_node = new_node
      prev_node.next_node = new_node

      self._size += 1

  
  def remove_at(self, index: int) -> any:
    ''' Removes and returns the item at an index in the list. '''
    # crash and burn if the index is out of range
    if index < 0 or index >= self._size:
      raise IndexError(f'The index {index} is out of range!')
    
    # if we're removing the first index, just use pop_front
    if index == 0:
      return self.pop_front()
    # if we're removing the last index, just use pop_back
    elif index == self._size - 1:
      return self.pop_back()
    else:
      # walk to the node before the index from whichever end is closer
      removed_node = None
      if index <= int(self._size / 2):
        # walk forward from the head
        removed_node = self._head
        for _ in range(index):
          removed_node = removed_node.next_node
      else:
        # walk backward from the tail
        removed_node = self._tail
        for _ in range(index - 1):
          removed_node = removed_node.prev_node

      # store the data so we can remove it later
      data = removed_node.data

      # update everyone's pointers to splice around the removed node
      # if this were C++, we'd also delete removed_node here
      prev_node = removed_node.prev_node
      next_node = removed_node.next_node

      prev_node.next_node = next_node
      next_node.prev_node = prev_node

      self._size -= 1
      return data


  def find(self, data: any) -> int:
    ''' Returns the index of an item, or -1 if the list does not contain that item. '''
    # start at the head, then walk down the list until we either hit the data or run out of nodes
    index = 0
    current_node = self._head
    while current_node != None:
      if current_node.data == data:
        return index # stop as soon as we find the data
      
      current_node = current_node.next_node
      index += 1

    # return -1 if we run out of nodes and haven't found the data
    return -1


  def __getitem__(self, index: int) -> any:
    ''' Overload for the [] operator (when reading). '''
    # crash and burn if the index is out of range
    if index < 0 or index >= self._size:
      raise IndexError(f'The index {index} is out of range!')
    
    # walk to the node at the index from whichever end is closer
    current_node = None
    if index <= int(self._size / 2):
      # walk forward from the head
      current_node = self._head
      for _ in range(index):
        current_node = current_node.next_node
    else:
      # walk backward from the tail
      current_node = self._tail
      for _ in range(index):
        current_node = current_node.prev_node

    return current_node.data
  

  def __setitem__(self, index: int, data: any) -> None:
    ''' Overload for the [] operator (when writing). '''
    # crash and burn if the index is out of range
    if index < 0 or index >= self._size:
      raise IndexError(f'The index {index} is out of range!')
    
    # walk to the node at the index from whichever end is closer
    current_node = None
    if index <= int(self._size / 2):
      # walk forward from the head
      current_node = self._head
      for _ in range(index):
        current_node = current_node.next_node
    else:
      # walk backward from the tail
      current_node = self._tail
      for _ in range(index):
        current_node = current_node.prev_node

    current_node.data = data

  
  def __repr__(self) -> str:
    ''' Python-specific method to print out the list. '''
    output = '['
    current_node = self._head
    while current_node != None:
      output += f'{current_node.data}'
      if current_node.next_node != None:
        output += ', '
      current_node = current_node.next_node
    output += ']'
    return output
  

''' Test Code '''
test_list = Double_Linked_List()
print(f'Current list: {test_list}\n')

test_list.push_front('stinks')
print("test_list.push_front('stinks')")
print(f'Current list: {test_list}\n')

test_list.push_front('manish')
print("test_list.push_front('manish')")
print(f'Current list: {test_list}\n')

test_list.insert_at('really', 1)
print("test_list.insert_at('really', 1)")
print(f'Current list: {test_list}\n')

print(f'test_list[1]: {test_list[1]}')
print(f"test_list.find('really'): {test_list.find('really')}\n")

test_list[1] = 'really_really'
print("test_list[1] = 'really_really'")
print(f'Current list: {test_list}\n')

print(f'test_list.remove_at(1): {test_list.remove_at(1)}')
print(f'Current list: {test_list}\n')

print(f'test_list.pop_front(): {test_list.pop_front()}')
print(f'Current list: {test_list}\n')


test_list.push_back('badly')
print("test_list.push_back('badly')")
print(f'Current list: {test_list}\n')

print(f'test_list.pop_back(): {test_list.pop_back()}')
print(f'Current list: {test_list}\n')
