Max=int(input("Insira o numero:"))

Primo=[2,3,5]##Lista de primos
for i in range(5, Max+1):##Gerador de numeros primos <=Max
    ward=True
    for cont in range(len(Primo)):
        if i % Primo[cont]==0:
            ward=False
            break
    if ward==True:
        Primo.append(i)
PrimeS=set(Primo)
if Max in PrimeS:
    print("Numero primo!")
else:
    print("Numero composto!")
