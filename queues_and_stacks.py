# You want to be able to access the largest element in a stack. ↴
class Stack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]

class MaxStack(object):

    def __init__(self):
        self.stack = Stack()
        self.maxes_stack = Stack()

    def push(self, item):
        """Add a new item onto the top of our stack."""
        self.stack.push(item)

        # If the item is greater than or equal to the last item in maxes_stack,
        # it's the new max! So we'll add it to maxes_stack.
        if self.maxes_stack.peek() is None or item >= self.maxes_stack.peek():
            self.maxes_stack.push(item)

    def pop(self):
        """Remove and return the top item from our stack."""
        item = self.stack.pop()

        # If it equals the top item in maxes_stack, they must have been pushed
        # in together. So we'll pop it out of maxes_stack too.
        if item == self.maxes_stack.peek():
            self.maxes_stack.pop()

        return item

    def get_max(self):
        """The last item in maxes_stack is the max item in our stack."""
        return self.maxes_stack.peek()

"""
Implement a queue ↴ with 2 stacks.
Your queue should have an enqueue and a dequeue method and it should be "first in first out" (FIFO).
"""
class QueueTwoStacks(object):
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        if len(self.out_stack) == 0:
            return IndexError('Cannot dequeu from empty queue')

        if self.out_stack:
            return self.out_stack.pop()
        else:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
    
"""
Write a function that, given a sentence like the one above, 
along with the position of an opening parenthesis, finds the corresponding closing parenthesis.
Example: if the example string above is input with the number 10 (position of the first parenthesis), 
the output should be 79 (position of the last parenthesis).
"""
def get_closing_paren(sentence, opening_paren_index):
    open_nested_parens = 0

    for position in range(opening_paren_index+1, len(sentence)):
        char = sentence[position]

        if char == '(':
            open_nested_parens += 1

        elif char == ')':
            if open_nested_parens == 0:
                return position
            else:
                open_nested_parens -= 1

    raise Exception('No closing parantheses :(')



"""
Let's say:

'(', '{', '[' are called "openers."
')', '}', ']' are called "closers."
Write an efficient function that tells us whether or not an input string's openers and closers are properly nested.

Examples:

"{ [ ] ( ) }" should return True
"{ [ ( ] ) }" should return False
"{ [ }" should return False
"""
def is_valid(code):
    openers_to_closers = {
        '(' : ')',
        '[' : ']',
        '{' : '}'
    }

    openers = set(openers_to_closers.keys())
    closers = set(openers_to_closers.values())

    openers_stack = []
    for char in code:
        if char in openers:
            openers_stack.append(char)

        elif char in closers:
            if not openers_stack:
                return False
            else:
                last_unclosed_opener = openers_stack.pop()
                if not openers_to_closers[last_unclosed_opener] == char:
                    return False

    return openers_stack == []

