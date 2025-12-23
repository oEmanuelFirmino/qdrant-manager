from pydantic import BaseModel, Field
from typing import List


# --- Value Objects ---
class Analogy(BaseModel):
    title: str
    source_domain: str
    content: str


class History(BaseModel):
    hook: str
    protagonist: str
    year: int
    content: str


class Application(BaseModel):
    field: str
    example: str
    explanation: str


class DidacticData(BaseModel):
    analogy: Analogy
    history: History
    application: Application


class Metadata(BaseModel):
    tags: List[str]


# --- Entities / DTOs ---
class KnowledgePayload(BaseModel):
    record_id: str
    concept_name: str
    concept_slug: str
    domain: str
    difficulty_level: int = Field(..., ge=1, le=5)
    didactic_data: DidacticData
    metadata: Metadata


class SearchRequest(BaseModel):
    query: str
    limit: int = 3


class SearchResponse(BaseModel):
    score: float
    concept_name: str
    didactic_summary: str
