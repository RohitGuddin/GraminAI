from pydantic import BaseModel, Field

from app.schemas.common import InferredStatement


class Opportunity(BaseModel):
    title: str
    reason: str
    supporting_factors: list[str] = Field(default_factory=list)


class OpportunityAnalysis(BaseModel):
    opportunities: list[Opportunity] = Field(default_factory=list)
    notes: list[InferredStatement] = Field(default_factory=list)
