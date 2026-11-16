import sys


def parse_args() -> dict[str, int]:
    dict_args: dict[str, int] = {}
    for arg in sys.argv[1:]:
        if arg.count(":") != 1:
            print(f"Error - invalid parameter '{arg}'")
            continue

        key, raw_value = arg.split(":")
        if not key:
            print(f"Error - invalid parameter '{arg}'")
            continue
        if key in dict_args:
            print(f"Redundant item '{key}' - discarding")
            continue
        try:
            dict_args[key] = int(raw_value)
        except ValueError as e:
            print(f"Quantity error for '{key}': {e}")
    return dict_args


def get_minmax_dict(
    dico: dict[str, int],
) -> tuple[tuple[str, int], tuple[str, int]] | None:
    max_key = ""
    max_value = 0
    min_key = ""
    min_value = 0
    first = True
    for key in dico.keys():
        value = dico[key]
        if first:
            max_key = key
            max_value = value
            min_key = key
            min_value = value
            first = False
            continue
        if value > max_value:
            max_key = key
            max_value = value
        if value < min_value:
            min_key = key
            min_value = value
    if first:
        return None
    return ((max_key, max_value), (min_key, min_value))


def ft_inventory_system() -> None:
    print("=== Inventory System Analysis ===")
    inventory = parse_args()
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    total_quantity = sum(inventory.values())
    print(
        f"Total quantity of the {len(inventory.keys())} items: "
        f"{total_quantity}"
    )
    for key in inventory.keys():
        quantity = inventory[key]
        percentage = 0.0
        if total_quantity:
            percentage = round(100 * quantity / total_quantity, 1)
        print(f"Item {key} represents {percentage}%")

    minmax = get_minmax_dict(inventory)
    if minmax is not None:
        ((max_key, max_value), (min_key, min_value)) = minmax
        print(f"Item most abundant: {max_key} with quantity {max_value}")
        print(f"Item least abundant: {min_key} with quantity {min_value}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    ft_inventory_system()
