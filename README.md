Plant Disease Classifier API

Async FastAPI API for plant disease image classification using the Hugging Face model `eymenslimani/plant-disease-detector`.

The API accepts an uploaded image and returns the top 5 most probable plant disease classes.

## Run

```bash
uv run uvicorn src.main:app --reload
```

The first startup downloads `best_model.pth` from Hugging Face and loads it into a `timm` EfficientNetV2-M model.

## Predict

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/predictions" \
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

## Health Check

```bash
curl "http://127.0.0.1:8000/health"
```

## Configuration

Runtime configuration is loaded from `src/.env`. See `src/.env.example` for available settings.
