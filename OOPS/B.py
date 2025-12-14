from A import parentClass
from A import AdditionSubstractionClass
class childClass(parentClass):
    def childClassMethod(self):
        print("This is child class method")


class MultiplicationClass(AdditionSubstractionClass):
    def MultiplicationMethod(self, a, b):
        print(a*b)

