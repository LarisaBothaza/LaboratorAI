#sa se determine al k-lea cel mai mare elemnt al unui sir de numere cu n elemnte (k<n)
#ex al 2lea cel mai mare elemnt din sir [7,4,6,3,9,1] este 7
#complexitate Theta(n)

k = input("k=")
k = int(k)

n = input("n=")
n = int(n)

sir = [0] * n
for i in range(0,n):
    sir[i] = int(input())

def afisare(k,n,sir):
    return sorted(sir, reverse=True)[k-1]

print(afisare(k,n,sir))

#test
assert afisare(2,6,[7,4,6,3,9,1]) == 7
assert afisare(3,5,[1,2,3,4,5]) == 3