from pydantic import BaseModel
from typing import List, Dict

class TranslationRequest(BaseModel):
    text: str
    languages: List[str]

class TaskResponse(BaseModel):
    task_id: int

class TranslationStatus(BaseModel):
    task_id: int
    status: str
    translations: Dict[str, str]