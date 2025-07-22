from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class UserPreferences(BaseModel):
    preferred_genres: List[str]
    preferred_watching_times: List[str]
    mood_preferences: List[str]
    social_circle: List[str]

class User(BaseModel):
    id: str
    name: str
    preferences: UserPreferences
    watch_history: List[str]
    created_at: datetime
    last_active: datetime
