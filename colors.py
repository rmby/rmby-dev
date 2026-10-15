import random


def generate_random_hex_color():
    """Generate a random color in hexadecimal format."""
    color_value = random.randrange(0x1000000)
    hex_color = format(color_value, "06X")
    return "#" + hex_color


def main():
    color = generate_random_hex_color()
    print(color)


if __name__ == "__main__":
    main()
