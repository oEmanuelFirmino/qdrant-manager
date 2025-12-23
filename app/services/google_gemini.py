import google.generativeai as genai
from app.core.interfaces import VectorGenerator
from app.core.settings import settings


class GeminiVectorService(VectorGenerator):
    def __init__(self):
        genai.configure(api_key=settings.GOOGLE_API_KEY)
        self.model = "models/text-embedding-004"

    def generate(self, text: str, task_type: str) -> list[float]:
        # task_type deve ser 'retrieval_document' ou 'retrieval_query'
        result = genai.embed_content(
            model=self.model,
            content=text,
            task_type=task_type,
            title="Concept" if task_type == "retrieval_document" else None,
        )
        return result["embedding"]
