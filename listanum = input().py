listanum = input().split()
print(listanum)
listanum = [int(num) for num in listanum]
print(listanum)
maior = 0
numcres = []
for i in range(3):
    print(i)
    menor = min(listanum)
    numcres.append(menor)
    listanum.remove(menor)
print(numcres)
