# -*- coding: cp1252 -*-
Min=int(input("Carta Menor:"))
Max=int(input("Carta Maior:"))
Primo=[2,3,5]##Lista de primos
for i in range(5, Max+1):##Gerador de numeros primos <=Max
    ward=True
    for cont in range(len(Primo)):
        if i % Primo[cont]==0:
            ward=False
            break
    if ward==True:
        Primo.append(i)
intPrimo=[]
##for i in range(Min, Max):##Checa o intervalo entre as duas cartas
##    ward=True##meu marcador de primo
##    for cont in range(len(Primo)):##Checa se o numero i é primo
##        if i % Primo[cont]==0:
##            ward=False
##            break
##    if ward==True:##Adiciona i a lista caso seja primo
##        intPrimo.append(i)
PrimeS=set(Primo)
for i in range(Min, Max+1):
    if i in PrimeS:
        intPrimo.append(i)
Soma=0
for i in range(len(intPrimo)):
    Soma=Soma+intPrimo[i]
print "Lista de Primos",Primo
print "Primos no intervalo",intPrimo
print "Soma=",Soma
