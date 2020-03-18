class Criterion:
    data = None

    def __init__(self, data):
        self.data = data

    def evaluate(self):
        raise Exception("Needs implementation in child class")

    def modifiers(self):
        return ""
