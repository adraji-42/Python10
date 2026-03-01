from typing import Callable, Tuple, List, Any


def spell_combiner(
    spell1: Callable[..., Any],
    spell2: Callable[..., Any]
) -> Callable[..., Tuple[Any, Any]]:
    """Combines two spells into one.

    Args:
        spell1: The first spell function.
        spell2: The second spell function.

    Returns:
        A new function that executes
        both spells and returns a tuple of results.
    """
    def combined_spell(*args: Any, **kwargs: Any) -> Tuple[Any, Any]:
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    return combined_spell


def power_amplifier(
    base_spell: Callable[..., int],
    multiplier: int
) -> Callable[..., int]:
    """Amplifies the power of a base spell.

    Args:
        base_spell: The spell function to be amplified.
        multiplier: The integer multiplier to apply.

    Returns:
        A new function that executes the base spell and multiplies its result.
    """
    def amplified_spell(*args: Any, **kwargs: Any) -> int:
        return base_spell(*args, **kwargs) * multiplier
    return amplified_spell


def conditional_caster(
    condition: Callable[..., bool],
    spell: Callable[..., Any]
) -> Callable[..., Any]:
    """Casts a spell conditionally.

    Args:
        condition: A function evaluating the condition to cast the spell.
        spell: The spell function to cast.

    Returns:
        A function that executes the spell if the condition is met,
        or returns the string 'Spell fizzled' otherwise.
    """
    def conditional_spell(*args: Any, **kwargs: Any) -> Any:
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return conditional_spell


def spell_sequence(
    spells: List[Callable[..., Any]]
) -> Callable[..., List[Any]]:
    """Creates a sequence of spells to be cast in order.

    Args:
        spells: A list of spell functions.

    Returns:
        A function that executes all spells and returns a list of results.
    """
    def sequential_spell(*args: Any, **kwargs: Any) -> List[Any]:
        return [s(*args, **kwargs) for s in spells]
    return sequential_spell


def main() -> None:
    """Executes the test cases for the module functions."""
    def fireball(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    def damage() -> int:
        return 10

    print("\nTesting spell combiner...")
    try:
        combined = spell_combiner(fireball, heal)
        res1, res2 = combined("Dragon")
    except Exception as e:
        print(f"Error type: {e.__class__.__name__}: {e}")
    else:
        print(f"Combined spell result: {res1}, {res2}")

    print("\nTesting power amplifier...")
    try:
        amplified = power_amplifier(damage, 3)
        orig = damage()
        amp = amplified()
    except Exception as e:
        print(f"Error type: {e.__class__.__name__}: {e}")
    else:
        print(f"Original: {orig}, Amplified: {amp}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error type: {e.__class__.__name__}: {e}")
