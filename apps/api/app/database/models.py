from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class GovernmentSchemeRow(Base):
    __tablename__ = "government_schemes"

    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    scheme_name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    official_source: Mapped[str] = mapped_column(String(255))
    source_url: Mapped[str | None] = mapped_column(String(1024), nullable=True)
    source_type: Mapped[str | None] = mapped_column(String(64), nullable=True)
    last_updated: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    retrieved_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    eligibility_rows: Mapped[list["SchemeEligibilityRow"]] = relationship(back_populates="scheme")
    financial_terms: Mapped[list["SchemeFinancialTermsRow"]] = relationship(back_populates="scheme")
    documents: Mapped[list["SchemeDocumentRow"]] = relationship(back_populates="scheme")
    sources: Mapped[list["SchemeSourceRow"]] = relationship(back_populates="scheme")
    updates: Mapped[list["SchemeUpdateRow"]] = relationship(back_populates="scheme")


class SchemeEligibilityRow(Base):
    __tablename__ = "scheme_eligibility"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    scheme_id: Mapped[str] = mapped_column(ForeignKey("government_schemes.id"))
    criterion: Mapped[str] = mapped_column(Text)
    scheme: Mapped[GovernmentSchemeRow] = relationship(back_populates="eligibility_rows")


class SchemeFinancialTermsRow(Base):
    __tablename__ = "scheme_financial_terms"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    scheme_id: Mapped[str] = mapped_column(ForeignKey("government_schemes.id"))
    loan_limits: Mapped[str | None] = mapped_column(Text, nullable=True)
    subsidy: Mapped[str | None] = mapped_column(Text, nullable=True)
    interest_information: Mapped[str | None] = mapped_column(Text, nullable=True)
    scheme: Mapped[GovernmentSchemeRow] = relationship(back_populates="financial_terms")


class SchemeDocumentRow(Base):
    __tablename__ = "scheme_documents"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    scheme_id: Mapped[str] = mapped_column(ForeignKey("government_schemes.id"))
    document_name: Mapped[str] = mapped_column(String(255))
    scheme: Mapped[GovernmentSchemeRow] = relationship(back_populates="documents")


class SchemeSourceRow(Base):
    __tablename__ = "scheme_sources"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    scheme_id: Mapped[str] = mapped_column(ForeignKey("government_schemes.id"))
    official_source: Mapped[str] = mapped_column(String(255))
    source_url: Mapped[str | None] = mapped_column(String(1024), nullable=True)
    source_type: Mapped[str | None] = mapped_column(String(64), nullable=True)
    scheme: Mapped[GovernmentSchemeRow] = relationship(back_populates="sources")


class SchemeUpdateRow(Base):
    __tablename__ = "scheme_updates"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    scheme_id: Mapped[str] = mapped_column(ForeignKey("government_schemes.id"))
    note: Mapped[str] = mapped_column(Text)
    recorded_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    scheme: Mapped[GovernmentSchemeRow] = relationship(back_populates="updates")
