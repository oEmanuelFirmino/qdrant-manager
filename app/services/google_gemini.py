from google import genai
from google.genai import types
from app.core.interfaces import VectorGenerator
from app.core.settings import Settings
from dotenv import load_dotenv

load_dotenv()


class GeminiVectorService(VectorGenerator):
    def __init__(self):
        self.settings = Settings()
        self.client = genai.Client(api_key=self.settings.GOOGLE_API_KEY)
        self.model = "models/text-embedding-004"

    def generate(self, text: str, task_type: str) -> list[float]:
        result = self.client.embed_content(
            model=self.model,
            content=text,
            task_type=task_type,
            title="Concept" if task_type == "retrieval_document" else None,
        )
        return result["embedding"]
