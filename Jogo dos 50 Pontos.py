# -*- coding: cp1252 -*-
def primeGen(maxi):
    Primo=[2, 3, 5]
    for i in range(5, maxi+1):##Gerador de numeros primos <=Max
        ward=True
        for cont in range(len(Primo)):
            if i % Primo[cont]==0:
                ward=False
                break
        if ward==True:
            Primo.append(i)
    primeS=set(Primo)
    Primo=[]
    return primeS

def segCond(Plcard):
    intPrimo=[]
    Min, Max=Plcard[0], Plcard[1]
    PrimeS=primeGen(Max)
    for i in range(Min, Max+1):
        if i in PrimeS:
            intPrimo.append(i)
    Soma=0
    for i in range(len(intPrimo)):
        Soma=Soma+intPrimo[i]
    intPrimo=[]
    if Soma>=1000:
##        print intPrimo,"=",Soma,". (+2)"
        return True
    else:
##        print intPrimo,"=",Soma
        return False

def pCheck(clist):
    temp=0
    if clist[1]-clist[0] in primeGen(clist[1]):
        temp=5
##        print clist[1]-clist[0]," é primo! (+5)"
    if segCond(clist):
        temp=temp+2
    return temp

def jogForm(N):
    Pcard=[]
##    print "Jogador ",N,", 1º Numero:"
    Pcard.append(int(input()))
##    print "Jogador ",N,", 2º Numero:"
    Pcard.append(int(input()))
##    print "Jogador",N,"=",Pcard
    Pcard.sort()
    Pl=0
    if pCheck(Pcard)==0:
##        print "Nenhuma condição anterior satisfeita.(+1)"
        Pl=Pl+1
    else:
        Pl=Pl+pCheck(Pcard)
    Pcard=[]
    return Pl

Pmax=10
Pl1, Pl2=0, 0
Turno=0
while Pl1<Pmax and Pl2<Pmax:
##    print "\nTurno ",Turno
    Pl1=Pl1+jogForm(1)
    Pl2=Pl2+jogForm(2)
##    print "P1=", Pl1, "P2=", Pl2
    Turno=Turno+1
print "Numero de turnos:",Turno
print "Pontos Jogador 1:",Pl1
print "Pontos Jogador 2:",Pl2 
if Pl1>=Pmax:
    print "Jogador 1 ganhou!!! \o/"
elif Pl2>=Pmax:
    print "Jogador 2 ganhou!!! \o/"
else:
    print "Empate!!!"
    
    
    
    
    
            
        
