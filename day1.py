import os
DOWNLOADS = os.environ['HOME'] + '/Descargas'
print(f'Directorio: {DOWNLOADS}')
[print(file) for file in os.listdir(DOWNLOADS) if os.path.isfile(os.path.join(DOWNLOADS,file))]