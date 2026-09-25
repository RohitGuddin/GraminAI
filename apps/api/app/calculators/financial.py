from datetime import datetime, timezone
from math import pow

from app.schemas.finance import FinancialCalculationResult, FinancialInputs, RepaymentInstallment


class FinancialCalculator:
    """Authoritative reducing-balance EMI. Independent of any LLM."""

    def calculate(self, inputs: FinancialInputs) -> FinancialCalculationResult:
        principal = float(inputs.loan_amount)
        annual = float(inputs.interest_rate)
        tenure = int(inputs.tenure)
        moratorium = int(inputs.moratorium)
        if moratorium >= tenure:
            raise ValueError("moratorium must be less than tenure")

        monthly_rate = annual / 12.0 / 100.0
        capitalized = principal
        for _ in range(moratorium):
            capitalized *= 1 + monthly_rate

        remaining_periods = tenure - moratorium
        emi = self._emi(capitalized, monthly_rate, remaining_periods)
        schedule: list[RepaymentInstallment] = []
        balance = capitalized
        total_interest = capitalized - principal

        for i in range(1, remaining_periods + 1):
            interest_component = balance * monthly_rate
            principal_component = emi - interest_component
            if i == remaining_periods:
                principal_component = balance
                emi_this = principal_component + interest_component
            else:
                emi_this = emi
            balance = max(0.0, balance - principal_component)
            total_interest += interest_component
            schedule.append(
                RepaymentInstallment(
                    period=moratorium + i,
                    emi=round(emi_this, 2),
                    principal_component=round(principal_component, 2),
                    interest_component=round(interest_component, 2),
                    remaining_principal=round(balance, 2),
                )
            )

        total_repayment = principal + total_interest
        return FinancialCalculationResult(
            principal=round(principal, 2),
            emi=round(emi, 2),
            total_interest=round(total_interest, 2),
            total_repayment=round(total_repayment, 2),
            repayment_schedule=schedule,
            calculation_method="reducing_balance_emi_with_interest_capitalizing_moratorium",
            calculated_at=datetime.now(timezone.utc),
        )

    @staticmethod
    def _emi(principal: float, monthly_rate: float, n: int) -> float:
        if n <= 0:
            raise ValueError("remaining tenure must be positive")
        if monthly_rate == 0:
            return principal / n
        factor = pow(1 + monthly_rate, n)
        return principal * monthly_rate * factor / (factor - 1)
