#define class circle 
#datamembers->radius
#methords->area(),circumference()
class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        area=(22/7)*((self.radius)**2)
        print(f"Area of the circle is {area}")
    def circumference(self):
        cir=2*(22/7)*self.radius
        print(f"The required circumference is {cir}")
x=circle(12)
x.area()
x.circumference()
#define class rectangel
#data members->legnth,bredth
#methords -> area(),peremeter()
class Rectangle:
    def __init__(self,legnth,bredth):
        self.legnth=legnth
        self.bredth=bredth
    def area(self):
        area=(self.legnth)*(self.bredth)
        print(f"The required area is {area}")
    def peremeter(self):
        print(f"The peremeter is {2*(self.legnth+self.bredth)}")
y=Rectangle(10,11)
y.area()
y.peremeter()



