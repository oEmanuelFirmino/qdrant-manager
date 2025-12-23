from functools import lru_cache
from app.services.google_gemini import GeminiVectorService
from app.services.qdrant import QdrantService
from app.services.orchestrator import KnowledgeOrchestrator


@lru_cache()
def get_orchestrator() -> KnowledgeOrchestrator:
    vector_service = GeminiVectorService()
    storage_service = QdrantService()

    return KnowledgeOrchestrator(vector_gen=vector_service, db=storage_service)
