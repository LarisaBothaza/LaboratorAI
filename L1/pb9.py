#Considerandu-se o matrice cu n x m elemente intregi si o lista cu perechi formate din 
# coordonatele a 2 casute din matrice ((p,q) si (r,s)), sa se calculeze suma elem. din submatricile 
# identificate de fiecare pereche

#Ex: pt matricea
#[ [0,2,5,4,1],
#  [4,8,2,3,7],
#  [6,3,4,6,2],
#  [7,3,1,8,3],
#  [1,5,7,9,4] ]
# pt lista de perechi ((1,1) si (3,3)) => suma este 38
# pt lista de perechi ((2,2) si (4,4)) => suma este 44

def suma_submatrice(n,m,a,p,q,r,s):
    sum = 0
    for i in range(p,r+1):
        for j in range(q,s+1):
            sum = sum + a[i][j]

    return sum

#test
a = [[0,2,5,4,1],[4,8,2,3,7],[6,3,4,6,2],[7,3,1,8,3],[1,5,7,9,4]]
assert suma_submatrice(4,4,a,1,1,3,3) == 38
assert suma_submatrice(4,4,a,2,2,4,4) == 44