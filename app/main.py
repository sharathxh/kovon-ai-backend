from fastapi import FastAPI
from app.api import candidate_routes, job_routes

app = FastAPI()

app.include_router(candidate_routes.router)
app.include_router(job_routes.router)