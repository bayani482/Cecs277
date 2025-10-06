class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Woof!"
    
class Trainer:
    def __init__(self, dog):
        self.dog = dog

    def train(self):
        print(self.dog.name + " is training.")
        self.dog.speak()
        return f"{self.dog.name} is learning to sit."