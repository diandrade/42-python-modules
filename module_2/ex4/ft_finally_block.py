#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def main() -> None:
    ft_finally_block()


def ft_finally_block() -> None:
    test_watering_system()


def valid_plants() -> None:
    print("Testing valid plants...")
    print("Opening watering system")

    try:
        water_plant("Tomato")
    except PlantError as e:
        print(f"Caught PlantError : {e}")
        print(".. ending tests and returning to main")
        return

    try:
        water_plant("Lettuce")
    except PlantError as e:
        print(f"Caught PlantError : {e}")
        print(".. ending tests and returning to main")
        return

    try:
        water_plant("Carrots")
    except PlantError as e:
        print(f"Caught PlantError : {e}")
        print(".. ending tests and returning to main")
        return


def invalid_plants() -> None:
    print("Testing invalid plants...")
    print("Opening watering system")

    try:
        water_plant("Tomato")
    except PlantError as e:
        print(f"Caught PlantError : {e}")
        print(".. ending tests and returning to main")
        return

    try:
        water_plant("lettuce")
    except PlantError as e:
        print(f"Caught PlantError : {e}")
        print(".. ending tests and returning to main")
        return

    try:
        water_plant("Carrots")
    except PlantError as e:
        print(f"Caught PlantError : {e}")
        print(".. ending tests and returning to main")
        return


def test_watering_system() -> None:
    print("=== Garden Watering System ===")

    try:
        try:
            valid_plants()
        finally:
            print("Closing watering system\n")

        try:
            invalid_plants()
        finally:
            print("Closing watering system\n")
    finally:
        print("Cleanup always happens, even with errors!")


def water_plant(plant_name: str) -> None:
    if is_capitalized(plant_name):
        print(f"Watering {plant_name}: [OK]")
        return
    raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def is_capitalized(value: str) -> bool:
    if value[:1] == value.capitalize()[:1]:
        return True
    return False


if __name__ == "__main__":
    main()
