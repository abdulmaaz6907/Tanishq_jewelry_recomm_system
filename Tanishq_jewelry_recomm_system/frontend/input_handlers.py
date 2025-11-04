# input_handlers.py
import requests
import io
import base64
from PIL import Image
from backend.jewelry_recomm_service import JewelryRecommenderService
from utils.formatter import ResultFormatter

class InputHandlers:
    """Handles different types of image inputs for recommendation."""
    
    @staticmethod
    def process_image(image, num_recommendations=5, skip_exact_match=True):
        """Process direct image input.
        
        Args:
            image: The image (PIL, numpy array, etc.)
            num_recommendations (int): Number of recommendations
            skip_exact_match (bool): Whether to skip the first/exact match
            
        Returns:
            str: HTML formatted results or error message
        """
        try:
            # Initialize the recommender service
            recommender = JewelryRecommenderService()
            
            # Get recommendations
            recommendations = recommender.get_recommendations(
                image, num_recommendations, skip_exact_match
            )
            
            # Format and return the results as HTML
            return ResultFormatter.format_html(recommendations)
        
        except Exception as e:
            # Log the error for debugging
            print(f"Error processing image: {str(e)}")
            
            # Return a user-friendly error message
            return "<p style='color: red;'>Error: Unable to process the image. Please try again.</p>"
    
    @staticmethod
    def process_url(url, num_recommendations=5, skip_exact_match=True):
        """Process image from URL.
        
        Args:
            url (str): URL to the image
            num_recommendations (int): Number of recommendations
            skip_exact_match (bool): Whether to skip the first/exact match
            
        Returns:
            str: HTML formatted results
        """
        try:
            import requests
            response = requests.get(url)
            image = Image.open(io.BytesIO(response.content))
            return InputHandlers.process_image(image, num_recommendations, skip_exact_match)
        except Exception as e:
            return f"Error processing URL: {str(e)}"
    
    @staticmethod
    def process_base64(base64_string, num_recommendations=5, skip_exact_match=True):
        """Process base64-encoded image.
        
        Args:
            base64_string (str): Base64 encoded image
            num_recommendations (int): Number of recommendations
            skip_exact_match (bool): Whether to skip the first/exact match
            
        Returns:
            str: HTML formatted results
        """
        try:
            # Remove data URL prefix if present
            if ',' in base64_string:
                base64_string = base64_string.split(',', 1)[1]
            
            image_bytes = base64.b64decode(base64_string)
            image = Image.open(io.BytesIO(image_bytes))
            return InputHandlers.process_image(image, num_recommendations, skip_exact_match)
        except Exception as e:
            return f"Error processing base64 image: {str(e)}"
