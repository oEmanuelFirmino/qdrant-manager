from typing import Protocol, List, Dict, Any, Optional


class VectorGenerator(Protocol):
    def generate(self, text: str, task_type: str) -> List[float]:
        """Gera o embedding para o texto dado."""
        ...


class VectorDatabase(Protocol):
    def upsert(
        self, point_id: str, vector: List[float], payload: Dict[str, Any]
    ) -> str:
        """Insere ou atualiza um ponto."""
        ...

    def search(self, vector: List[float], limit: int) -> List[Any]:
        """Busca por similaridade."""
        ...
