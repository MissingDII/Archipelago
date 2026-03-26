from typing import Protocol

from BaseClasses import Region, MultiWorld
from . import SilksongOptions
from .data.connections_data import all_connections, connections_by_name
from .strings.region_names import all_region_names
from ..generic.Rules import add_rule


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


def has_requirement(state, requirement: str | tuple[str, ...], player, count):
    if isinstance(requirement, str):
        return state.has(requirement, player, count)
    return state.has_from_list([*requirement], player, count)


def set_entrance_rules(multiworld: MultiWorld, player: int, world_options: SilksongOptions) -> None:
    for entrance_name, entrance in multiworld.regions.entrance_cache[player].items():
        entrance_data = connections_by_name[entrance_name]
        if entrance_data.requirements:
            for requirement, amount in entrance_data.requirements.items():
                add_rule(entrance, lambda state, req=requirement, player=player, count=amount: has_requirement(state, req, player, count))
