from typing import Protocol, List, Dict, Any, Optional


class VectorGenerator(Protocol):
    def generate(self, text: str, task_type: str) -> List[float]: ...


class VectorDatabase(Protocol):
    def upsert(
        self, point_id: str, vector: List[float], payload: Dict[str, Any]
    ) -> str: ...

    def search(self, vector: List[float], limit: int) -> List[Any]: ...
