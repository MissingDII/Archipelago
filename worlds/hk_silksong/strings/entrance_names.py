all_entrance_names = []


def entrance(name: str) -> str:
    all_entrance_names.append(name)
    return name


class EntranceName:
    spawn_moss_grotto = entrance("Spawn in Moss Grotto")
