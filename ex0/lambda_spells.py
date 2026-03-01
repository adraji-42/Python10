from typing import List, Dict, Union

Artifact = Dict[str, Union[str, int]]
Mage = Dict[str, Union[str, int]]


def artifact_sorter(artifacts: List[Artifact]) -> List[Artifact]:
    """Sorts a list of artifacts by power in descending order.

    Args:
        artifacts: A list of dictionaries representing artifacts.
            Each dictionary must contain a 'power' key (int).

    Returns:
        A new list of artifacts sorted by power (descending).
    """
    return sorted(
        artifacts,
        key=lambda x: (x.get("power", 0), x.get("name", "Unknown")),
        reverse=True
    )


def power_filter(mages: List[Mage], min_power: int) -> List[Mage]:
    """Filters mages based on a minimum power level.

    Args:
        mages: A list of dictionaries representing mages.
            Each dictionary must contain a 'power' key (int).
        min_power: The minimum power required.

    Returns:
        A list of mages who meet the power requirement.
    """
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: List[str]) -> List[str]:
    """Transforms spell names by adding asterisks.

    Args:
        spells: A list of spell names (strings).

    Returns:
        A list of transformed strings in the format '* spell *'.
    """
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: List[Mage]) -> Dict[str, Union[int, float]]:
    """Calculates statistics for a group of mages.

    Args:
        mages: A list of dictionaries representing mages.
            Each dictionary must contain a 'power' key (int).

    Returns:
        A dictionary containing 'max_power', 'min_power', and 'avg_power'.
    """
    powers = list(map(lambda x: x["power"], mages))

    return {
        "max_power": max(powers),
        "min_power": min(powers),
        "avg_power": round(sum(powers) / len(powers), 2)
    }


def main() -> None:
    """Executes the test cases for the module functions."""
    test_artifacts: List[Artifact] = [
        {"name": "Crystal Orb", "power": None, "type": "tool"},
        {"name": "Fire Staff", "power": 92, "type": "weapon"},
        {"name": "Wooden Wand", "power": 15, "type": "weapon"}
    ]

    test_spells: List[str] = ["fireball", "heal", "shield"]

    test_mages: List[Mage] = [
        {"name": "Merlin", "power": 90, "element": "magic"},
        {"name": "Gandalf", "power": 100, "element": "light"},
        {"name": "Apprentice", "power": 10, "element": "none"}
    ]

    print("Testing artifact sorter...")
    try:
        sorted_artifacts = artifact_sorter(test_artifacts)
    except Exception as e:
        print(f"Error type: {e.__class__.__name__}: {e}")
    else:
        print(" comes before ".join([
                    f"{a.get('name', 'Unknown')} ({a.get('power', 0)} power)"
                    for a in sorted_artifacts
                ]))

    print("\nTesting spell transformer...")
    try:
        transformed_spells = spell_transformer(test_spells)
    except Exception as e:
        print(f"Error type: {e.__class__.__name__}: {e}")
    else:
        print(*transformed_spells)

    print("\nTesting mage stats...")
    try:
        stats = mage_stats(test_mages)
    except Exception as e:
        print(f"Error type: {e.__class__.__name__}: {e}")
    else:
        print(f"Stats: {stats}")


if __name__ == "__main__":
    main()
