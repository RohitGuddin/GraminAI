from typing import Protocol

from app.schemas.geography import GeographicData, NearbyPlace, RouteDatum
from app.schemas.request import FeasibilityRequest


class GeographicDataProvider(Protocol):
    """Google Maps Platform: Geocoding, Places (New), Routes."""

    def geocode_location(self, location: str) -> GeographicData: ...

    def search_nearby_places(
        self, *, latitude: float, longitude: float, radius_meters: int, place_types: list[str]
    ) -> list[NearbyPlace]: ...

    def search_text_places(self, query: str) -> list[NearbyPlace]: ...

    def get_place_details(self, place_id: str) -> NearbyPlace: ...

    def calculate_route(self, origin: str, destination: str) -> RouteDatum: ...

    def calculate_distance_matrix(
        self, origins: list[str], destinations: list[str]
    ) -> list[RouteDatum]: ...

    def fetch_geographic_data(self, request: FeasibilityRequest) -> GeographicData: ...
