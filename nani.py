from math import pi
class Calculate:
    def area(self,*args):
        print('area of a circle ',pi*args[0]*args[0])
        print('area of a rectangle ',args[1]*args[2])
        print('area of a triangle ',5*args[3]*args[4])
        
        
calc=Calculate()
radius=float(input('enter radius of a circle '))
length=int(input('enter length of a rectangle '))
breadth=int(input('enter breadth of a rectangle '))
base=float(input('enter base of a rectangle '))
height=float(input('enter height of triangle '))
calc.area(radius,length,breadth,base,height)