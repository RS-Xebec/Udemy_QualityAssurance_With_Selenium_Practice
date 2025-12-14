#Overriding Parent Class Methods...Here Class A's sub method os overrided in filee2's Class B and when we make an obj using class B, class B's method will be used .

class A:
    def sum(self,a,b):
        print(a+b)

    def sub(self,a,b):
        print(a-b)

