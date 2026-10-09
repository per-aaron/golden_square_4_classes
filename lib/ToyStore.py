class ToyStore():
    def __init__(self):
        self.toys = []

    def add(self, toy):
        if type(toy) != str:
            raise TypeError("'toy' must be a string")
        self.toys.append(toy)

    def see_toys(self):
        return self.toys