from pydantic import BaseModel
from pydantic_settings import BaseSettings


# ==============================
# Configurações básicas da API
# ==============================
class Settings(BaseSettings):
    # Indentificacao
    app_name: str = "Qdrant Manager"
    description: str = "Manage your Qdrant instance with ease"
    environment: str = "development"

    # Servidor
    host: str = "0.0.0.0"
    port: int = 8000
    debug: bool = False

    # CORS
    allowed_origins: list[str] = ["*"]
    allowed_credentials: bool = True
    allowed_methods: list[str] = ["*"]
    allowed_headers: list[str] = ["*"]

    # Google Gemini
    GOOGLE_API_KEY: str

    # Qdrant
    QDRANT_URL: str = "http://localhost:6333"
    QDRANT_API_KEY: str | None = None
    QDRANT_COLLECTION_NAME: str = "engineering_knowledge"
    QDRANT_VECTOR_SIZE: int = 768  # Gemini text-embedding-004

    class Config:
        env_file: str = ".env"
        env_file_encoding: str = "utf-8"


# ======================================
# Modelos de retorno das rotas básicas
# ======================================
class ApplicationInfo(BaseModel):
    name: str
    description: str
    environment: str


class ServerInfo(BaseModel):
    host: str
    port: int
    debug: bool


class RootResponse(BaseModel):
    application: ApplicationInfo
    server: ServerInfo


class HealthResponse(BaseModel):
    status: str
    message: str
