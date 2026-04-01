from typing import Protocol

from BaseClasses import Region, MultiWorld
from . import SilksongOptions
from .data.connections_data import all_connections, connections_by_name
from .logic.combat_logic import combat_logic_requirements
from .options.options import CombatLogic
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


def set_entrance_rules(multiworld: MultiWorld, player: int) -> None:
    for entrance_name, entrance in multiworld.regions.entrance_cache[player].items():
        entrance_data = connections_by_name[entrance_name]
        if entrance_data.requirements:
            for requirement, amount in entrance_data.requirements.items():
                add_rule(entrance, lambda state, req=requirement, player=player, count=amount: has_requirement(state, req, player, count))


def merge_requirements(requirements1: dict[str | tuple[str], int], requirements2: dict[str | tuple[str], int]) -> dict[str | tuple[str], int]:
    merged_reqs = dict()
    for req, amount in requirements1.items():
        if req not in merged_reqs:
            merged_reqs[req] = amount
            continue
        merged_reqs[req] = max(merged_reqs[req], amount)
    for req, amount in requirements2.items():
        if req not in merged_reqs:
            merged_reqs[req] = amount
            continue
        merged_reqs[req] = max(merged_reqs[req], amount)
    return merged_reqs


def set_combat_logic_entrance_rules(multiworld: MultiWorld, player: int, options: SilksongOptions) -> None:
    if options.combat_logic == CombatLogic.option_none:
        return
    pattern_suffix = " After Defeated"
    for entrance_name, entrance in multiworld.regions.entrance_cache[player].items():
        entrance_data = connections_by_name[entrance_name]
        destination = entrance_data.destination
        if not destination.endswith(pattern_suffix):
            continue

        boss_name = destination[0:-len(pattern_suffix)]
        if boss_name not in combat_logic_requirements:
            continue

        requirements = dict()
        if options.combat_logic >= CombatLogic.option_minimal and CombatLogic.option_minimal in combat_logic_requirements[boss_name]:
            requirements = merge_requirements(requirements, combat_logic_requirements[boss_name][CombatLogic.option_minimal])
        if options.combat_logic >= CombatLogic.option_usual and options.combat_logic != CombatLogic.option_nice_tools and CombatLogic.option_usual in combat_logic_requirements[boss_name]:
            requirements = merge_requirements(requirements, combat_logic_requirements[boss_name][CombatLogic.option_usual])
        if options.combat_logic >= CombatLogic.option_nice_tools and CombatLogic.option_nice_tools in combat_logic_requirements[boss_name]:
            requirements = merge_requirements(requirements, combat_logic_requirements[boss_name][CombatLogic.option_nice_tools])
        if options.combat_logic >= CombatLogic.option_skill_issue and CombatLogic.option_skill_issue in combat_logic_requirements[boss_name]:
            requirements = merge_requirements(requirements, combat_logic_requirements[boss_name][CombatLogic.option_skill_issue])

        if requirements:
            for requirement, amount in requirements.items():
                add_rule(entrance, lambda state, req=requirement, player=player, count=amount: has_requirement(state, req, player, count))
