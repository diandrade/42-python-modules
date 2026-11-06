#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self._height = 0.0
        self._age = 0
        self._stats = self._statistics()
        if self._is_valid_height(height):
            self._height = height
        if self._is_valid_age(age):
            self._age = age

    class _statistics():
        def __init__(self) -> None:
            self._grow_counter = 0
            self._age_counter = 0
            self._show_counter = 0

        def increment_grow(self) -> None:
            self._grow_counter += 1

        def increment_age(self) -> None:
            self._age_counter += 1

        def increment_show(self) -> None:
            self._show_counter += 1

        def display(self) -> None:
            print(f"Stats: {self._grow_counter} grow, "
                  f"{self._age_counter} age, "
                  f"{self._show_counter} show")

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        if age > 365:
            return True
        return False

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

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

    def grow(self, amount: float = 30) -> None:
        self._height += amount
        self._stats.increment_grow()

    def age(self, days: int = 20) -> None:
        self._age += days
        self._stats.increment_age()

    def show(self) -> None:
        print(
            f"{self.name}: "
            f"{self.get_height():.1f}cm, {self.get_age()} days old"
        )
        self._stats.increment_show()

    def show_stats(self) -> None:
        self._stats.display()


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
    class _statistics(Plant._statistics):
        def __init__(self) -> None:
            super().__init__()
            self._shade_counter = 0

        def increment_shade(self) -> None:
            self._shade_counter += 1

        def display(self) -> None:
            super().display()
            print(f"{self._shade_counter} shade")

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
        self._stats.increment_shade()

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


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int,
                 color: str) -> None:
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")


def display_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.show_stats()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> "
          f"{Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> "
          f"{Plant.is_older_than_year(400)}")

    print("=== Flower")
    rose = Flower("rose", 15, 10, "red")
    rose.show()
    display_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8)
    rose.bloom()
    rose.show()
    display_statistics(rose)

    print("=== Tree")
    oak = Tree("oak", 200, 365, 5.0)
    oak.show()
    display_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_statistics(oak)

    print("=== Seed")
    sunflower = Seed("sunflower", 80, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_statistics(sunflower)

    print("=== Anonymous")
    unknown = Plant.anonymous()
    unknown.show()
    display_statistics(unknown)
