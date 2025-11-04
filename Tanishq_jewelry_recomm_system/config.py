# config.py
import os
import torch
import torchvision.transforms as transforms

class Config:
    """Configuration class for the Jewelry Recommender System."""
    
    # Model settings
    VECTOR_DIMENSION = 1280
    INDEX_PATH = "models/jewelry_index.idx"
    METADATA_PATH = "models/jewelry_metadata.pkl"
    
    # Hardware settings
    DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    # Image processing settings
    IMAGE_SIZE = (640, 640)
    NORMALIZATION_MEAN = [0.485, 0.456, 0.406]
    NORMALIZATION_STD = [0.229, 0.224, 0.225]
    
    # Recommendation settings
    DEFAULT_NUM_RECOMMENDATIONS = 5
    MAX_RECOMMENDATIONS = 20
    
    @classmethod
    def get_image_transform(cls):
        """Returns the image transformation pipeline."""
        from PIL import ImageOps
        return transforms.Compose([
            transforms.Lambda(lambda img: ImageOps.exif_transpose(img)),
            transforms.Resize(cls.IMAGE_SIZE),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=cls.NORMALIZATION_MEAN,
                std=cls.NORMALIZATION_STD
            )
        ])