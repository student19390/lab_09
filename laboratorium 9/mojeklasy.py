#Łukaszczyk Aleksandra 19390

import math

class Punkt2D():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def drukuj(self):
        print("x =", self.x, "y =", self.y)
        
    def zeruj(self):
        print("Zeruj")
        self.x = 0
        self.y = 0
        
class Punkt3D(Punkt2D):
    def __init__(self,x,y,z):
        Punkt2D.__init__(self,x,y)
        self.z=z
        
    def drukuj(self):
        print("x =", self.x,"y =", self.y,"z =", self.z)
        
    def zeruj(self):
        print("Zeruj")
        self.x=0
        self.y=0
        self.z=0
        
class Odcinek(Punkt2D):
    def __init__(self,a,b,c,d):
        self.A=Punkt2D(a,b)
        self.B=Punkt2D(c,d)
        self.odl=math.sqrt((self.B.x-self.A.x)^2+(self.B.y-self.A.y)^2)
    def drukuj(self):
        print("Wynik: ",self.odl)

def testy():
    pass

print("Zadanie 1:")
pkt1 = Punkt2D(1,2)
pkt1.drukuj()
pkt1.zeruj()
pkt1.drukuj()
print()



print("Zadanie 2:")
pkt2 = Punkt3D(5,2,1)
pkt2.drukuj()
pkt2.zeruj()
pkt2.drukuj()
print()


print("Zadanie 3:")
dluOdc = Odcinek(1,2,2,5)
dluOdc.drukuj()
print()


if __name__ == "__main__":
    testy()