#!/usr/bin/python3

import sys

# Leemos línea a línea de la entrada estándar
for line in sys.stdin:  
    # Extraemos el nombre y las notas
    name, *marks = line.split()
    marks = list(map(int, marks))
    
    # Emitimos cada nota con el nombre del estudiante como clave
    for mark in marks:
        print(f'{name}\t{mark}')
