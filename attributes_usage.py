class Atrbinfo:
    name = 'tommy'
    age = '10'
    def show(self):
        print(self.name)
        print(self.age)
d1 = Atrbinfo()
print(getattr(d1,'name'))
print(hasattr(d1,'age'))
setattr(d1,'age', 15)
print(getattr(d1,'age'))