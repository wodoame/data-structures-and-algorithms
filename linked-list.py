# Reference: Jay Wengrow chapter 11, page 143
# A node stores some data as well as the link to another node

class Node: 
    def __init__(self, data) -> None:
        self.data = data
        self.next_node = None
        
node_1 = Node('This')
node_2 = Node('is')
node_3 = Node('a')
node_4 = Node('linked')

# Each node points to another node starting from node 1
node_1.next_node = node_2
node_2.next_node = node_3
node_3.next_node = node_4

class LinkedList:
    def __init__(self, first_node):
        self.first_node = first_node
        
    def read(self, index):
        current_index = 0
        current_node = self.first_node
        # we increment the current index until we get the desired index we ... 
        # ... want to read from then we return the data stored there
        # When we reach the end of the list the next_node=None this means ... 
        # ... that the index provided is out of bounds so we just return None
        while current_index < index:
            # pointing to the next node and incrementing index accordingly
            current_node = current_node.next_node
            current_index += 1
            if not current_node: 
                return None
        return current_node.data
    
    def search(self, data):
        current_index = 0
        current_node = self.first_node
        # We basically check every node until we find a match to the data
        # If we reach the end of the list we just return None
        while current_node:
            if current_node.data == data:
                return current_index
            
            current_node = current_node.next_node 
            current_index += 1
        return current_node 
    
    def insert(self, index, value):
        current_index = 0
        current_node = self.first_node
        # suppose this is how the nodes are linked ['once', 'upon', 'a', 'time']
        # Now I want to insert a new node with the value 'long' before the node with the value 'time'...
        # ... so that it reads 'once upon a long time' 
        # So I'm going to insert at index 3 (so that the new node is now index 3)
        # I have to iterate until I get to index 2
        # When I get there I link node at index 2 to the new node and link the new node to the node...
        # ...that was originally there
        
        while current_index < index - 1: 
            current_node = current_node.next_node
            current_index += 1
            # Case where index is not found is not handled 
            # This code is just for demonstration
        new_node = Node(value)
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node
    
    def delete(self, index): 
        current_index = 0 # [0, 1, 2, 3, 4, 5]
        if index != 0: 
            current_node = self.first_node
            while current_index < index - 1: 
                current_node = current_node.next_node
                current_index += 1
            current_node.next_node = current_node.next_node.next_node
        else: 
            self.first_node = self.first_node.next_node

    # Obtaining the size of a linked list is O(n)
    def size(self):
        size = 0
        if self.first_node:
            current_node = self.first_node
            while current_node:
                size += 1
                current_node = current_node.next_node 
            return size
        else:
            return 0
      
        
          
list_1 = LinkedList(node_1)
list_1.insert(4, 'list')

print([list_1.read(i) for i in range(list_1.size())])
print(list_1.search('linked'))
list_1.delete(0)
print([list_1.read(i) for i in range(list_1.size())])
print(list_1.size())
        