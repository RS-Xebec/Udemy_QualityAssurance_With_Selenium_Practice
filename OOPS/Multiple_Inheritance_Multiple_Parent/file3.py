from file1 import A

# from file2 import B

class C(A):
    def __init__(self):
        print("This is class c constructor")
    def classcmethod(self):
        print("This is class C method")

obj2= C()
obj2.classcmethod()     #only child class constructor will be called when there are child class constructor and parent class constructor
obj2.classamethod()

