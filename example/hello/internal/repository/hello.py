class HelloRepository:
    def __init__(self, name):
        self.name = name

    def get(self):
        return self.name
