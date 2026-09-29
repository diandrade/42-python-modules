def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        print(f"{seed_type} seeds: {quantity} packets available")
    elif unit == "grams":
        print(f"{seed_type} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{seed_type} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")


menu = """Select the unit:
1 - Packets
2 - Grams
3 - Area
: """

if __name__ == "__main__":
    units = ["packets", "grams", "area"]

    seed_type = input("Seed type: ")
    quantity = input("Quantity of seeds: ")
    code = int(input(menu))

    unit: str

    match code:
        case 1:
            unit = units[0]
        case 2:
            unit = units[1]
        case 3:
            unit = units[2]
        case _:
            print("Select a valid code.")
            exit()

    ft_seed_inventory(seed_type, quantity, unit)
