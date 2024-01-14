#Descargar la imagen del sistema operativo con la versión de python instalada
FROM python:3.10.13-bullseye

# Define el directorio de trabajo
WORKDIR /app
# Copia el archivo de requerimiento de proyecto
COPY ./requirements.txt /var/www/requirements.txt
# Instala los módulos y las librerías del proyecto
RUN pip install -r /var/www/requirements.txt
# Copia el archivo principal de la aplicación
COPY . /app

CMD [ "python", "index.py" ]