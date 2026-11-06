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

    def grow(self, amount: float = 0.8) -> None:
        self._height += amount

    def age(self, days: int = 1) -> None:
        self._age += days

    def show(self) -> None:
        print(
            f"{self.name}: "
            f"{self.get_height():.1f}cm, {self.get_age()} days old"
        )


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int,
                 color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        self.is_blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.is_blooming:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.get_height():.1f}cm long and "
            f"{self.trunk_diameter}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0.0

    def grow(self, amount: float = 0.8) -> None:
        super().grow(amount)
        self.nutritional_value += 0.5

    def age(self, days: int = 1) -> None:
        super().age(days)
        self.nutritional_value += 0.5 * days

    def grow_and_age(self, size: float, days: int) -> None:
        print(f"[make {self.name.lower()} grow and age for {days} days]")
        for _ in range(days):
            self.grow(size)
            self.age()

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {round(self.nutritional_value)}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose: Flower = Flower("rose", 15, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("=== Tree")
    oak: Tree = Tree("oak", 200, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("=== Vegetable")
    tomato: Vegetable = Vegetable("tomato", 5, 10, "April")
    tomato.show()
    tomato.grow_and_age(2.1, 20)
    tomato.show()
