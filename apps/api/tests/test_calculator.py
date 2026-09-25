from app.calculators.financial import FinancialCalculator
from app.schemas.finance import FinancialInputs


def test_zero_rate_splits_principal() -> None:
    calc = FinancialCalculator()
    result = calc.calculate(
        FinancialInputs(
            project_cost=1200,
            own_investment=200,
            loan_amount=1200,
            interest_rate=0,
            tenure=12,
            moratorium=0,
        )
    )
    assert result.emi == 100
    assert result.principal == 1200
    assert result.total_interest == 0


def test_positive_rate_emi_is_deterministic() -> None:
    calc = FinancialCalculator()
    inputs = FinancialInputs(
        project_cost=100000,
        own_investment=0,
        loan_amount=100000,
        interest_rate=12,
        tenure=12,
        moratorium=0,
    )
    a = calc.calculate(inputs)
    b = calc.calculate(inputs)
    assert a.emi == b.emi
    assert a.emi > 0
    assert a.total_repayment >= a.principal
