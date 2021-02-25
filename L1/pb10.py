#Considerandu-se o matrice cu n x m elemnte binare (0 sau 1) swortate crescator pe linii, sa se identifice indexul liniei care contine cele mai multe elem de 1
#ex
# [ [0,0,0,1,1],
#   [0,1,1,1,1],
#   [0,0,1,1,1] ]
#a doua linie contine cele mai multe elemente de 1

def max_elems1(n,m,a):
    max = -1
    index = -1
    for l in range(0,n):
        j = 0
        while a[l][j] == 0:
            j = j + 1
        if max < m - j:     # m-j reprezinta nr de 1 de pe linie
            max  = m - j
            index = l
    return index

#test
a = [[0,0,0,1,1],[0,1,1,1,1],[0,0,1,1,1]]
assert max_elems1(3,5,a) == 1
b = [[1,1,1,1,1],[0,1,1,1,1],[0,0,1,1,1]]
assert max_elems1(3,5,b) == 0