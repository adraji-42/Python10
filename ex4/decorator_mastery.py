import time
import random
import inspect
import functools
from typing import Callable, Optional, Any


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    """Times the execution of a function safely.

    Args:
        func: The function to be timed.

    Returns:
        The wrapped function preserving original metadata and result.
    """
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start_t = time.perf_counter()
        try:
            result = func(*args, **kwargs)
            return result
        finally:
            end_t = time.perf_counter()
            print(f"Spell completed in {end_t - start_t:.3f} seconds")

    return wrapper


def power_validator(
    min_power: int | float
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Creates a decorator to validate power levels in arguments.

    Args:
        min_power: The minimum required power level to execute the function.

    Returns:
        A decorator that wraps a function to check its 'power' argument.

    Raises:
        TypeError: If min_power is not an integer or float.
    """
    if not isinstance(min_power, (int, float)):
        raise TypeError("min_power must be an int or float")

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            sig = inspect.signature(func)
            try:
                bound_args = sig.bind(*args, **kwargs)
                bound_args.apply_defaults()
                power_val = bound_args.arguments.get("power")
            except TypeError:
                return "Invalid arguments for this spell"

            if isinstance(power_val, (int, float)) and power_val >= min_power:
                return func(*args, **kwargs)

            return "Insufficient power for this spell"

        return wrapper
    return decorator


def retry_spell(
    max_attempts: int
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Creates a decorator that retries a function upon raising an exception.

    Args:
        max_attempts: The maximum number of execution attempts.

    Returns:
        A decorator that retries the wrapped function.

    Raises:
        ValueError: If max_attempts is less than or equal to 0.
    """
    if max_attempts <= 0:
        raise ValueError("max_attempts must be greater than 0")

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception: Optional[Exception] = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(
                        f"Spell failed, retrying... "
                        f"(attempt {attempt}/{max_attempts})"
                    )

            if last_exception is not None:
                raise last_exception

            raise RuntimeError("Unexpected failure in retry_spell")

        return wrapper
    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: Any) -> bool:
        """Validates a mage's name based on length and character types.

        Args:
            name: The name string to validate.

        Returns:
            True if valid, False otherwise.
        """
        if not isinstance(name, str):
            return False
        return len(name) >= 3 and name.replace(" ", "").isalpha()

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Casts a spell with the required power validation.

        Args:
            spell_name: The name of the spell.
            power: The amount of power used for the spell.

        Returns:
            A string indicating successful execution.
        """
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    """Executes the test cases for the module functions and classes."""
    @spell_timer
    def fireball() -> str:
        """Simulates casting a fireball spell."""
        time.sleep(random.random())
        return "Fireball cast!"

    print("\nTesting spell timer...")
    result = fireball()
    print(f"Result: {result}")

    guild = MageGuild()
    name_test: list[Any] = ["Merlin", "Harry Potter", "X", None, ["List"]]

    print("\nTesting MageGuild...")
    for name in name_test:
        try:
            print(f"Name validate '{name}': {guild.validate_mage_name(name)}")
        except Exception as e:
            print(f"Error type: {e.__class__.__name__}: {e}")

    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Ice Blast", 5))
    print(guild.cast_spell(spell_name="Fire", power=20))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error type: {e.__class__.__name__}: {e}")
