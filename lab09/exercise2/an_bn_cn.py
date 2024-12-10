import sys

sys.path.append("..")  # Lets us import from the parent directory
# Either of the following Stack imports will work identically
from stack_python_list import Stack  # noqa: E402
# from stack_linked_list import Stack  # noqa: E402


class AnBnCn:
    def __init__(self):
        self.stack_a = Stack()
        self.stack_b = Stack()
        self.expecting_b = False  # To track if we are expecting 'b's
        self.expecting_c = False  # To track if we are expecting 'c's

    def accept(self, in_string):
        self.stack_a.clear()
        self.stack_b.clear()

        for char in in_string:
            if char == "a":
                if self.expecting_b or self.expecting_c:
                    return False  # Invalid: 'a' after 'b' or 'c'
                self.stack_a.push("a")

            elif char == "b":
                if self.expecting_c:
                    return False  # Invalid: 'b' after 'c'
                self.expecting_b = True  # Now expecting 'b's
                if self.stack_a.is_empty():
                    return False
                self.stack_a.pop()  # Match this 'b' with an 'a'
                self.stack_b.push("b")

            elif char == "c":
                self.expecting_c = True  # Now expecting 'c's
                if self.stack_b.is_empty():
                    return False
                self.stack_b.pop()  # Match this 'c' with a 'b'

            else:
                return False  # Invalid character

        # Final check: Both stacks should be empty
        return self.stack_a.is_empty() and self.stack_b.is_empty()

    def clear(self):
        """Clear the internal state of the AnBnCn instance."""
        self.stack_a.clear()  # Clear stack_a
        self.stack_b.clear()  # Clear stack_b
        self.expecting_b = False  # Reset expecting_b flag
        self.expecting_c = False  # Reset expecting_c flag
