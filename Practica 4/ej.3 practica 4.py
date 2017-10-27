# -*- coding: cp1252 -*-
"""Enrique Ibáñez Orero - 1º DAW - Practica 4 - Ejercicio 3 - Pràctica 4. Exercicis per resoldre amb bucle for."""
a=int(input("Escriba un número : "))
b=int(input("Escriba un número mayor o igual que %d : " %a))

if b<a:
    print("¡Le he pedido un número entero mayor o igual que %d!: " %a)
else:
    suma=0
    for i in range(a,b+1):
        suma=suma+i
    print("La suma desde %d hasta %d es %d" %(a, b, suma))
    for i in range(a,b):
        print i, "+",
print("%d = %d" %(b, suma))
