def ft_plot_area() -> None:
    garden_length: int = int(input("Enter length: "))
    garden_width: int = int(input("Enter width: "))

    print(f"Plot area: {garden_length * garden_width}")


if __name__ == "__main__":
    ft_plot_area()
