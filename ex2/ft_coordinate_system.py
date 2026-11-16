import math


def get_distance(
    p1: tuple[float, float, float], p2: tuple[float, float, float]
) -> float:
    (x1, y1, z1) = p1
    (x2, y2, z2) = p2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    return distance


def get_player_pos() -> tuple[float, float, float]:
    prompt = "Enter new coordinates as floats in format 'x,y,z': "
    while True:
        raw_input = input(prompt)
        parts = raw_input.split(",")

        if len(parts) != 3:
            print("Invalid syntax")
            continue
        coords: list[float] = []
        error = False
        for p in parts:
            try:
                coords.append(float(p))
            except ValueError as e:
                print(f"Error on parameter '{p}': {e}")
                error = True
                break
        if error:
            continue
        return (coords[0], coords[1], coords[2])


def ft_coordinate_system() -> None:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    x1, y1, z1 = get_player_pos()
    print(f"Got a first tuple: ({x1}, {y1}, {z1})")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    distance_center = round(get_distance((x1, y1, z1), (0.0, 0.0, 0.0)), 4)
    print(f"Distance to center: {distance_center}")
    print("Get a second set of coordinates")
    x2, y2, z2 = get_player_pos()
    distance = round(get_distance((x1, y1, z1), (x2, y2, z2)), 4)
    print(f"Distance between the 2 sets of coordinates: {distance}")


if __name__ == "__main__":
    ft_coordinate_system()
