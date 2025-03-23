#Dockerfile para API Titanic

#Imagen base ligera con Python

FROM python:3.12-slim


#Establece el directorio de trabajo

WORKDIR /app

#Copia archivos necesarios al contenedor

COPY requirements.txt ./
COPY app/ ./app/
COPY models/ ./models/

#nstala dependencias

RUN pip install --no-cache-dir -r requirements.txt

#Expone el puerto de la API

EXPOSE 8000

#Comando para iniciar la aplicación con Uvicorn

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]