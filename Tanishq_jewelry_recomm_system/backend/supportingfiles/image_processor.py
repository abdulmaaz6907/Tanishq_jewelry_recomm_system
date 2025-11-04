# image_processor.py
import io
import torch
import numpy as np
from PIL import Image
from config import Config

class ImageProcessor:
    """Handles processing and feature extraction from images."""
    
    def __init__(self, model):
        """Initialize with a pre-trained model.
        
        Args:
            model: The pre-trained model for feature extraction
        """
        self.model = model
        self.transform = Config.get_image_transform()
    
    def normalize_image_input(self, image):
        """Normalize different image input types to a PIL Image.
        
        Args:
            image: Can be a PIL.Image, file path, byte stream, or numpy array
            
        Returns:
            PIL.Image: The normalized image
        """
        try:
            if isinstance(image, str):
                # If image is a file path
                return Image.open(image).convert('RGB')
            elif isinstance(image, bytes) or isinstance(image, io.BytesIO):
                # If image is a byte stream
                if isinstance(image, bytes):
                    image = io.BytesIO(image)
                return Image.open(image).convert('RGB')
            elif isinstance(image, np.ndarray):
                # If image is a numpy array (as from gradio)
                return Image.fromarray(image.astype('uint8')).convert('RGB')
            elif isinstance(image, Image.Image):
                # If image is already a PIL Image
                return image.convert('RGB')
            else:
                raise ValueError(f"Unsupported image type: {type(image)}")
        except Exception as e:
            print(f"Error normalizing image: {str(e)}")
            return None
  
    # def process_image(image, num_recommendations=5, skip_exact_match=True):
    #     """Process the selected image and return recommendations."""
    #     if isinstance(image, str):  # If the input is a file path
    #         image = Image.open(image)
        
    #     recommender = JewelryRecommenderService()
    #     recommendations = recommender.get_recommendations(image, num_recommendations, skip_exact_match)
    #     return ResultFormatter.format_html(recommendations)
        
    def extract_embedding(self, image):
        """Extract feature embedding from an image.
        
        Args:
            image: The image to extract features from (various formats accepted)
            
        Returns:
            numpy.ndarray: The feature embedding or None if extraction failed
        """
        try:
            img = self.normalize_image_input(image)
            if img is None:
                return None
                
            img_tensor = self.transform(img).unsqueeze(0).to(Config.DEVICE)
            with torch.no_grad():
                embedding = self.model(img_tensor).flatten().cpu().numpy()
            return embedding
        except Exception as e:
            print(f"Error extracting embedding: {str(e)}")
            return None
