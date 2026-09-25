from app.schemas.geography import GeographicData, NearbyPlace, RouteDatum
from app.schemas.request import FeasibilityRequest


class MockGeographicDataProvider:
    def __init__(self, data: GeographicData | None = None) -> None:
        self.data = data or GeographicData()
        self.calls = 0

    def geocode_location(self, location: str) -> GeographicData:
        self.calls += 1
        return self.data

    def search_nearby_places(
        self, *, latitude: float, longitude: float, radius_meters: int, place_types: list[str]
    ) -> list[NearbyPlace]:
        return list(self.data.nearby_places)

    def search_text_places(self, query: str) -> list[NearbyPlace]:
        return list(self.data.nearby_places)

    def get_place_details(self, place_id: str) -> NearbyPlace:
        return self.data.nearby_places[0] if self.data.nearby_places else NearbyPlace(place_id=place_id)

    def calculate_route(self, origin: str, destination: str) -> RouteDatum:
        return RouteDatum(origin=origin, destination=destination)

    def calculate_distance_matrix(
        self, origins: list[str], destinations: list[str]
    ) -> list[RouteDatum]:
        return []

    def fetch_geographic_data(self, request: FeasibilityRequest) -> GeographicData:
        self.calls += 1
        return self.data
