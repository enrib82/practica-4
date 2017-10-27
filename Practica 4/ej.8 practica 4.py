# -*- coding: cp1252 -*-
"""Enrique Ibáñez Orero - 1º DAW - Practica 4 - Ejercicio 6 - Pràctica 4. Exercicis per resoldre amb bucle for."""

alto=input("Escriba la altura del triangulo : ")

ancho=alto

for i in range(ancho):
    print"*"*i
for i in range(alto):
    print"*"*(alto)
    alto=alto-1   
