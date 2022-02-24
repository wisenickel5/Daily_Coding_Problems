'''
Problem completed by Dylan Alexander 2/24/2022
This problem was asked by Amazon.
Implement a stack that has the following methods:
push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.
Each method should run in constant time.
'''

class Stack:
    def __init__(self, n: int) -> None:
        self.maxsize = n
        self.values = []*n

    def push(self, new_val: int) -> None:
        self.values.insert(0, new_val)

    def pop(self) -> int:
        if len(self.values) == 0:
            raise Exception("(pop) There are no elements within the stack")
        return self.values[0]

    def max_value(self) -> int:
        if len(self.values) == 0:
            raise Exception("(max_value) There are no elements within the stack")
        counter = 0
        for i in self.values:
            if i > counter:
                counter = i
        return counter

if __name__ == "__main__":
    test_stack = Stack(5)
    test_stack.push(1)
    test_stack.push(2)
    test_stack.push(3)
    test_stack.push(4)
    test_stack.push(5)
    biggest = test_stack.max_value
    print(f"Max value within the stack: {str(biggest)}")
    popped = test_stack.pop
    print(f"Popped {str(popped)} off the stack")