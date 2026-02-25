<<<<<<< HEAD
# Customer Scoring API

## í³Œ DescripciÃ³n del Proyecto

Este proyecto consiste en el desarrollo de una API REST construida con FastAPI que permite calcular un puntaje de riesgo para clientes en funciÃ³n de su edad e ingresos.

La API fue contenerizada usando Docker y probada localmente en localhost.

---

## í»  TecnologÃ­as Utilizadas

- Python 3.11
- FastAPI
- Uvicorn
- Docker

---

## í³‚ Estructura del Proyecto

```
api-linux/
â”‚
â”œâ”€â”€ app/
â”‚   â””â”€â”€ main.py
â”œâ”€â”€ requirements.txt
â”œâ”€â”€ Dockerfile
â””â”€â”€ README.md
```

---

## íº€ CÃ³mo ejecutar el proyecto en local

### 1ï¸âƒ£ Construir la imagen Docker

```bash
docker build -t api-linux .
```

### 2ï¸âƒ£ Ejecutar el contenedor

```bash
docker run -p 8000:8000 api-linux
```

La API estarÃ¡ disponible en:

```
http://localhost:8000
```

---

## í´Ž Endpoints Disponibles

### âœ… GET /

Verifica que la API estÃ¡ funcionando.

**Ejemplo:**

```bash
curl http://localhost:8000/
```

Respuesta:

```json
{"message":"API funcionando correctamente"}
```

---

### âœ… GET /health

Endpoint de verificaciÃ³n de estado.

```bash
curl http://localhost:8000/health
```

Respuesta:

```json
{"status":"ok"}
```

---

### âœ… POST /score

Calcula el puntaje de riesgo de un cliente.

#### í´ Requiere Header de autorizaciÃ³n:

```
Authorization: Bearer supertoken123
```

#### í³¥ Body JSON:

```json
{
  "name": "Juan",
  "age": 30,
  "income": 2000,
  "country": "Ecuador"
}
```

#### í³¤ Ejemplo con curl:

```bash
curl -X POST http://localhost:8000/score -H "Content-Type: application/json" -H "Authorization: Bearer supertoken123" -d '{"name":"Juan","age":30,"income":2000,"country":"Ecuador"}'
```

#### í³¤ Respuesta:

```json
{
  "name": "Juan",
  "score": 70,
  "risk_level": "LOW"
}
```

---

## í´ Validaciones Implementadas

- El cliente debe ser mayor de edad.
- Se requiere token de autorizaciÃ³n.
- ValidaciÃ³n automÃ¡tica del modelo usando Pydantic.
- Respuestas HTTP apropiadas (400, 401).

---

## í¼¿ Manejo de Ramas (Git)

Se trabajÃ³ utilizando ramas:

```bash
git checkout -b feature/scoring
git checkout main
git merge feature/scoring
```

Esto permite un flujo de trabajo organizado y profesional.

---

## í°³ ContenerizaciÃ³n

El proyecto fue contenerizado utilizando Docker mediante un Dockerfile basado en Python 3.11-slim.

La aplicaciÃ³n se ejecuta usando Uvicorn dentro del contenedor.

---

## í·ª Pruebas Realizadas

- Pruebas con curl en terminal
- ValidaciÃ³n de token correcto e incorrecto
- ValidaciÃ³n de edad mÃ­nima
- Pruebas en navegador para endpoints GET

---

## í³Œ ConclusiÃ³n

La API cumple con:

- ConstrucciÃ³n de API REST
- ValidaciÃ³n de datos
- Uso de ramas Git
- ContenerizaciÃ³n con Docker
- Pruebas locales en localhost
- Manejo de autenticaciÃ³n bÃ¡sica

El sistema se encuentra funcionando correctamente en entorno local.

=======
# costume-api
>>>>>>> b80c72a8e704ed0a6e20cdf0bb0bdd85e694c33e
