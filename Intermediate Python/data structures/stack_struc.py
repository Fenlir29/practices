class Node:

  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self,new_node):
        new_node.next = self.top
        self.top = new_node


    def pop(self):
        if self.top == None:
            print("no hay mas nodos")
        else :
            self.top = self.top.next


    def show_stack(self):
        current_node = self.top
        while current_node is not None:
            print(f"{current_node.data}")
            current_node = current_node.next



stack = Stack()

stack.push(Node("Primer nodo"))
stack.push(Node("Segundo nodo"))
stack.push(Node("Tercer nodo"))

print("Stack:")
stack.show_stack()

print("Después de hacer pop:")
stack.pop()
stack.show_stack()