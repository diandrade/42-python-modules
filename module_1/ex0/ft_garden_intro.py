#!/usr/bin/env python3

def message(name: str, height: float, age: int) -> None:
    print(f"Plant: {name}")
    print(f"Height {height}cm")
    print(f"Age: {age} days")


if __name__ == "__main__":
    name: str = "Rose"
    height: float = 25
    age: int = 30

    print("=== Welcome to My garden ===")
    message(name, height, age)
    print("\n=== End of Program ===")
