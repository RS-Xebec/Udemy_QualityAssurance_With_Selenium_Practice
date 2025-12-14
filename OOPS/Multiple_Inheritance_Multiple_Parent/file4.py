from file3 import C

class D(C):
    def classdmethod(self):
        print("This is class d method")

obj = D()
obj.classamethod()
obj.classbmethod()
obj.classcmethod()