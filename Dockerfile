# Imagen base ligera con Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia archivos necesarios al contenedor
COPY requirements.txt .
COPY main.py .
COPY modelo_titanic.joblib .

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto de la API
EXPOSE 8000

# Comando para iniciar la aplicación con Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
