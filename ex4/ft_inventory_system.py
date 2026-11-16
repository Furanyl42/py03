import sys


def parse_args() -> dict[str, int]:
    dict_args = {}
    for arg in sys.argv[1:]:
        if not ":" in arg:
            print(f"Error - invalid parameter {arg}")
            continue

        if ":" in arg:
            key = arg.split(":")[0]
            value = arg.split(":")[1]
            if key in dict_args:
                print(f"Redundant item {key} - discarding")
                continue
            try:
                value = int(value)
                dict_args[key] = value
            except ValueError as e:
                print(f"Quantity error for {key}: {e}")
    return dict_args


def get_minmax_dict(dico: dict[str, int]) -> ((str, int), (str, int)):
    max_key = None
    max_value = None
    min_key = None
    min_value = None
    for key in dico.keys():
        value = dico[key]
        if max_value is None or value > max_value:
            max_key = key
            max_value = value
        if min_value is None or value < min_value:
            min_key = key
            min_value = value
    return ((max_key, max_value), (min_key, min_value))


def ft_inventory_system() -> None:
    inventory = parse_args()
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    print(
        f"Total quantity of the {len(inventory.keys())} items: {sum(inventory.values())}"
    )
    for key, value in inventory.items():
        print(
            f"Item {key} represents {round(100 * value / sum(inventory.values()), 1)}%"
        )

    ((max_key, max_value), (min_key, min_value)) = get_minmax_dict(inventory)
    print(f"Item most abundant: {max_key} with quantity {max_value}")
    print(f"Item least abundant: {min_key} with quantity {min_value}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    ft_inventory_system()
