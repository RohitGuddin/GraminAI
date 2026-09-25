from typing import Protocol


class GovernmentDataIngestionJob(Protocol):
    """Future scheduled sync. Official source → fetch → validate → normalize → upsert.

    JanSamarth is not assumed to expose a generic public API. Adapters remain behind
    this boundary until an approved source is available.
    """

    def run(self) -> None: ...
