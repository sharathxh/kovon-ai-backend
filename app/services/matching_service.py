from typing import List, Dict
from app.models.candidate_model import candidate_db
from app.models.job_model import job_db
from app.config import embedding_service, candidate_faiss_store


class MatchingService:

    def match_candidates(self, job_id: str, top_k: int = 5) -> List[Dict]:

        
        job = job_db.get(job_id)
        if not job:
            return []

        
        job_embedding = embedding_service.generate_embedding(job.description)

        
        results = candidate_faiss_store.search(job_embedding, top_k=10)

        matched_candidates = []

        for item_id, score in results:
            
            if item_id in candidate_db:
                candidate = candidate_db[item_id]
                matched_candidates.append({
                    "candidateId": candidate.id,
                    "similarityScore": round(score, 4),
                    "experience": candidate.experience
                })

        
        matched_candidates.sort(
            key=lambda x: (x["similarityScore"], x["experience"]),
            reverse=True
        )

        return matched_candidates[:top_k]