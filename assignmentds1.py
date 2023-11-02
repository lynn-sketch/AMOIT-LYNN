# number one
# Define a class for the stack
class Stack:
    # Initialize an empty list to store the elements
    def __init__(self):
        self.items = []

    # Check if the stack is empty
    def is_empty(self):
        return len(self.items) == 0

    # Push an element to the top of the stack
    def push(self, item):
        self.items.append(item)

    # Pop an element from the top of the stack
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    # Peek at the top element of the stack
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None


class Browser:
    def __init__(self):
        self.back_stack = []
        self.forward_stack = []

    def go_forward(self):
        if self.forward_stack:
            url = self.forward_stack.pop()
            self.back_stack.append(url)
            print("Going forward...")
        else:
            print("No forward history available.")

    def go_back(self):
        if self.back_stack:
            url = self.back_stack.pop()
            self.forward_stack.append(url)
            print("Going back...")
        else:
            print("No back history available.")

    def visit_url(self, url):
        self.back_stack.append(url)
        self.forward_stack.clear()
        print("Visiting", url)


# Example usage:
browser = Browser()
browser.visit_url("facebook.com")
browser.visit_url("ucu.com")
browser.visit_url("whatsup.com")
# goes to backward page
browser.go_back()

# goes to forward page
# browser.go_forward()
