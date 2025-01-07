#!/usr/bin/python3

import sys
import re
from collections import Counter

# Inicializamos un contador para las palabras
word_count = Counter()

# Leemos línea por línea de la entrada estándar
for line in sys.stdin:
    # Convertir la línea a minúsculas y eliminar caracteres no alfabéticos
    line = re.sub(r'[^a-zA-Z\s]', '', line.lower())
    # Dividir la línea en palabras
    words = line.split()
    
    # Actualizamos el contador de palabras
    word_count.update(words)

# Después de procesar todas las líneas, emitimos la frecuencia de las palabras
for word, count in word_count.items():
    print(f'{count}\t{word}')
