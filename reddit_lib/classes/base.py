from typing import TypedDict


class Thing(TypedDict):
    kind: str


class ThingData(TypedDict):
    after: str
    before: str
    dist: int
    geo_filter: str
    modhash: str