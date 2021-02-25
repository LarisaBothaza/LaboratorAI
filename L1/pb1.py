# Sa Se det. ultimul (dpdv alfabetic) cuvant care poate aparea intr-un text care contine mai multe cuvinte separate prin spatiu
#complexitate: O(n*logn)

x = input("Dati sirul: ")

def ultimul(x):
    y = x.split(" ")
    y.sort()
    return y[-1]

print(ultimul(x))

#teste:
assert ultimul("Ana mere la bal") == "mere"
assert ultimul("") == ""
assert ultimul("Ana are mere rosii si galbene") == "si"