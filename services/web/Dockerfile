#Instalacion de python3.9.1
FROM python:3.9-slim-buster

#Establece el directorio de trabajo
WORKDIR /usr/src/app

#Establece algunas variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1  
ENV PYTHONUNBUFFERED 1

# Instalacion de las dependencias
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# Copia el proyecto
COPY . /usr/src/app/

