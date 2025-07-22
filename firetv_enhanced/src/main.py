from fastapi import FastAPI, HTTPException
from typing import List, Dict
from .models.user import User, UserPreferences
from .models.content import Content
from .services.recommendation_engine import RecommendationEngine
from .services.mood_analyzer import MoodAnalyzer
from .services.social_features import SocialFeatures
from .services.feedback_collector import FeedbackCollector

app = FastAPI(title="Enhanced Fire TV Experience")

# Initialize services
recommendation_engine = RecommendationEngine()
mood_analyzer = MoodAnalyzer()
social_features = SocialFeatures()
feedback_collector = FeedbackCollector()

@app.get("/")
def read_root():
    return {"message": "Welcome to Enhanced Fire TV Experience API"}

@app.post("/users/")
def create_user(user: User):
    # In real implementation, this would save to a database
    return {"user_id": user.id, "message": "User created successfully"}

@app.get("/recommendations/{user_id}")
def get_recommendations(user_id: str, context: Dict):
    # In real implementation, this would fetch user from database
    user = User(
        id=user_id,
        name="Test User",
        preferences=UserPreferences(
            preferred_genres=["action", "comedy"],
            preferred_watching_times=["evening"],
            mood_preferences=["excited", "happy"],
            social_circle=[]
        ),
        watch_history=[],
        created_at=datetime.now(),
        last_active=datetime.now()
    )
    return recommendation_engine.get_recommendations(user, context)

@app.post("/watch-party/")
def create_watch_party(host_id: str, content_id: str):
    party_id = social_features.create_watch_party(host_id, content_id)
    return {"party_id": party_id}

@app.post("/feedback/")
def submit_feedback(user_id: str, content_id: str, feedback_data: Dict):
    feedback = feedback_collector.collect_feedback(user_id, content_id, feedback_data)
    return {"feedback_id": id(feedback), "message": "Feedback submitted successfully"}
