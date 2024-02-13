#Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
#a) a área do triângulo retângulo que tem A por base e C por altura.
#b) a área do círculo de raio C. (pi = 3.14159)
#c) a área do trapézio que tem A e B por bases e C por altura.
#d) a área do quadrado que tem lado B.
#e) a áre9a do retângulo que tem lados A e B.
ENTRADA = (input().split())
A = float(ENTRADA[0])
B = float(ENTRADA[1])
C = float(ENTRADA[2])
TRIANGULO = (A*C)/2
CIRCULO = 3.14159*(C*C)
TRAPEZIO = ((A+B)*C)/2
QUADRADO = B*B
RETANGULO = A*B 
print("TRIANGULO: %0.3f"%TRIANGULO)
print("CIRCULO: %0.3f"%CIRCULO)
print("TRAPEZIO: %0.3f"%TRAPEZIO)
print("QUADRADO: %0.3f"%QUADRADO)
print("RETABGULO: %0.3f"%RETANGULO)
