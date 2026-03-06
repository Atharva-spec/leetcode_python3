class MinStack: #this is a system design problem
    def __init__(self):
        self.stack = []  
        self.stackmini = [] 

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.stackmini[-1] if self.stackmini else val)
        self.stackmini.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.stackmini.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stackmini[-1]
        
#trick : we maintain two stacks, one for the actual values and another for the minimum values.                   