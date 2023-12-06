from internal.repository.hello import HelloRepository


class HelloService:
    def __init__(self, repository: HelloRepository):
        self.repository = repository

    def say(self):
        name = self.repository.get()
        print(f"Hello, {name}!")
