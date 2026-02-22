import faiss
import numpy as np
from typing import List, Tuple


class FaissStore:
    def __init__(self, dimension: int = 384):
        """
        dimension = embedding size (384 for all-MiniLM-L6-v2)
        """
        self.dimension = dimension

        
        self.index = faiss.IndexFlatIP(dimension)

        
        self.id_map = []  # stores IDs in insertion order

    def add_vector(self, vector: np.ndarray, item_id: str):
        """
        Add embedding vector to FAISS index
        """
        vector = np.expand_dims(vector, axis=0)

        
        faiss.normalize_L2(vector)

        self.index.add(vector)
        self.id_map.append(item_id)

    def search(self, query_vector: np.ndarray, top_k: int = 5) -> List[Tuple[str, float]]:
        """
        Perform similarity search
        Returns list of (item_id, similarity_score)
        """
        query_vector = np.expand_dims(query_vector, axis=0)

        
        faiss.normalize_L2(query_vector)

        scores, indices = self.index.search(query_vector, top_k)

        results = []
        for score, idx in zip(scores[0], indices[0]):
            if idx == -1:
                continue
            item_id = self.id_map[idx]
            results.append((item_id, float(score)))

        return results