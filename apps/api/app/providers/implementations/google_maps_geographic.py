from app.core.exceptions import ProviderNotImplementedError
from app.schemas.geography import GeographicData, NearbyPlace, RouteDatum
from app.schemas.request import FeasibilityRequest


class GoogleMapsGeographicDataProvider:
    """Planned adapter: Google Geocoding, Places API (New), Routes API.

    Uses GOOGLE_MAPS_API_KEY. Coordinates come from Geocoding, not the LLM.
    """

    def __init__(self, api_key: str) -> None:
        self._api_key = api_key

    def geocode_location(self, location: str) -> GeographicData:
        raise ProviderNotImplementedError("GoogleMapsGeographicDataProvider.geocode_location")

    def search_nearby_places(
        self, *, latitude: float, longitude: float, radius_meters: int, place_types: list[str]
    ) -> list[NearbyPlace]:
        raise ProviderNotImplementedError("GoogleMapsGeographicDataProvider.search_nearby_places")

    def search_text_places(self, query: str) -> list[NearbyPlace]:
        raise ProviderNotImplementedError("GoogleMapsGeographicDataProvider.search_text_places")

    def get_place_details(self, place_id: str) -> NearbyPlace:
        raise ProviderNotImplementedError("GoogleMapsGeographicDataProvider.get_place_details")

    def calculate_route(self, origin: str, destination: str) -> RouteDatum:
        raise ProviderNotImplementedError("GoogleMapsGeographicDataProvider.calculate_route")

    def calculate_distance_matrix(
        self, origins: list[str], destinations: list[str]
    ) -> list[RouteDatum]:
        raise ProviderNotImplementedError("GoogleMapsGeographicDataProvider.calculate_distance_matrix")

    def fetch_geographic_data(self, request: FeasibilityRequest) -> GeographicData:
        raise ProviderNotImplementedError("GoogleMapsGeographicDataProvider.fetch_geographic_data")
