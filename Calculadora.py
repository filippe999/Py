# -*- coding: cp1252 -*-
print("Calculadora - escolha operação: 1 - +, 2 - -, 3 - *, 4 - /")
op=input()
N1=int(input("N1:"))
N2=int(input("N2:"))
N3=0
if op==1:
    N3=N1+N2
elif op==2:
    N3=N1-N2
elif op==3:
    N3=N1*N2
elif op==4:
    N3=N1/N2
print("Resultado:", N3)
