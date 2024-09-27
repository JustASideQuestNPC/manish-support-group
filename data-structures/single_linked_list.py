from __future__ import annotations # for type

'''
  A demo for a singly-linked list. By the end of the semester you'll probably be able to write one
  of these in your sleep, because Manish spends 6 ******* weeks on lists and pretends that none
  of the other data structures exist. I don't know why he does this, but I suspect that it's
  because Manish has no idea how to write any other data structures.

  Note: Any class attributes or methods that start with an underscore are private.
'''

class Node:
  ''' A single node in the list. '''
  data: any
  next_node: Node # points to the node after this one

  def __init__(self, data: any) -> None:
    self.data = data
    self.next_node = None


class Single_Linked_List:
  ''' A singly-linked list made up of a chain of nodes. '''
  _head: Node # points to the first node in the chain
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

    # make the new node point to the current head if it exists
    if self._size > 0:
      new_node.next_node = self._head
    # make ourselves point to the new head
    self._head = new_node

    self._size += 1

  
  def pop_front(self) -> any:
    ''' Removes and returns the first item in the list '''
    # crash and burn if the list is empty
    if self._size == 0:
      raise RuntimeError('Cannot pop from an empty list!')

    # store the existing data so we can return it later
    data = self._head.data

    # remove the first node by making ourselves point directly to the second node (if it exists)
    # if this were C++ we'd need to manually delete the first node to prevent a memory leak, but
    # in Python we can just throw it away and it'll get deleted for us
    if self._size == 1:
      self._head = None
    else:
      self._head = self._head.next_node

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
    else:
      # create a new node to hold the data
      new_node = Node(data)

      # start at the head, then walk down the list until we hit the node before the index
      prev_node = self._head
      for _ in range(index - 1):
        prev_node = prev_node.next_node

      # if this is the last node, just make the current node point to the new node
      if prev_node.next_node == None:
        prev_node.next_node = new_node
      # otherwise, make the new node point to the node after the current one, then make the current
      # node point to the new node
      else:
        new_node.next_node = prev_node.next_node
        prev_node.next_node = new_node

      self._size += 1

  
  def remove_at(self, index: int) -> any:
    ''' Removes and returns the item at an index in the list. '''
    # crash and burn if the index is out of range
    if index < 0 or index >= self._size:
      raise IndexError(f'The index {index} is out of range!')

    # if we're removing the first item, just use pop_front
    if index == 0:
      return self.pop_front()
    else:
      # start at the head, then walk down the list until we hit the node before the index
      prev_node = self._head
      for _ in range(index - 1):
        prev_node = prev_node.next_node

      removed_node = prev_node.next_node

      # store the node's data so we can return it later
      data = removed_node.data

      # if we're removing the last node, we can just make the current node point nowhere
      if removed_node.next_node == None:
        # if this were C++, we'd delete the removed node here
        prev_node.next_node = None
      # otherwise, make the current node point to the node after the node we're removing
      else:
        prev_node.next_node = removed_node.next_node
        # if this were C++, we'd delete the removed node here

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
    
    # start at the first node in the chain, then step forward until we reach the index
    current_node = self._head
    for _ in range(index):
      current_node = current_node.next_node

    return current_node.data
  

  def __setitem__(self, index: int, data: any) -> None:
    ''' Overload for the [] operator (when writing). '''
    # crash and burn if the index is out of range
    if index < 0 or index >= self._size:
      raise IndexError(f'The index {index} is out of range!')
    
    # start at the first node in the chain, then step forward until we reach the index
    current_node = self._head
    for _ in range(index):
      current_node = current_node.next_node

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
test_list = Single_Linked_List()
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
