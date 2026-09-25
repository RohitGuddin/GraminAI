# Market provider

```
Market Agent
↓
DataGovMarketDataProvider
↓
data.gov.in / AGMARKNET
↓
commodity / mandi / price data
↓
normalization
↓
context (user business + location + prices)
↓
LLMProvider → OpenRouter → MarketAnalysis
```

## Provides

Commodity, variety, state, district, market/mandi, min/max/modal price, date.

## Does not provide

Demand, customer preferences, “market opportunity”, competition. Those are LLM inference when produced at all.

Configuration: `DATA_GOV_IN_API_KEY`. HTTP is not implemented yet.
