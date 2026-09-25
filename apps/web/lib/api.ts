import type { FeasibilityRequest, FeasibilityResponse, HealthResponse } from "@gramin-ai/types";

const API_URL = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

export async function getHealth(): Promise<HealthResponse> {
  const res = await fetch(`${API_URL}/health`);
  if (!res.ok) throw new Error("health failed");
  return res.json() as Promise<HealthResponse>;
}

export async function postFeasibility(body: FeasibilityRequest): Promise<FeasibilityResponse> {
  const res = await fetch(`${API_URL}/api/v1/feasibility`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  if (!res.ok) throw new Error(`feasibility failed: ${res.status}`);
  return res.json() as Promise<FeasibilityResponse>;
}
