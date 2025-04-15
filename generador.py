import pandas as pd
import numpy as np

# Leer archivo y obtener palabras únicas
with open('texto.txt', 'r', encoding='utf-8') as file:
    texto = file.read().lower()
    palabras = texto.split()
    palabras_unicas = sorted(list(set(palabras)))

# Inicializa matriz de transiciones en 0
matriz_transiciones = pd.DataFrame(0, index=palabras_unicas, columns=palabras_unicas)

# Recorremos las palabras y sumamos transiciones
for i in range(len(palabras) - 1):
    actual = palabras[i]
    siguiente = palabras[i + 1]
    matriz_transiciones.loc[actual, siguiente] += 1

# Mostrar matriz de transiciones
#print("Matriz de transiciones:")
#print(matriz_transiciones)

# Calcular totales horizontales
totales_horizontal = {}
for palabra in palabras_unicas:
    total = 0
    for siguiente in palabras_unicas:
        total += int(matriz_transiciones.loc[palabra, siguiente])
    totales_horizontal[palabra] = total

#print("\nTotales por palabra (origen):")
#print(totales_horizontal)

# Generar secuencia de palabras
cadena = []
actual = np.random.choice(palabras_unicas)
cadena.append(actual)
#print("\nPalabra inicial:", actual)

for i in range(50):  # Generar 10 palabras
    # Si no hay transiciones para la palabra actual
    if totales_horizontal[actual] == 0:
        nueva_palabra = np.random.choice(palabras_unicas)
        cadena.append(nueva_palabra)
        actual = nueva_palabra
        continue
    
    # Calcular probabilidades de transición
    probabilidades = []
    for palabra in palabras_unicas:
        prob = matriz_transiciones.loc[actual, palabra] / totales_horizontal[actual]
        probabilidades.append(prob)
    
    # Seleccionar siguiente palabra basada en probabilidades
    siguiente_palabra = np.random.choice(palabras_unicas, p=probabilidades)
    cadena.append(siguiente_palabra)
    actual = siguiente_palabra

print("\nSecuencia generada:")
print(" ".join(cadena))