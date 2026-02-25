# Customer Scoring API

## Ì≥å Descripci√≥n del Proyecto

Este proyecto consiste en el desarrollo de una API REST construida con FastAPI que permite calcular un puntaje de riesgo para clientes en funci√≥n de su edad e ingresos.

La API fue contenerizada usando Docker y probada localmente en localhost.

---

## Ìª† Tecnolog√≠as Utilizadas

- Python 3.11
- FastAPI
- Uvicorn
- Docker

---

## Ì≥Ç Estructura del Proyecto

```
api-linux/
‚îÇ
‚îú‚îÄ‚îÄ app/
‚îÇ   ‚îî‚îÄ‚îÄ main.py
‚îú‚îÄ‚îÄ requirements.txt
‚îú‚îÄ‚îÄ Dockerfile
‚îî‚îÄ‚îÄ README.md
```

---

## Ì∫Ä C√≥mo ejecutar el proyecto en local

### 1Ô∏è‚É£ Construir la imagen Docker

```bash
docker build -t api-linux .
```

### 2Ô∏è‚É£ Ejecutar el contenedor

```bash
docker run -p 8000:8000 api-linux
```

La API estar√° disponible en:

```
http://localhost:8000
```

---

## Ì¥é Endpoints Disponibles

### ‚úÖ GET /

Verifica que la API est√° funcionando.

**Ejemplo:**

```bash
curl http://localhost:8000/
```

Respuesta:

```json
{"message":"API funcionando correctamente"}
```

---

### ‚úÖ GET /health

Endpoint de verificaci√≥n de estado.

```bash
curl http://localhost:8000/health
```

Respuesta:

```json
{"status":"ok"}
```

---

### ‚úÖ POST /score

Calcula el puntaje de riesgo de un cliente.

#### Ì¥ê Requiere Header de autorizaci√≥n:

```
Authorization: Bearer supertoken123
```

#### Ì≥• Body JSON:

```json
{
  "name": "Juan",
  "age": 30,
  "income": 2000,
  "country": "Ecuador"
}
```

#### Ì≥§ Ejemplo con curl:

```bash
curl -X POST http://localhost:8000/score -H "Content-Type: application/json" -H "Authorization: Bearer supertoken123" -d '{"name":"Juan","age":30,"income":2000,"country":"Ecuador"}'
```

#### Ì≥§ Respuesta:

```json
{
  "name": "Juan",
  "score": 70,
  "risk_level": "LOW"
}
```

---

## Ì¥ê Validaciones Implementadas

- El cliente debe ser mayor de edad.
- Se requiere token de autorizaci√≥n.
- Validaci√≥n autom√°tica del modelo usando Pydantic.
- Respuestas HTTP apropiadas (400, 401).

---

## Ìºø Manejo de Ramas (Git)

Se trabaj√≥ utilizando ramas:

```bash
git checkout -b feature/scoring
git checkout main
git merge feature/scoring
```

Esto permite un flujo de trabajo organizado y profesional.

---

## Ì∞≥ Contenerizaci√≥n

El proyecto fue contenerizado utilizando Docker mediante un Dockerfile basado en Python 3.11-slim.

La aplicaci√≥n se ejecuta usando Uvicorn dentro del contenedor.

---

## Ì∑™ Pruebas Realizadas

- Pruebas con curl en terminal
- Validaci√≥n de token correcto e incorrecto
- Validaci√≥n de edad m√≠nima
- Pruebas en navegador para endpoints GET

---

## Ì≥å Conclusi√≥n

La API cumple con:

- Construcci√≥n de API REST
- Validaci√≥n de datos
- Uso de ramas Git
- Contenerizaci√≥n con Docker
- Pruebas locales en localhost
- Manejo de autenticaci√≥n b√°sica

El sistema se encuentra funcionando correctamente en entorno local.

