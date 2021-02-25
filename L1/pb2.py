# Sa se determine distanta Euclidiana intre doua locatii identificate prin perechi de numere
#Ex: (1,5) si (4,1) este 5.0
#complexitate Theta(1)

import math

Xa = int(input("Xa: "))
Xb = int(input("Xb: "))
Ya = int(input("Ya: "))
Yb = int(input("Yb: "))

def dist(Xa,Xb,Ya,Yb):
    return math.sqrt(pow((Xa-Xb),2)+pow((Ya-Yb),2))

print(dist(Xa,Xb,Ya,Yb))

#test:
assert dist(1,5,4,1) == 5