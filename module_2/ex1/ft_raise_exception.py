#!/usr/bin/env python3

def main() -> None:
    ft_raise_exception()


def ft_raise_exception() -> None:
    print("=== Garden Temperature ===\n")
    test_temperature()


def input_temperature(temp_str: str) -> int:
    temperature: int = int(temp_str)

    if temperature < 0:
        raise ValueError(f"{temperature}°C is too cold for plants (min 0°C)")
    elif temperature > 40:
        raise ValueError(f"{temperature}°C is too hot for plants (max 40°C)")
    return temperature


def display_temperature(temperature: int) -> None:
    print(f"Temperature is now {temperature}°C\n")


def test_temperature() -> None:
    tests: list[str] = ["25", "abc", "100", "-50"]

    try:
        print(f"Input data is '{tests[0]}'")
        display_temperature(input_temperature(tests[0]))
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")

    try:
        print(f"Input data is '{tests[1]}'")
        display_temperature(input_temperature(tests[1]))
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")

    try:
        print(f"Input data is '{tests[2]}'")
        display_temperature(input_temperature(tests[2]))
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")

    try:
        print(f"Input data is '{tests[3]}'")
        display_temperature(input_temperature(tests[3]))
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
