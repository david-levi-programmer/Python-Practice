class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi there! My name is {self.name}.")


guy = Person("Jake")
guy.talk()
other_guy = Person("Billy")
other_guy.talk()
