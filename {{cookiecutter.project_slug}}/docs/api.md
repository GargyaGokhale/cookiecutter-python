# API

FastAPI REST API.

## Quick Start

```bash
make api
```

- Swagger UI: http://localhost:8000/docs
- Health check: http://localhost:8000/health

## Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | API info |
| `/health` | GET | Health check |

## Adding Endpoints

Edit `api/main.py`:

```python
@app.get("/your-endpoint")
async def your_endpoint():
    return {"message": "Hello"}
```

