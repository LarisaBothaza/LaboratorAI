# Sa se determine cuvintele unui text care apar exact o singura data
#complexitate Theta(n)

text = input("Textul: ")

def aparitieUnica(text):
    list = text.split(" ")
    dic = {}   #dic = {cuvant : nrAparitii}
    for cuv in list:
        if dic.get(cuv) == None:
            dic[cuv] = 1                        #initializez cheia cuvantului cu valoarea 1
        else:
            dic[cuv] = dic.get(cuv) + 1         #cresc frecventa aparitiilor
            
    afisare = ""
    for x in dic.keys():
        if dic.get(x) == 1:
            afisare = afisare + x + " " 
    return afisare

print(aparitieUnica(text))

#test 
assert aparitieUnica("Ana are mere") == "Ana are mere "
assert aparitieUnica("Larisa Larisa pisica caine") == "pisica caine "
