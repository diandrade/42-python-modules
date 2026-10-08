#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")

    rose: Plant = Plant("Rose", 25, 30)
    rose.show()

    sunflower: Plant = Plant("Sunflower", 80, 45)
    sunflower.show()

    cactus: Plant = Plant("Cactus", 15, 120)
    cactus.show()
