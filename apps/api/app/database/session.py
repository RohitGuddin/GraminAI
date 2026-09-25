"""Session factory is planned. Agents must not import this module."""

from app.core.config import get_settings


def get_database_url() -> str:
    return get_settings().database_url
