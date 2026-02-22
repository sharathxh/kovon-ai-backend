from fastapi import APIRouter
from app.schemas.candidate_schema import CandidateCreate, CandidateResponse
from app.models.candidate_model import Candidate, candidate_db
from app.services.embedding_service import EmbeddingService
from app.db.faiss_store import FaissStore

router = APIRouter()

from app.config import embedding_service, candidate_faiss_store


@router.post("/candidates", response_model=CandidateResponse)
def create_candidate(candidate_data: CandidateCreate):
    # 1️⃣ Create candidate object
    candidate = Candidate(
        name=candidate_data.name,
        skill_description=candidate_data.skill_description,
        experience=candidate_data.experience,
        location=candidate_data.location
    )

    
    embedding = embedding_service.generate_embedding(candidate.skill_description)

    
    candidate_faiss_store.add_vector(embedding, candidate.id)

    
    candidate_db[candidate.id] = candidate

    return CandidateResponse(
        id=candidate.id,
        name=candidate.name,
        experience=candidate.experience,
        location=candidate.location
    )