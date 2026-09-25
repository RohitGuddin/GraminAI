"use client";

import { useCallback, useState } from "react";
import type { FeasibilityRequest, FeasibilityResponse } from "@gramin-ai/types";
import { postFeasibility } from "../lib/api";

export function useFeasibility() {
  const [data, setData] = useState<FeasibilityResponse | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  const submit = useCallback(async (request: FeasibilityRequest) => {
    setLoading(true);
    setError(null);
    try {
      const result = await postFeasibility(request);
      setData(result);
      return result;
    } catch (err) {
      setError(err instanceof Error ? err.message : "request failed");
      return null;
    } finally {
      setLoading(false);
    }
  }, []);

  return { data, error, loading, submit };
}
