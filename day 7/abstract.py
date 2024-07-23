from abc import ABC, abstractmethod


class Computer(ABC):
    @abstractmethod
    def processs(self, app):
        pass

    def run(self, app):
        self.processs(app)


class Mobile(Computer):
    def processs(self, app):
        print(f"Mobile is running {app}")


class Laptop(Computer):
    def processs(self, app):
        print("Laptop is running Windows")


samsung = Mobile()

samsung.run("Google Chrome")