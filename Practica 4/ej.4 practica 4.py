# -*- coding: cp1252 -*-
"""Enrique Ibáñez Orero - 1º DAW - Practica 4 - Ejercicio 4 - Pràctica 4. Exercicis per resoldre amb bucle for."""

num=int(raw_input("Escribe un numero para sacar su factorial ==> "))
factorial=1
auxvar=num
for i in range(auxvar):
    factorial *= auxvar # Esto es igual que factorial=factorial*num
    auxvar -= 1 # Esto es igual que num=num-1

print "El factorial de %d es: %d" %(num, factorial)
