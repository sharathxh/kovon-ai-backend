from app.services.embedding_service import EmbeddingService
from app.db.faiss_store import FaissStore


embedding_service = EmbeddingService()


candidate_faiss_store = FaissStore()