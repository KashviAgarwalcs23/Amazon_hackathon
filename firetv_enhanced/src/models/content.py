from pydantic import BaseModel
from typing import List, Optional

class Content(BaseModel):
    id: str
    title: str
    type: str  # movie, series, etc.
    genres: List[str]
    mood_tags: List[str]
    duration: int
    rating: float
    description: str
    cast: List[str]
    release_date: str
