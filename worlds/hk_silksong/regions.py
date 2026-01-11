from typing import Protocol

from BaseClasses import Region
from . import SilksongOptions
from .data.connections_data import all_connections
from .strings.region_names import all_region_names


class RegionFactory(Protocol):
    def __call__(self, name: str) -> Region:
        raise NotImplementedError


def create_regions(region_factory: RegionFactory, world_options: SilksongOptions) -> dict[str, Region]:
    regions = [region_factory(region_name) for region_name in all_region_names]

    regions_by_name: dict[str, Region] = {region.name: region for region in regions}

    for connection in all_connections:
        origin_region_name = connection.origin
        destination_region_name = connection.destination
        origin_region = regions_by_name[origin_region_name]
        destination_region = regions_by_name[destination_region_name]
        origin_region.connect(destination_region, connection.entrance)

    return regions_by_name
