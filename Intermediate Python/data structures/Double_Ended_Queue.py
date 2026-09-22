class Node:

  def __init__(self, data, next=None ,prev=None):
    self.data = data
    self.next = next
    self.prev = prev

class Double_ended_queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_left(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            old_head = self.head
            new_node.next = self.head
            old_head.prev = new_node
            self.head = new_node

    def push_right(self,new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            old_tail = self.tail
            new_node.prev = self.tail
            old_tail.next = new_node
            self.tail = new_node

    def pop_left(self):
        if self.head == None:
            print("no hay mas nodos")
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None


    def pop_right(self):
        if self.head == None:
            print("no hay mas nodos")
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def show_queue(self):
        current_node = self.head
        while current_node is not None:
            print(f"{current_node.data}")
            current_node = current_node.next