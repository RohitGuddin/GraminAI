# PostgreSQL schemes

Normalized tables: `government_schemes`, `scheme_eligibility`, `scheme_financial_terms`, `scheme_documents`, `scheme_sources`, `scheme_updates`.

Every scheme keeps `official_source`, `source_url`, `source_type`, `last_updated`, `retrieved_at`.

`GovernmentDataIngestionJob` is an interface only. No invented scheme rows are loaded.
