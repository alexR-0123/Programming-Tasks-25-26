"""
TASK: 03 Queue Simulation

# Queue Simulation using OOP
Make a Queue class with:
- enqueue, dequeue, peek, size  
Simulate customers joining/leaving.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
class Queue:
    def __init__(self,maxItems):
        self.tiems = [None]*maxItems
        self.front = 0
        self.rear = -1
        self.size = 0
        self.maxSize = maxItems
        
    def enQueue(self, item):
        if self.size == maxSize:
            print("Queue is full, size =", self.size)
        else:
            self.rear(self.rear + 1)%(self.maxSize)
            self.size += 1
            self.items[self.rear] = item
           
    def deQueue(self):
        if (self.size == 0):
            return "Queue is empty"
        else:
            first = self.items[self.front]
            self.size +=1
            self.front(self.front + 1)%(self.maxSize)
            return first
        
    def peek(self):
        if self.size == 0:
            return "Queue is empty "
        else:
            return self.items[self.front]
def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    pass


if __name__ == "__main__":
    main()
