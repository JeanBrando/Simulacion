# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 14:35:55 2025

@author: jean_
"""

import tkinter as tk
from tkinter import simpledialog, messagebox
import random
from collections import defaultdict

def main():
    # Solicitar entrada al usuario
    cantidad_numeros = int(simpledialog.askstring("Input", "Ingrese la cantidad de números a evaluar:"))
    decimales = int(simpledialog.askstring("Input", "Ingrese el número de decimales (3, 4 o 5):"))
    
    numeros = []
    
    # Generar números aleatorios
    for _ in range(cantidad_numeros):
        numero = round(random.random(), decimales)
        numeros.append(numero)
    
    categorias = [
        "Todos diferentes (TD)",
        "Exactamente un par (1P)",
        "Dos pares (2P)",
        "Tercia y un par (TP)",
        "Tercia (T)",
        "Póker (P)",
        "Quintilla (Q)"
    ]
    
    # Generar probabilidades aleatorias y normalizarlas
    probabilidades = [random.random() for _ in range(len(categorias))]
    suma = sum(probabilidades)
    probabilidades = [p / suma for p in probabilidades]
    
    grados_libertad = len(categorias) - 1
    frecuencias = [0] * len(categorias)

    for numero in numeros:
        num_str = "{:.{prec}f}".format(numero, prec=decimales).split('.')[1]
        conteo = defaultdict(int)
        
        for c in num_str:
            conteo[c] += 1
        
        max_rep = max(conteo.values()) if conteo else 0
        pares = sum(1 for v in conteo.values() if v == 2)
        
        if max_rep == 5:
            frecuencias[6] += 1  # Quintilla
        elif max_rep == 4:
            frecuencias[5] += 1  # Póker
        elif max_rep == 3 and pares == 1:
            frecuencias[3] += 1  # Tercia y un par
        elif max_rep == 3:
            frecuencias[4] += 1  # Tercia
        elif pares == 2:
            frecuencias[2] += 1  # Dos pares
        elif pares == 1:
            frecuencias[1] += 1  # Exactamente un par
        else:
            frecuencias[0] += 1  # Todos diferentes
    
    # Construir el resultado
    resultado = "Frecuencias observadas:\n"
    for i, categoria in enumerate(categorias):
        resultado += f"{categoria}: {frecuencias[i]}\n"
    
    # Calcular chi-cuadrada
    chi_cuadrada = 0.0
    for i in range(len(categorias)):
        esperado = probabilidades[i] * cantidad_numeros
        chi_cuadrada += (frecuencias[i] - esperado) ** 2 / esperado
    
    resultado += f"\nEstadístico Chi-cuadrada: {chi_cuadrada}"
    resultado += f"\nGrados de libertad: {grados_libertad}"
    
    messagebox.showinfo("Resultados", resultado)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal de tkinter
    main()