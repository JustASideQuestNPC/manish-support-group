from __future__ import annotations # for type hinting

'''
  A demo for a binary search tree.

  Note: Any class attributes or methods that start with an underscore are private.
'''

class Node:
  ''' A single node in the tree. '''
  key: int # the key used to find the node
  left: Node # pointer to the left node (lower key)
  right: Node # pointer to the right node (higher key)

  def __init__(self, key: int) -> None:
    self.key = key
    self.parent = None
    self.left = None
    self.right = None


class Search_Tree:
  ''' A binary search tree. '''
  _root: Node # Pointer to the first node in the tree

  def __init__(self) -> None:
    self._root = None

  
  def insert(self, key: int) -> None:
    ''' Inserts a value into the tree. '''
    # create a node to hold the data
    new_node = Node(key)

    # if the tree is empty, just make this node the root
    if self._root == None:
      self._root = new_node
    # otherwise, find where to put the node
    else:
      # start at the head, and walk down the tree
      parent_node = None
      current_node = self._root
      # walk until we hit the end of the branch
      while current_node != None:
        parent_node = current_node
        # lower keys are always on the left of a node, and higher keys are always on the right
        if new_node.key < current_node.key:
          current_node = current_node.left
        elif new_node.key > current_node.key:
          current_node = current_node.right
        # duplicate keys are not allowed
        else:
          raise KeyError(f'Key {key} already exists!')
        
      # once current_node is None, we've reached the end of the branch and can add the node to the
      # correct side of the parent
      if new_node.key < parent_node.key:
        parent_node.left = new_node
      else:
        parent_node.right = new_node

  
  def _preorder(self, node: Node) -> str:
    ''' Private method that recursively performs a preorder traversal of the tree. '''

    # do nothing if the node is none
    if node == None:
      return ''
    
    output = ''
    # add this current node's key
    output += f'[{node.key}]'
    # traverse down the left branch
    output += self._preorder(node.left)
    # once the left branch is finished, traverse the right branch
    output += self._preorder(node.right)

    return output
  
  
  def _inorder_traverse(self, node: Node) -> str:
    ''' Private method that recursively performs an inorder traversal of the tree. '''

    # do nothing if the node is none
    if node == None:
      return ''
    
    output = ''
    # continue down the left branch
    output += self._preorder(node.left)
    # once the left branch is finished, add this node's key
    output += f'[{node.key}]'
    # traverse the right branch
    output += self._preorder(node.right)

    return output
  
  def _postorder(self, node: Node) -> str:
    ''' Private method that recursively performs a postorder traversal of the tree. '''

    # do nothing if the node is none
    if node == None:
      return ''
    
    output = ''
    # continue down the left branch
    output += self._preorder(node.left)
    # once the left branch is finished, traverse the right branch
    output += self._preorder(node.right)
    # once both branches are finished, add this node's key
    output += f'[{node.key}]'

    return output
  

  def preorder_traverse(self):
    return self._preorder(self._root)

  
  def inorder_traverse(self):
    return self._inorder(self._root)

  
  def postorder_traverse(self):
    return self._postorder(self._root)


tree = Search_Tree()
tree.insert(50)
tree.insert(30)
tree.insert(60)
tree.insert(20)
tree.insert(25)

print(f'preorder: {tree.preorder_traverse()}')
print(f'preorder: {tree.preorder_traverse()}')
print(f'preorder: {tree.preorder_traverse()}')
