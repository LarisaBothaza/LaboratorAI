#Sa se genereze toate nr (in reprezentare binara) curpinse intre 1 si n
#ex. n=4, nr sunt: 1,10,11,100

n = input("n= ")
n = int(n)

def transform_b10_to_b2(x):
    p = 1
    y = 0
    while x != 0:
        r = x % 2
        x = x // 2
        y = y + r * p
        p = p * 10
    return y

#test
assert transform_b10_to_b2(4) == 100
assert transform_b10_to_b2(5) == 101

def generare(n):
    nr = []
    for i in range(1,n+1):
        nr.append(transform_b10_to_b2(i))
    return nr

print(generare(n))

#test
assert generare(4) == [1, 10, 11, 100]