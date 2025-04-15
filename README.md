# Generador de Texto Basado en Cadenas de Markov

Este proyecto implementa un generador de texto que utiliza cadenas de Markov para crear nuevas secuencias de palabras basadas en un texto de entrada. El generador analiza las probabilidades de transición entre palabras en el texto original para crear nuevas combinaciones que mantienen cierta coherencia estadística.

## Características

- Procesamiento de texto en español
- Generación de matriz de transiciones usando Pandas
- Implementación de cadenas de Markov para la generación de texto
- Manejo de casos especiales cuando no hay transiciones disponibles

## Requisitos

```python
import pandas as pd
import numpy as np
```

## Uso

1. Coloca tu texto de entrada en el archivo `texto.txt`
2. Ejecuta el script:
```bash
python generador.py
```
3. El programa generará una secuencia de 50 palabras basada en las probabilidades del texto original

## Funcionamiento

1. Lee y procesa el texto de entrada
2. Crea una matriz de transiciones entre palabras
3. Calcula las probabilidades de transición
4. Genera nuevas secuencias de texto usando las probabilidades calculadas

## Estructura del Proyecto

```
├── generador.py     # Script principal
└── texto.txt        # Texto de entrada
```
