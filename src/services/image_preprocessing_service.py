from io import BytesIO

import numpy as np
import torch
from PIL import Image, UnidentifiedImageError


class InvalidImageError(ValueError):
    pass


class ImagePreprocessingService:
    def __init__(self, image_size: int) -> None:
        self._image_size = image_size
        self._mean = np.array([0.485, 0.456, 0.406], dtype=np.float32)
        self._std = np.array([0.229, 0.224, 0.225], dtype=np.float32)

    def preprocess(self, image_bytes: bytes) -> torch.Tensor:
        try:
            with Image.open(BytesIO(image_bytes)) as image:
                image = image.convert("RGB")
                image = image.resize((self._image_size, self._image_size))
                image_array = np.asarray(image, dtype=np.float32) / 255.0
        except (UnidentifiedImageError, OSError) as exc:
            raise InvalidImageError("Uploaded file is not a valid image") from exc

        image_array = (image_array - self._mean) / self._std
        image_tensor = torch.from_numpy(image_array).permute(2, 0, 1).contiguous()
        return image_tensor.unsqueeze(0)


class PestImagePreprocessingService:
    def decode(self, image_bytes: bytes) -> Image.Image:
        try:
            with Image.open(BytesIO(image_bytes)) as image:
                return image.convert("RGB").copy()
        except (UnidentifiedImageError, OSError) as exc:
            raise InvalidImageError("Uploaded file is not a valid image") from exc
