from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


class GraminAIError(Exception):
    def __init__(self, message: str, status_code: int = 500) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.message = message


class ProviderNotImplementedError(GraminAIError):
    def __init__(self, provider: str) -> None:
        super().__init__(f"{provider} HTTP integration is not implemented yet.", 501)


class LLMProviderError(GraminAIError):
    def __init__(self, message: str, status_code: int = 502) -> None:
        super().__init__(message, status_code)


class OpenRouterAuthError(LLMProviderError):
    def __init__(self) -> None:
        super().__init__("OpenRouter authentication failed.", 401)


class OpenRouterRateLimitError(LLMProviderError):
    def __init__(self) -> None:
        super().__init__("OpenRouter rate limited the request.", 429)


class OpenRouterTimeoutError(LLMProviderError):
    def __init__(self) -> None:
        super().__init__("OpenRouter request timed out.", 504)


class StructuredOutputError(LLMProviderError):
    def __init__(self, message: str = "LLM output failed schema validation.") -> None:
        super().__init__(message, 502)


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(GraminAIError)
    async def handle_gramin_error(_request: Request, exc: GraminAIError) -> JSONResponse:
        return JSONResponse(status_code=exc.status_code, content={"detail": exc.message})

    @app.exception_handler(NotImplementedError)
    async def handle_not_implemented(_request: Request, exc: NotImplementedError) -> JSONResponse:
        return JSONResponse(status_code=501, content={"detail": str(exc) or "Not implemented."})
