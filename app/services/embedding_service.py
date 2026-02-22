from sentence_transformers import SentenceTransformer
import numpy as np

class EmbeddingService:
    def __init__(self):
        
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def generate_embedding(self, text: str) -> np.ndarray:
        """
        Convert input text into embedding vector
        """
        embedding = self.model.encode(text)
        return np.array(embedding, dtype="float32")