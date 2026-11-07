from math import pi


def circle_area(r):
    if type(r) not in (int, float):
        raise TypeError("Promień musi być liczbą rzeczywistą (int lub float).")
    if r < 0:
        raise ValueError("Promień nie może być ujemny.")
    return pi * r ** 2


if __name__ == "__main__":
    for r in (0, 1, 2.5, 10):
        print(f"r = {r} -> pole = {circle_area(r):.4f}")
