import os
import shutil
import variables

def organizar_directorio(ruta_directorio):
    # 1. Crear carpetas importando los nombres desde variables.py
    for carpeta in variables.carpetas_destino:
        ruta_carpeta = os.path.join(ruta_directorio, carpeta)
        if not os.path.exists(ruta_carpeta):
            os.makedirs(ruta_carpeta)
            
    # 2. Clasificar y mover archivos
    archivos = os.listdir(ruta_directorio)
    for archivo in archivos:
        ruta_origen = os.path.join(ruta_directorio, archivo)
        if os.path.isdir(ruta_origen):
            continue
            
        nombre , extension = os.path.splitext(archivo)
        extension = extension.lower()
        
        # Comparar con las tuplas definidas en variables.py
        if extension in variables.doc_types:
            destino = 'Documentos'
        elif extension in variables.img_types:
            destino = 'Imagenes'
        elif extension in variables.software_types:
            destino = 'Software'
        else:
            destino = 'Otros'
            
        ruta_destino = os.path.join(ruta_directorio, destino, archivo)
        shutil.move(ruta_origen, ruta_destino)
        print(f"Movido: {archivo} -> {destino}")