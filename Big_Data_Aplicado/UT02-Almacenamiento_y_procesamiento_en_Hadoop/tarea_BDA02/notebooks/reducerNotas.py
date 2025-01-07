#!/usr/bin/python3

import sys

prev_name=''
max_mark = -1

# Leemos línea a línea de la entrada estándar
for line in sys.stdin: 
    
    name, mark = line.split()
    mark = float(mark)
    
    # Si el nombre es igual al de la anterior línea o es la primera iteración, acumulamos la suma de notas y el nḿero de notas
    if not prev_name or prev_name == name:                
        max_mark  = max(max_mark, mark)
    
    # Cuando el nombre sea diferente, emitimos el nombre anterior y la nota más alta
    else:
        print(f'"{prev_name}"\t{max_mark:.1f}')
        max_mark = mark
        
    prev_name=name
           
# Emitimos el nombre y la nota más alta del último nombre
print(f'"{prev_name}"\t{max_mark:.1f}')
