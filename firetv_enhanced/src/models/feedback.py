from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Feedback(BaseModel):
    user_id: str
    content_id: str
    rating: int
    mood_after: str
    favorite_parts: List[str]
    would_rewatch: bool
    preferred_watching_time: str
    created_at: datetime
