#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, plant_age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.plant_age = plant_age

    def show(self) -> str:
        return (
            f"{self.name}: "
            f"{self.height:.1f}cm, {self.plant_age} days old"
        )

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.plant_age += 1


if __name__ == "__main__":
    plants = [
        Plant("rose", 25.0, 30),
        Plant("oak", 200.0, 365),
        Plant("cactus", 5.0, 90),
        Plant("sunflower", 80.0, 45),
        Plant("fern", 15.0, 60)]

    print("=== Plant Factory Output ===")
    for plant in plants:
        print(f"Created: {plant.show()}")
