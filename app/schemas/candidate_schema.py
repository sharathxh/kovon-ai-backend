from pydantic import BaseModel


class CandidateCreate(BaseModel):
    name: str
    skill_description: str
    experience: int
    location: str


class CandidateResponse(BaseModel):
    id: str
    name: str
    experience: int
    location: str