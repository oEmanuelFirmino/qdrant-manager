import uuid
from app.core.interfaces import VectorGenerator, VectorDatabase
from app.resources.schemas import KnowledgePayload


class KnowledgeOrchestrator:
    def __init__(self, vector_gen: VectorGenerator, db: VectorDatabase):
        self.vector_gen = vector_gen
        self.db = db

    def _prepare_semantic_string(self, data: KnowledgePayload) -> str:
        return f"""
        Conceito: {data.concept_name}
        Domínio: {data.domain}
        Analogia: {data.didactic_data.analogy.content}
        Aplicação: {data.didactic_data.application.explanation}
        Tags: {', '.join(data.metadata.tags)}
        """.strip()

    def ingest_concept(self, data: KnowledgePayload):
        semantic_text = self._prepare_semantic_string(data)

        vector = self.vector_gen.generate(semantic_text, "retrieval_document")


        technical_id = str(uuid.uuid4())
        self.db.upsert(technical_id, vector, data.model_dump())

        return {"status": "success", "uuid": technical_id}

    def search_concept(self, query: str, limit: int):
        vector = self.vector_gen.generate(query, "retrieval_query")

        raw_results = self.db.search(vector, limit)

        return [
            {
                "score": res.score,
                "concept_name": res.payload.get("concept_name"),
                "didactic_summary": res.payload.get("didactic_data", {})
                .get("analogy", {})
                .get("content"),
            }
            for res in raw_results
        ]
