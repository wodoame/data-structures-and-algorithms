# A node stores some data as well as the link to another node

class Node: 
    def __init__(self, data) -> None:
        self.data = data
        self.next_node = None
        
node_1 = Node('once')
node_2 = Node('upon')
node_3 = Node('a')
node_4 = Node('time')

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
          
            
        
list_1 = LinkedList(node_1)
print(list_1.search('once'))


        