from stack import Stack


class StringProcessor:
    def __init__(self):
        self.stack = Stack()  # Initialize an empty stack

    def process_string(self, encoded_message):
        self.encoded_message = encoded_message  # Set the encoded message
        self.decoded_message = ""  # Reset the decoded message for new input
        self.stack.clear()

        for char in self.encoded_message:
            if char == "*":
                if self.stack:  # Check if the stack is not empty
                    self.decoded_message += (
                        self.stack.pop()
                    )  # Pop one character and append to result
            elif char == "^":
                if (
                    len(self.stack) >= 2
                ):  # Ensure there are at least two characters to pop
                    self.decoded_message += (
                        self.stack.pop()
                    )  # Pop first character and append
                    self.decoded_message += (
                        self.stack.pop()
                    )  # Pop second character and append
            else:
                self.stack.push(char)  # Push regular characters onto the stack
        return self.decoded_message
