# model_loader.py
import os
import pickle
import faiss
import torch
import torchvision.models as models
import warnings
from config import Config

class ModelLoader:
    """Handles loading of the feature extraction model and FAISS index."""
    
    @staticmethod
    def load_feature_extraction_model():
        """Loads and configures the EfficientNet model for feature extraction."""
        print("Loading feature extraction model...")
        model = models.efficientnet_b0(weights='EfficientNet_B0_Weights.DEFAULT')
        model.eval()
        # Remove the classification head
        model = torch.nn.Sequential(*list(model.children())[:-1])
        model = model.to(Config.DEVICE)
        return model
    
    @staticmethod
    def load_index_and_metadata(index_path=None, metadata_path=None):
        """Loads the FAISS index and metadata from files.
        
        Args:
            index_path (str): Path to the FAISS index file
            metadata_path (str): Path to the metadata pickle file
            
        Returns:
            tuple: (index, metadata, success_flag)
        """
        warnings.filterwarnings("ignore")
        
        index_path = index_path or Config.INDEX_PATH
        metadata_path = metadata_path or Config.METADATA_PATH
        
        try:
            if os.path.exists(index_path) and os.path.exists(metadata_path):
                index = faiss.read_index(index_path)
                with open(metadata_path, "rb") as f:
                    metadata = pickle.load(f)
                print(f"Index and metadata loaded successfully.")
                return index, metadata, True
            else:
                print(f"Index file or metadata file not found.")
                return None, {}, False
        except Exception as e:
            print(f"Error loading index or metadata: {e}")
            return None, {}, False
