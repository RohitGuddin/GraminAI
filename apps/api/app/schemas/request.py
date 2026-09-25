from pydantic import BaseModel, Field, model_validator


class FeasibilityRequest(BaseModel):
    """User input collected by Next.js and posted to FastAPI."""

    business: str = Field(min_length=1)
    location: str = Field(min_length=1)
    budget: float = Field(gt=0)
    own_investment: float = Field(ge=0)
    loan_required: float = Field(ge=0)
    language: str = Field(min_length=2)

    @model_validator(mode="after")
    def own_plus_loan_reasonable(self) -> "FeasibilityRequest":
        if self.own_investment + self.loan_required <= 0:
            raise ValueError("own_investment and loan_required cannot both be zero")
        return self
