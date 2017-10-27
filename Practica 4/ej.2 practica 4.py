# -*- coding: cp1252 -*-
"""Enrique Ibáñez Orero - 1º DAW - Practica 4 - Ejercicio 2 - Pràctica 4. Exercicis per resoldre amb bucle for."""
a=int(input("Escriba un número : "))
b=int(input("Escriba un número mayor o igual que %d : " %a))

if b<a:
    print("¡Le he pedido un número entero mayor o igual que %d!: " %a)
else:
    for i in range(a, b + 1):
        if i%2==0:
            print("El número %d es par" %i)
        else:
            print("El número %d es impar" %i)
