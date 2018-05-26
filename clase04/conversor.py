import os
import subprocess

archivos_carpeta = list(os.walk('.'))[0][2]
nombres_archivo = filter(lambda nombre: '.mp4' in nombre, archivos_carpeta)

for archivo in nombres_archivo:
    subprocess.run([
        'ffmpeg',
        '-i', archivo,
        archivo[:-1] + '3'  # ????
    ])
