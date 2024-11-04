listaorig= input().split(" ")
listaorig = [int(num) for num in listaorig]

listanova = []
for i in listaorig:
    listanova.append(i)

menor = 0
numcres = []

for i in range(3):#conversao de lista
    menor = min(listanova)
    numcres.append(menor)
    listanova.remove(menor)

for i in numcres: #impressao lista convertida
    print(i)
print()
for i in listaorig:#impressao de lista original
    print(i)
