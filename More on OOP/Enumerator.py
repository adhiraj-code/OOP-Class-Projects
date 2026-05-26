class fruits:
    def __init__(self, items):
        self.items = items
    def display(self):
        for i, product in enumerate(self.items, start=1):
            print(f"{i}.{product}")

obj = fruits(["apple", "mango", "banana"])
obj.display()