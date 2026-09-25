# Competition provider

```
Competition Agent
↓
GooglePlacesCompetitionProvider
↓
Google Places API (New)
  Text Search | Nearby Search | Place Details
↓
normalized Competitor rows
↓
OpenRouter → CompetitionAnalysis
```

## Observed

place_id, name, category, address, lat/lng, rating, user_rating_count, business_status, website when returned by Places.

## Not observed (do not invent)

Revenue, profit, market share, sales volume, exact product pricing.

Queries are built from business + location, not a hardcoded dairy-only string.
