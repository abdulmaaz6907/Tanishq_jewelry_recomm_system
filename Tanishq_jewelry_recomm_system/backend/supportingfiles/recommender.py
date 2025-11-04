# recommender.py
import numpy as np
from config import Config

class RecommenderEngine:
    """Engine for finding similar jewelry items based on image embeddings."""
    
    def __init__(self, index, metadata):
        """Initialize with FAISS index and metadata.
        
        Args:
            index: FAISS index for similarity search
            metadata (dict): Metadata for the indexed items
        """
        self.index = index
        self.metadata = metadata
    
    def find_similar_items(self, embedding, num_recommendations=None, skip_exact_match=True):
        """Find similar items based on embedding vector.
        
        Args:
            embedding (numpy.ndarray): The query embedding vector
            num_recommendations (int): Number of recommendations to return
            skip_exact_match (bool): Whether to skip the first result (exact match)
            
        Returns:
            list: Sorted list of recommendation dictionaries
        """
        if self.index is None:
            print("Error: Index not loaded")
            return []
            
        if embedding is None:
            print("Error: Invalid embedding")
            return []
        
        num_recommendations = num_recommendations or Config.DEFAULT_NUM_RECOMMENDATIONS
        
        # Calculate how many items to retrieve based on whether we're skipping the first match
        search_k = num_recommendations
        if skip_exact_match:
            search_k += 1
        
        # Get exact number of results we need
        distances, indices = self.index.search(embedding.reshape(1, -1), search_k)
        
        results = []
        
        # Start from index 1 to skip the first result (closest match) if skip_exact_match is True
        start_idx = 1 if skip_exact_match and len(indices[0]) > 1 else 0
        
        for dist, idx in zip(distances[0][start_idx:], indices[0][start_idx:]):
            if idx != -1:
                metadata = self.metadata[idx]
                similarity_score = 1 / (1 + float(dist))
                
                # Add item to results without category filtering
                result = {
                    "metadata": metadata,
                    "distance": float(dist),
                    "similarity_score": similarity_score
                }
                results.append(result)
        
        # Sort by similarity score (highest first)
        results.sort(key=lambda x: x["similarity_score"], reverse=True)
        return results[:num_recommendations]
