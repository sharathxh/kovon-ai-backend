from datetime import datetime
from typing import Dict
import uuid


class Job:
    def __init__(self, title: str, country: str, description: str):
        self.id = str(uuid.uuid4())
        self.title = title
        self.country = country
        self.description = description
        self.created_at = datetime.utcnow()



job_db: Dict[str, Job] = {}