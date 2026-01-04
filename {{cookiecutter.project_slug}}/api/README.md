# API

FastAPI application for {{ cookiecutter.project_name }}.

## Quick Start

```bash
make api
# or
uv run uvicorn api.main:app --reload
```

## Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | API info |
| `/health` | GET | Health check |
| `/docs` | GET | Swagger UI |

## Adding Endpoints

```python
@app.get("/your-endpoint")
async def your_endpoint():
    return {"message": "Hello"}
```
