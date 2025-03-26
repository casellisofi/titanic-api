# Titanic Survival Prediction API

API desarrollada con **FastAPI** para predecir la supervivencia de pasajeros del Titanic utilizando un modelo de Machine Learning.

---

## **Estructura del Proyecto**

```
titanic-api/
│
├── app/
│   ├── core/
│   │   ├── __init__.py
│   │   └── model_loader.py    
│   ├── utils/
│   │   ├── __init__.py
│   │   └── preprocessing.py   
│   ├── __init__.py
│   ├── main.py                  
│   └── schemas.py              
├── models/
│   └── modelo_titanic.joblib  
├── tests/
│   ├── __init__.py
│   └── test_main.py 
│   └── test_model_loader.py 
│   └── test_preprocessing.py 
├── .gitignore       
├── docker-compose.yml     
├── Dockerfile  
├── README.md                      
└── requirements.txt                              
```

---

## **Instalación y Ejecución Local**

### **Clonar el repositorio:**

```bash
git clone https://github.com/casellisofi/titanic-api.git
cd titanic-api
```

### **Crear entorno virtual:**

```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
```

### **Instalar dependencias:**

```bash
pip install -r requirements.txt
```

### **Ejecutar la API con Uvicorn:**

```bash
uvicorn app.main:app --reload
```

La documentación de la API estará disponible en:

- **Swagger UI** → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc** → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## **Levantar la API con Docker**
Asegurate de que Docker esté en ejecución.

### **Construir la imagen:**

```bash
docker build -t titanic-api .
```

### **Ejecutar el contenedor:**

```bash
docker run -p 8000:8000 titanic-api
```

---

## **Levantar la API con Docker Compose**

Para simplificar la ejecución, usá Docker Compose:

### Levantar todo en un solo comando:

```bash
docker-compose up --build
```

### Parar la API:

```bash
docker-compose down
```

---

## **Probar la API con curls**

### En Linux / macOS:

```bash
curl -X POST "http://127.0.0.1:8000/predict/" \
-H "Content-Type: application/json" \
-d '{ "pclass": 3, "sex": 1, "age": 22.0, "sibsp": 1, "parch": 0, "fare": 7.25, "embarked": 0 }'
```

### En Windows:

```bash
curl -X POST "http://127.0.0.1:8000/predict/" ^
-H "Content-Type: application/json" ^
-d "{ \"pclass\": 3, \"sex\": 1, \"age\": 22.0, \"sibsp\": 1, \"parch\": 0, \"fare\": 7.25, \"embarked\": 0 }"
```
---

## **Probar la API con Postman**

1. En Postman seleccioná **POST**
2. URL:
   ```
   http://127.0.0.1:8000/predict/
   ```
4. Ejemplo de Body para pruebas:
   ```json
   {
     "pclass": 3,
     "sex": 1,
     "age": 22.0,
     "sibsp": 1,
     "parch": 0,
     "fare": 7.25,
     "embarked": 0
   }
   ```
6. Respuesta esperada:
   ```json
   {
     "survived": 0
   }
   ```

---

## **Tests Automáticos**

### Ejecutar los tests:

```bash
pytest tests/test_main.py
pytest tests/test_model_loader.py
pytest tests/test_preprocessing.py
```
