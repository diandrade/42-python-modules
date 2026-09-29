def ft_harvest_total() -> None:
    day_1_harvest: int = int(input("Day 1 harvest: "))
    day_2_harvest: int = int(input("Day 2 harvest: "))
    day_3_harvest: int = int(input("Day 3 harvest: "))

    print(f"Total harvest: {day_1_harvest + day_2_harvest + day_3_harvest}")


if __name__ == "__main__":
    ft_harvest_total()
