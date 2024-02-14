#Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:
MAIOR AB=(a+b+abs(a-b))/2

valor = input().split()
A = int(valor[0])
B = int(valor[1])
C = int(valor[2])
MAIOR = ((A+B)+abs(A-B))/2
RES = ((MAIOR +C)+abs(MAIOR - C))/2
print("%d eh o maior"%RES)
