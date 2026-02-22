from fastapi import APIRouter
from app.schemas.job_schema import JobCreate, JobResponse
from app.models.job_model import Job, job_db
from app.services.embedding_service import EmbeddingService
from app.db.faiss_store import FaissStore

router = APIRouter()

from app.config import embedding_service


@router.post("/jobs", response_model=JobResponse)
def create_job(job_data: JobCreate):

    
    job = Job(
        title=job_data.title,
        country=job_data.country,
        description=job_data.description
    )

    
    embedding = embedding_service.generate_embedding(job.description)

    
    
    job_db[job.id] = job

    return JobResponse(
        id=job.id,
        title=job.title,
        country=job.country
    )
    
from app.services.matching_service import MatchingService

matching_service = MatchingService()


@router.get("/jobs/{job_id}/match")
def match_candidates(job_id: str):
    return matching_service.match_candidates(job_id)