# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 22:30:57 2025

@author: Usuario
"""
import time


def escribir_lento (cad, vel):
    for i in cad:
        print(i, end="", flush=True)
        time.sleep(vel)
        
presentacion = """
Hola mundo 👋

Soy Sofía
Estudiante de Ingenieria de Datos e Inteligencia Artificial en la universidad de León y 
apasionada de aprender cosas nuevas y encontrar patrones donde otros solo ven datos.

💡Mi misión: Aplicar esa curiosidad infinita y mi capacidad para encontrar patrones en
el mundo de los datos y la IA

💻 Mi stack ténico:
    - Python 🐍 (espeializado en ciencia de datos)
    - Analisis de datos: Pandas 📊, NumPy
    - Aprendizaje automatio: Scikit-learn 🤖
    - Visualización: Matplotlib 📈
    
🚀Buscando oportunidades donde mi pasión por los patrones y el aprendizaje puedan 
generar impacto real.

"""
escribir_lento(presentacion, 0.05)