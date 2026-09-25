from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Server-side configuration. API keys never go to the browser."""

    model_config = SettingsConfigDict(env_file=(".env", "../../.env"), extra="ignore")

    openrouter_api_key: str = ""
    openrouter_model: str = ""
    google_maps_api_key: str = ""
    data_gov_in_api_key: str = ""
    database_url: str = ""

    market_data_provider: str = "datagov"
    geographic_data_provider: str = "google_maps"
    competition_data_provider: str = "google_places"
    government_data_provider: str = "government_sources"

    api_host: str = "0.0.0.0"
    api_port: int = 8000
    web_origin: str = "http://localhost:3000"


@lru_cache
def get_settings() -> Settings:
    return Settings()
