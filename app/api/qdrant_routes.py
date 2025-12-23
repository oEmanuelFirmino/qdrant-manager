from fastapi import APIRouter, Depends, HTTPException
from app.resources.schemas import KnowledgePayload, SearchRequest
from app.services.orchestrator import KnowledgeOrchestrator
from app.api.dependencies import get_orchestrator

router = APIRouter()


@router.post("/ingest", status_code=201)
async def ingest_knowledge(
    payload: KnowledgePayload,
    service: KnowledgeOrchestrator = Depends(get_orchestrator),
):
    try:
        return service.ingest_concept(payload)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/search")
async def search_knowledge(
    request: SearchRequest, service: KnowledgeOrchestrator = Depends(get_orchestrator)
):
    try:
        return service.search_concept(request.query, request.limit)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
