from google import genai
from google.genai import types
from app.core.interfaces import VectorGenerator
from app.core.settings import Settings


class GeminiVectorService(VectorGenerator):
    def __init__(self):
        self.settings = Settings()
        self.client = genai.Client(api_key=self.settings.GOOGLE_API_KEY)
        self.model = "text-embedding-004"

    def generate(self, text: str, task_type: str) -> list[float]:
        """
        Gera embeddings usando o novo SDK google-genai.

        Args:
            text: O texto a ser vetorizado.
            task_type: 'retrieval_document' (ingestão) ou 'retrieval_query' (busca).
        """

        sdk_task_type = "RETRIEVAL_DOCUMENT"
        if task_type == "retrieval_query":
            sdk_task_type = "RETRIEVAL_QUERY"

        try:
            result = self.client.models.embed_content(
                model=self.model,
                contents=text,
                config=types.EmbedContentConfig(
                    task_type=sdk_task_type,
                    title="Concept" if sdk_task_type == "RETRIEVAL_DOCUMENT" else None,
                ),
            )

            return result.embeddings[0].values

        except Exception as e:
            print(f"Erro Gemini: {str(e)}")
            raise e
