import subprocess

# Cambia el nombre del archivo por el que quieres convertir
file_ipynb = "Tarea para BDA02.ipynb"

# Convierte a HTML
subprocess.run(["jupyter", "nbconvert", file_ipynb, "--to", "html"])
print(f"Archivo convertido: {file_ipynb[:-5]}-new.html")
