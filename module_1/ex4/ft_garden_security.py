#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self._height = 0.0
        self._age = 0
        if self._is_valid_height(height):
            self._height = height
        if self._is_valid_age(age):
            self._age = age
        print(f"Plant created: {self.show()}")

    def _is_valid_height(self, height: float) -> bool:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            return False
        return True

    def _is_valid_age(self, age: int) -> bool:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            return False
        return True

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> None:
        if not self._is_valid_height(height):
            print("Height update rejected")
            return
        self._height = height
        print(f"Height updated: {self.get_height()}cm")

    def set_age(self, age: int) -> None:
        if not self._is_valid_age(age):
            print("Age update rejected")
            return
        self._age = age
        print(f"Age updated: {self.get_age()} days")

    def show(self) -> str:
        return (
            f"{self.name}: "
            f"{self.get_height():.1f}cm, {self.get_age()} days old"
        )

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.plant_age += 1


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose: Plant = Plant("rose", 15, 10)
    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-5)
    rose.set_age(-3)
    print(f"Current state: {rose.show()}")
