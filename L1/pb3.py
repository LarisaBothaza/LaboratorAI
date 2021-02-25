#Produsul scalar a doi vectori rari unidimensionali. Vectorii pot avea oricate dimensiuni
#complexitate Theta(n)

vectA = [] 
vectB = [] 

n = int(input("Nr. elem A: ")) 
for i in range(0, n): 
	x = int(input("a["+str(i)+"]:")) 
	vectA.append(x) 
	
m = int(input("Nr. elem B: ")) 
for i in range(0, m): 
	x = int(input("b["+str(i)+"]:")) 
	vectB.append(x) 
	
print("A: " , vectA) 
print("B: ", vectB) 

def produs_scalar(n,vectA,m,vectB):
    produs = 0
    if n == m:
        for i in range(0, n):
            if vectA[i] != 0 and vectB[i]!=0:
                produs = produs + vectA[i]*vectB[i]
    return produs


if n == m:
    print(produs_scalar(n,vectA,m,vectB))
else:
    print("Nu se poate calcula produsul scalar, cei doi vectori nu au aceeasi dimensiune")
    
#test
a = [1,0,2,0,3]
b = [1,2,0,3,1]
assert produs_scalar(5,a,5,b) == 4
