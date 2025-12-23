from qdrant_client import QdrantClient
from qdrant_client.http import models
from app.core.interfaces import VectorDatabase
from app.core import Settings
from typing import List, Dict, Any
from dotenv import load_dotenv

load_dotenv()


class QdrantService(VectorDatabase):
    def __init__(self):
        self.settings = Settings()
        self.client = QdrantClient(
            url=self.settings.QDRANT_URL, api_key=self.settings.QDRANT_API_KEY
        )

    def upsert(
        self, point_id: str, vector: List[float], payload: Dict[str, Any]
    ) -> str:
        point = models.PointStruct(
            id=point_id, payload=payload, vector={self.settings.VECTOR_NAME: vector}
        )

        self.client.upsert(
            collection_name=self.settings.QDRANT_COLLECTION_NAME, points=[point]
        )
        return point_id

    def search(self, vector: List[float], limit: int) -> List[Any]:
        result = self.client.query_points(
            collection_name=self.settings.QDRANT_COLLECTION_NAME,
            query=vector,
            using=self.settings.QDRANT_VECTOR_NAME,
            limit=limit,
        )
        return result.points
