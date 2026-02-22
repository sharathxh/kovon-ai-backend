from datetime import datetime
from typing import Dict
import uuid


class Candidate:
    def __init__(self, name: str, skill_description: str, experience: int, location: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.skill_description = skill_description
        self.experience = experience
        self.location = location
        self.created_at = datetime.utcnow()



candidate_db: Dict[str, Candidate] = {}