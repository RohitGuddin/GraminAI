/** Shared frontend/API contracts. Python Pydantic in apps/api is the source of truth. */

export type LanguageCode = string;

export interface FeasibilityRequest {
  business: string;
  location: string;
  budget: number;
  own_investment: number;
  loan_required: number;
  language: LanguageCode;
}

export interface SourceMetadata {
  source: string;
  source_type?: string | null;
  source_url?: string | null;
  retrieved_at?: string | null;
  provider?: string | null;
  data_freshness?: string | null;
  last_updated?: string | null;
}

export interface FeasibilityResponse {
  request: FeasibilityRequest;
  market_analysis: Record<string, unknown> | null;
  geographic_analysis: Record<string, unknown> | null;
  competition_analysis: Record<string, unknown> | null;
  financial_analysis: Record<string, unknown> | null;
  opportunity_analysis: Record<string, unknown> | null;
  swot_analysis: Record<string, unknown> | null;
  metadata: Record<string, unknown>;
}

export interface HealthResponse {
  status: "ok";
}
