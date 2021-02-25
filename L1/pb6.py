# Puntru un sir cu n nr intregi care contine si duplicate, sa se det. elem. majoritar (care apare de mai mult de n/2 ori)
#ex. 2 este majoritar pt [2, 8, 7, 2, 2, 5, 2, 3 , 1, 2, 2]
#complexitate Theta(n)

n = input("n=")
n = int(n)

sir = [0] * n
for i in range(0,n):
    sir[i] = int(input())


def elemMajoritar(n,sir):
    frecv = []
    frecv = [0 for i in range(n)]
    maxx = 0
    elem = 0
    for el in sir:
        frecv[el] = frecv[el] + 1
        if(frecv[el] > maxx):
            maxx = frecv[el]
            elem = el
    if(maxx > n // 2 ):
        return elem

print(elemMajoritar(n,sir))

#test
assert elemMajoritar(5, [1,1,1,1,1]) == 1
assert elemMajoritar(11, [2, 8, 7, 2, 2, 5, 2, 3 , 1, 2, 2]) == 2
