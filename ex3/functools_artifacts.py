import operator
import functools
from typing import Callable, Dict, List, Any


def spell_reducer(spells: List[int], operation: str) -> int:
    """Reduces a list of spell powers using the specified operation.

    Args:
        spells: A list of integers representing spell powers.
        operation: A string indicating the operation.

    Returns:
        The final reduced integer value.
    """
    if operation == "add":
        return functools.reduce(operator.add, spells)
    if operation == "multiply":
        return functools.reduce(operator.mul, spells)
    if operation == "max":
        return functools.reduce(max, spells)
    if operation == "min":
        return functools.reduce(min, spells)
    raise ValueError(f"Invalid operation: {operation}")


def partial_enchanter(
    base_enchantment: Callable[[int, str, str], Any]
) -> Dict[str, Callable[[str], Any]]:
    """Creates specialized enchantment functions using partial application.

    Args:
        base_enchantment: The base callable to be partially applied.

    Returns:
        A dictionary of partially applied enchantment functions.
    """
    return {
        "fire_enchant": functools.partial(base_enchantment, 50, "fire"),
        "ice_enchant": functools.partial(base_enchantment, 50, "ice"),
        "lightning_enchant": functools.partial(
            base_enchantment, 50, "lightning"
        )
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Calculates the nth Fibonacci number using iteration and memoization.

    Args:
        n: The position in the Fibonacci sequence to calculate.

    Returns:
        The calculated Fibonacci number.

    Raises:
        ValueError: If n is a negative integer.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b

    return a


def spell_dispatcher() -> Callable:
    """Creates a single-dispatch spell system.

    Returns:
        A generic dispatcher function that handles different types.
    """

    @functools.singledispatch
    def dispatcher(arg: Any) -> str:
        return "Unknown spell type"

    @dispatcher.register
    def _(arg: int) -> str:
        return f"Damage spell: {arg} power"

    def _(arg: str) -> str:
        return f"Enchantment spell: {arg}"

    def _(arg: List) -> str:
        return f"Multi-cast spell: {len(arg)} targets"

    return dispatcher


def main() -> None:
    """Executes the test cases for the module functions."""
    test_spells: List[int] = [10, 20, 30, 40]
    op = {
        "Min": "min",
        "Max": "max",
        "Sum": "add",
        "Product": "multiply"
    }

    print("\nTesting spell reducer...")
    try:
        for k, v in op.items():
            print(f"{k}: {spell_reducer(test_spells, v)}")
    except Exception as e:
        print(f"Error type: {e.__class__.__name__}: {e}")

    test_fib = [10, 15]
    print("\nTesting memoized fibonacci...")
    try:
        for i in test_fib:
            print(f"Fib({i}): {memoized_fibonacci(i)}")
    except Exception as e:
        print(f"Error type: {e.__class__.__name__}: {e}")


if __name__ == "__main__":
    main()
