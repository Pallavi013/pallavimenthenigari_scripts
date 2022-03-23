class Calculation:

    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def add(self):
        print(self.a+self.b)
    
    def div(self):
        print(self.a/self.b)

c1 = Calculation(20,10)
c2= Calculation(40,20)

c1.add()
c2.div()