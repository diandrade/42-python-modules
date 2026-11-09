def main() -> None:
    ft_first_exception()


def ft_first_exception() -> None:
    print("=== Garden Temperature ===\n")
    test_temperature()
    print("All tests completed - program didn't crash!")


def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def display_temperature(temperature: int) -> None:
    print(f"Temperature is now {temperature}°C\n")


def test_temperature() -> None:
    test_1: str = "25"
    test_2: str = "abc"

    try:
        print(f"Input data is '{test_1}'")
        display_temperature(input_temperature(test_1))
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")

    try:
        print(f"Input data is '{test_2}'")
        display_temperature(input_temperature(test_2))
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")


if __name__ == "__main__":
    main()
