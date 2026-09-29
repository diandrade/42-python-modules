def ft_count_harvest_recursive(days_until_harvest: int | None = None) -> None:
    if days_until_harvest is None:
        days_until_harvest: int = int(input("Days until harvest: "))
        ft_count_harvest_recursive(days_until_harvest)
        print("Harvest time!")
        return

    if days_until_harvest > 0:
        ft_count_harvest_recursive(days_until_harvest - 1)
        print(f"Day {days_until_harvest}")


if __name__ == "__main__":
    ft_count_harvest_recursive()
