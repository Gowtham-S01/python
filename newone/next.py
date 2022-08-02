class stu:
    def __init__(self):
        self.name="Gowtham"
        self.std=11
    def update(self):
        self.std=15
    def compare(self,others):
        if self.std==others.std:
            return True
        else:
            return False
s1=stu()
s2=stu()
s2.name='pooja'
s2.update()
if s1.compare(s2):
    print("Same Std")
else:
    print("Diff Std")
print("stud 1",s1.name)
print(s1.std)
print("stud 2",s2.name)
print(s2.std)



class car:
    wheels=4
    def __init__(self):
        self.name='audi'
        self.mil=10
c1=car()
c2=car()
c2.mil=6
car.wheels=5
print(c1.name,c1.wheels,c1.mil)
print(c2.name,c2.wheels,c2.mil)