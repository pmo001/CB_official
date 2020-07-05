import numpy as np

#two stacks using numpy array instead of list
class TwoStacks:
    def __init__(self, n):  # constructor
        self.size = n
        self.arr = np.zeros([n], dtype=int)
        
        self.top1 = -1 #delim LHS
        self.top2 = self.size #delim RHS

    # Method to push an element x to stack1(LHS)
    def push1(self, x):

        # There is at least one empty space for new element
        #       -1   <=     size - 2
        if self.top1 < self.top2 - 1:
        #if top1 + 1 <= top2 -1 //can take top2's empty spot
        #top1 is filled while top1+1 is empty
        #top1 marks the LHS filled delim
            self.top1 = self.top1 + 1 #0-> idx0 will be filled so move delim(top1) to the right
            self.arr[self.top1] = x   #filled
        else:
            print("Stack Overflow ")
            exit(1)

    # Method to push an element x to stack2
    def push2(self, x):

        # There is at least one empty space for new element
        # top1      <=  top2 - 2
        # top1 +1   <= top2 -1 #greater than is no good=> trespasses into delim 
        if self.top1 < self.top2 - 1:
            self.top2 = self.top2 - 1
            self.arr[self.top2] = x

        else:
            print("Stack Overflow ")
            exit(1)

    # Method to pop an element from first stack
    def pop1(self):
        if self.top1 >= 0: #not -1 ==equiv empty stack
            x = self.arr[self.top1]
            self.top1 = self.top1 - 1 #move top of stack down 
            return x
        else:
            print("Stack Underflow ")
            exit(1)

    # Method to pop an element from second stack
    def pop2(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 = self.top2 + 1
            return x
        else:
            print("Stack Underflow ")
            exit()

stack = TwoStacks(10)
stack.push1(20)
stack.push2(10)

print(stack.pop1())
stack.push1(100)
print(stack.arr)
            