# Pentru un  sir  cu n elemente care contine valori din multime {1, 2 ... n-1} a. i o singura valoare se repeta de 2 ori, sa se identifice acea valoare
#ex: pt sirul [1,2,3,4,2] valoarea 2 apare de 2 ori

n = input("n=")
n = int(n)

sir = [0] * n
for i in range(0,n):
    sir[i] = int(input())


def afisareElemDublat(n,sir):
    frecventa = []
    frecventa = [0 for i in range(n)]
    ok = 1
    i = 0
    while ok == 1 and i < n:
        frecventa[sir[i]] = frecventa[sir[i]] + 1
        if(frecventa[sir[i]] == 2):
            return sir[i]
        else:
            i = i + 1 
     
print(afisareElemDublat(n,sir))

#test
assert afisareElemDublat(4,[1,3,2,3]) == 3
assert afisareElemDublat(5,[1,2,3,4,2]) == 2



