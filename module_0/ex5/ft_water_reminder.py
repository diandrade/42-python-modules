def ft_water_reminder() -> None:
    last_watering: int = int(input("Days since last watering: "))

    if last_watering > 2:
        print("Water the plants!")
    else:
        print("Plants are fine.")


if __name__ == "__main__":
    ft_water_reminder()
