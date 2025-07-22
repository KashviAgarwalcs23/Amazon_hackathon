from typing import List, Dict
from datetime import datetime

class SocialFeatures:
    def __init__(self):
        self.active_watch_parties = {}

    def create_watch_party(self, host_id: str, content_id: str) -> str:
        """
        Create a new watch party
        """
        party_id = f"party_{datetime.now().timestamp()}"
        self.active_watch_parties[party_id] = {
            "host_id": host_id,
            "content_id": content_id,
            "participants": [host_id],
            "created_at": datetime.now()
        }
        return party_id

    def join_watch_party(self, party_id: str, user_id: str) -> bool:
        """
        Join an existing watch party
        """
        if party_id in self.active_watch_parties:
            self.active_watch_parties[party_id]["participants"].append(user_id)
            return True
        return False

    def get_active_parties(self) -> List[Dict]:
        """
        Get list of active watch parties
        """
        return [
            {
                "party_id": party_id,
                "host_id": party["host_id"],
                "content_id": party["content_id"],
                "participant_count": len(party["participants"])
            }
            for party_id, party in self.active_watch_parties.items()
        ]
