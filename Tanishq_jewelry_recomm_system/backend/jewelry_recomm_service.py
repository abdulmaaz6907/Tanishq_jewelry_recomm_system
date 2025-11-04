# jewelry_recommender.py
import warnings
from config import Config

from backend.supportingfiles.model_loader import ModelLoader
from backend.supportingfiles.image_processor import ImageProcessor
from backend.supportingfiles.recommender import RecommenderEngine

class JewelryRecommenderService:
    """Main service class for the Jewelry Recommender System."""
    
    def __init__(self, 
                index_path=None, 
                metadata_path=None):
        """Initialize the jewelry recommender service.
        
        Args:
            index_path (str, optional): Path to FAISS index
            metadata_path (str, optional): Path to metadata pickle file
        """
        warnings.filterwarnings("ignore")
        
        # Load the model
        self.model = ModelLoader.load_feature_extraction_model()
        
        # Load index and metadata
        self.index, self.metadata, success = ModelLoader.load_index_and_metadata(
            index_path, metadata_path
        )
        
        # Initialize pipeline components
        self.image_processor = ImageProcessor(self.model)
        self.recommender = RecommenderEngine(self.index, self.metadata)

    def get_recommendations(self, image, num_recommendations=None, skip_exact_match=True):
        """Get recommendations for a query image.
        
        Args:
            image: Query image (various formats)
            num_recommendations (int, optional): Number of recommendations
            skip_exact_match (bool): Whether to skip the first/exact match
            
        Returns:
            list: Recommendation results
        """
        if not self.index or not self.metadata:
            return [{"error": "Index/metadata not loaded"}]
        
        if image is None:
            return [{"error": "Invalid image input"}]
        
        num_recommendations = num_recommendations or Config.DEFAULT_NUM_RECOMMENDATIONS
        
        # Extract embedding from the image
        embedding = self.image_processor.extract_embedding(image)
        if embedding is None:
            return [{"error": "Failed to process image"}]
        
        # Get similar items based on the embedding
        recommendations = self.recommender.find_similar_items(
            embedding, num_recommendations, skip_exact_match
        )
        
        return recommendations
    
