from pydantic import BaseModel


class JobCreate(BaseModel):
    title: str
    country: str
    description: str


class JobResponse(BaseModel):
    id: str
    title: str
    country: str