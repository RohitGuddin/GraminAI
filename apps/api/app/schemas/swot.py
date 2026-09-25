from pydantic import BaseModel, Field

from app.schemas.common import InferredStatement


class SWOTAnalysis(BaseModel):
    strengths: list[InferredStatement] = Field(default_factory=list)
    weaknesses: list[InferredStatement] = Field(default_factory=list)
    opportunities: list[InferredStatement] = Field(default_factory=list)
    threats: list[InferredStatement] = Field(default_factory=list)
