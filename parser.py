from pydantic import BaseModel
from typing import List

class JDExtractor(BaseModel):
    skills: List[str]
    experience: str
    education: str