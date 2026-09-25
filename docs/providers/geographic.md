# Geographic provider

```
Geographic Agent
↓
GoogleMapsGeographicDataProvider
```

| API | Role |
| --- | --- |
| Google Geocoding API | Location → lat/lng, Place ID, normalized address |
| Google Places API (New) | Text Search, Nearby Search, Place Details |
| Google Routes API | Distance, duration, routes / route matrix |

Coordinates and distances are API facts. Suitability is LLM interpretation.

Configuration: `GOOGLE_MAPS_API_KEY`. Live Google calls are not implemented yet.
