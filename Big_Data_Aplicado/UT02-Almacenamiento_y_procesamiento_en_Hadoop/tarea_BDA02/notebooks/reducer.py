#!/usr/bin/python3
import sys

# Creamos un diccionario para almacenar las palabras y sus frecuencias
word_count = {}

# Leemos línea a línea de la entrada estándar
for line in sys.stdin:
    # Limpiamos los espacios en blanco antes y después de la línea
    line = line.strip()
    
    # Si la línea no está vacía, procesamos
    if line:
        try:
            count, word = line.split("\t")
            count = int(count)
            
            # Acumulamos la frecuencia de cada palabra
            if word in word_count:
                word_count[word] += count
            else:
                word_count[word] = count
        except ValueError:
            print(word_count)
            continue

# Convertimos las palabras y frecuencias a una lista de tuplas
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

# Imprimimos la salida en el formato esperado: lista de pares [frecuencia, palabra]
output = "["
output += ", ".join([f"[{freq}, '{word}']" for word, freq in sorted_words[:10]])
output += "]"
print(output)

