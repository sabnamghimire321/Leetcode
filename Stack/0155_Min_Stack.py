class MinStack:

    def __init__(self):
        """
        Initializes the stack object.
        """
        self.stack = []
        self.min_stack = []
        

    def push(self, value: int) -> None:
        """
        Pushes the element value onto the stack.
        """
        self.stack.append(value)
        # If min_stack is empty, current value is the minimum.
        # Otherwise, compare value with the current minimum at the top of min_stack.
        current_min = min(value, self.min_stack[-1]) if self.min_stack else value
        self.min_stack.append(current_min)
        

    def pop(self) -> None:
        """
        Removes the element on the top of the stack.
        """
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        """
        Gets the top element of the stack.
        """
        return self.stack[-1]
        

    def getMin(self) -> int:
        """
        Retrieves the minimum element in the stack.
        """
        return self.min_stack[-1]
