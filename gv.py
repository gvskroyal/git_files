import math as m
import calendar 

r=m.sqrt(10)
print(r)

class gvsk:
    def __init__(self) -> None:
        self.name="Venkatesh"
    print("i am parent class")
class gvsk1(gvsk):
    print("i am child class")
    def gvsk3(self):
        print(self.name)
    
gv=gvsk1()
gv.gvsk3()



