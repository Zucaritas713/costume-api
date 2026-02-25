<<<<<<< HEAD
# Customer Scoring API

## ��� Descripción del Proyecto

Este proyecto consiste en el desarrollo de una API REST construida con FastAPI que permite calcular un puntaje de riesgo para clientes en función de su edad e ingresos.

La API fue contenerizada usando Docker y probada localmente en localhost.

---

## ��� Tecnologías Utilizadas

- Python 3.11
- FastAPI
- Uvicorn
- Docker

---

## ��� Estructura del Proyecto

```
api-linux/
│
├── app/
│   └── main.py
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## ��� Cómo ejecutar el proyecto en local

### 1️⃣ Construir la imagen Docker

```bash
docker build -t api-linux .
```

### 2️⃣ Ejecutar el contenedor

```bash
docker run -p 8080:8080 api-linux
```

La API estará disponible en:

```
http://localhost:8080
```

---

## ��� Endpoints Disponibles

### ✅ GET /

Verifica que la API está funcionando.

**Ejemplo:**

```bash
curl http://localhost:8080/
```

Respuesta:

```json
{"message":"API funcionando correctamente"}
```

---

### ✅ GET /health

Endpoint de verificación de estado.

```bash
curl http://localhost:8080/health
```

Respuesta:

```json
{"status":"ok"}
```

---

### ✅ POST /score

Calcula el puntaje de riesgo de un cliente.

#### ��� Requiere Header de autorización:

```
Authorization: Bearer supertoken123
```

#### ��� Body JSON:

```json
{
  "name": "Juan",
  "age": 30,
  "income": 2000,
  "country": "Ecuador"
}
```

#### ��� Ejemplo con curl:

```bash
curl -X POST http://localhost:8080/score -H "Content-Type: application/json" -H "Authorization: Bearer supertoken123" -d '{"name":"Juan","age":30,"income":2000,"country":"Ecuador"}'
```

#### ��� Respuesta:

```json
{
  "name": "Juan",
  "score": 70,
  "risk_level": "LOW"
}
```

---

## ��� Validaciones Implementadas

- El cliente debe ser mayor de edad.
- Se requiere token de autorización.
- Validación automática del modelo usando Pydantic.
- Respuestas HTTP apropiadas (400, 401).

---

## ��� Manejo de Ramas (Git)

Se trabajó utilizando ramas:

```bash
git checkout -b feature/scoring
git checkout main
git merge feature/scoring
```

Esto permite un flujo de trabajo organizado y profesional.

---

## ��� Contenerización

El proyecto fue contenerizado utilizando Docker mediante un Dockerfile basado en Python 3.11-slim.

La aplicación se ejecuta usando Uvicorn dentro del contenedor.

---

## ��� Pruebas Realizadas

- Pruebas con curl en terminal
- Validación de token correcto e incorrecto
- Validación de edad mínima
- Pruebas en navegador para endpoints GET

---

## ��� Conclusión

La API cumple con:

- Construcción de API REST
- Validación de datos
- Uso de ramas Git
- Contenerización con Docker
- Pruebas locales en localhost
- Manejo de autenticación básica

El sistema se encuentra funcionando correctamente en entorno local.

=======
# costume-api
>>>>>>> b80c72a8e704ed0a6e20cdf0bb0bdd85e694c33e
