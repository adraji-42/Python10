from typing import Callable, Dict, Any


def mage_counter() -> Callable[[], int]:
    """Creates a counter function that remembers its state.

    Returns:
        A function that returns an incrementing integer on each call.
    """
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    """Creates an accumulator function for spell power.

    Args:
        initial_power: The starting power level.

    Returns:
        A function that takes an integer, adds it to the total,
        and returns the new total.
    """
    total_power = initial_power

    def accumulator(added_power: int) -> int:
        nonlocal total_power
        total_power += added_power
        return total_power

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    """Creates a function that applies a specific enchantment to items.

    Args:
        enchantment_type: The type of enchantment to apply.

    Returns:
        A function that takes an item name
        and returns the enchanted item string.
    """
    def enchanter(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchanter


def memory_vault() -> Dict[str, Callable[..., Any]]:
    """Creates a private memory vault with store and recall capabilities.

    Returns:
        A dictionary containing 'store' and 'recall' functions.
    """
    vault: Dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        vault[key] = value

    def recall(key: str) -> Any:
        return vault.get(key, "Memory not found")

    return {
        "store": store,
        "recall": recall
    }


def main() -> None:
    """Executes the test cases for the module functions."""
    print("\nTesting mage counter...")
    counter = mage_counter()
    for i in range(1, 4):
        if i > 3:
            print("...")
            break
        print(f"Call {i}: {counter()}")

    print("\nTesting enchantment factory...")
    fire_enchant = enchantment_factory("Flaming")
    ice_enchant = enchantment_factory("Frozen")
    print(fire_enchant("Sword"))
    print(ice_enchant("Shield"))


if __name__ == "__main__":
    main()
