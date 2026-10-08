#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, plant_age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.plant_age = plant_age

    def show(self) -> None:
        print("=== Garden Plant Growth ===")
        for day in range(1, 8):
            print(f"=== Day {day} ===")
            print(f"{self.name}: {self.height}cm, {self.plant_age} days old")
            self.__grow()
            self.__age()

    def __grow(self) -> None:
        self.height += 0.8

    def __age(self) -> None:
        self.plant_age += 1


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")

    rose: Plant = Plant("Rose", 25, 30)
    rose.show()

    sunflower: Plant = Plant("Sunflower", 80, 45)
    sunflower.show()

    cactus: Plant = Plant("Cactus", 15, 120)
    cactus.show()
