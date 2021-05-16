#Łukaszczyk Aleksandra 19390

import mojeklasy

print("Zadanie 4.")

def testy():
    pass

print("Zadanie 1.")
pkt1 = mojeklasy.Punkt2D(1, 2)
pkt1.drukuj()
pkt1.zeruj()
pkt1.drukuj()
print()

print("Zadanie 2.")
pkt2 = mojeklasy.Punkt3D(5, 2, 1)
pkt2.drukuj()
pkt2.zeruj()
pkt2.drukuj()
print()

print("Zadanie 3.")
dluOdc = mojeklasy.Odcinek(1, 2, 2, 5)
dluOdc.drukuj()
print()

if __name__ == "__main__":
    testy()