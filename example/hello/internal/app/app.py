from internal.repository.hello import HelloRepository
from internal.service.hello import HelloService


class App:
    def __init__(self):
        self.repository = HelloRepository("world")
        self.service = HelloService(self.repository)

    def say(self):
        self.service.say()
