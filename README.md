Crop Intelligence API

Async FastAPI API for plant disease classification and pest detection.

The plant disease API uses `eymenslimani/plant-disease-detector`. The pest detection API uses `underdogquality/yolo11s-pest-detection`.

## Run

```bash
uv run uvicorn src.main:app --reload
```

The first startup downloads both model files from Hugging Face and loads them once during application startup.

## Plant Disease Prediction

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/plant-diseases/predictions" \
  -F "file=@leaf.jpg"
```

Example response:

```json
{
  "predictions": [
    {
      "label": "Tomato_leaf_mosaic_virus",
      "confidence": 0.2285
    }
  ]
}
```

## Pest Detection

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/pests/predictions" \
  -F "file=@pest.jpg"
```

Example response:

```json
{
  "predictions": [
    {
      "label": "rice leaf roller",
      "confidence": 0.536,
      "risk_flag": "شديد الخطورة",
      "message": "يرقات تتغذى على أوراق الأرز وتلفّها، وقد تسبب فقدًا واضحًا في المسطح الورقي عند الإصابة العالية؛ أهميتها ترتفع في مناطق زراعة الأرز."
    }
  ]
}
```

`message` is returned only when `risk_flag` is `شديد الخطورة`. Other known risk levels return `message: null`.

## Health Check

```bash
curl "http://127.0.0.1:8000/health"
```

## Configuration

Runtime configuration is loaded from `src/.env`. See `src/.env.example` for available settings.
