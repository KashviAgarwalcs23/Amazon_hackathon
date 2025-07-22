from typing import Dict, List
from ..models.feedback import Feedback
from datetime import datetime

class FeedbackCollector:
    def __init__(self):
        self.feedback_history = []

    def collect_feedback(self, user_id: str, content_id: str, feedback_data: Dict) -> Feedback:
        """
        Collect and store user feedback
        """
        feedback = Feedback(
            user_id=user_id,
            content_id=content_id,
            rating=feedback_data.get("rating", 0),
            mood_after=feedback_data.get("mood_after", ""),
            favorite_parts=feedback_data.get("favorite_parts", []),
            would_rewatch=feedback_data.get("would_rewatch", False),
            preferred_watching_time=feedback_data.get("preferred_watching_time", ""),
            created_at=datetime.now()
        )
        
        self.feedback_history.append(feedback)
        return feedback

    def get_user_feedback_history(self, user_id: str) -> List[Feedback]:
        """
        Get feedback history for a specific user
        """
        return [f for f in self.feedback_history if f.user_id == user_id]
