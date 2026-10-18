import random


def no_colorsc():
    """Generate a random color in hexadecimal format."""
    color_value = random.randrange(0x1000000)
    hex_color = format(color_value, "06X")
    return "#" + hex_color


def main():
    color = no_colorsc()
    print(color)


if __name__ == "__main__":
    main()
