# -*- coding: cp1252 -*-
"""Enrique Ibáñez Orero - 1º DAW - Practica 4 - Ejercicio 6 - Pràctica 4. Exercicis per resoldre amb bucle for."""

ancho=int(raw_input("Dime el ancho del rectangulo "))
alto=int(raw_input("Dime la altura del rectangulo "))

for i in range(alto):
    for j in range(ancho):
        if (i==0) or (i==alto-1):
            print "*",
        else:
            if (j==0) or (j==ancho-1):
                print "*",
            else:
                print " ",
    print ""
