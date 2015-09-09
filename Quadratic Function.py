import math
print("Digite A")
A=int(input())
print("Digite B")
B=int(input())
print("Digite C")
C=int(input())
Delta=pow(B, 2)+(4*A*C)
print("Delta = ", Delta)
if(Delta>0):
    X1=(-B+math.sqrt(Delta))/2*A
    X2=(-B-math.sqrt(Delta))/2*A
    print("S = {%.2f"%X1,", %.2f"%X2,"}.")
elif(Delta<0):
    print("X incalculavel porque delta é negativo, ou seja a resposta está entre os numeros imaginarios")
else:
    X1=-(B/2*A)
    print("X = %.2f"%X1)
