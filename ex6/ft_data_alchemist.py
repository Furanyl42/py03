import random

RAW_LIST = [
    "Alice",
    "bob",
    "Charlie",
    "dylan",
    "Emma",
    "Gregory",
    "john",
    "kevin",
    "Liam",
]


def ft_data_alchemist() -> None:
    list_capitalized = [name.capitalize() for name in RAW_LIST]
    list_had_capital = [name for name in RAW_LIST if name.capitalize() == name]
    dict_capitalized = {name: random.randint(0, 1000) for name in list_capitalized}
    average = round(sum(dict_capitalized.values()) / len(dict_capitalized), 2)
    high_dict = {
        name: score for name, score in dict_capitalized.items() if score > average
    }
    print(f"Initial list of players: {RAW_LIST}")
    print(f"New list with all names capitalized: {list_capitalized}")
    print(f"New list of capitalized names only: {list_had_capital}\n")
    print(f"Score dict: {dict_capitalized}")
    print(f"Score average is {average}")
    print(f"High scores: {high_dict}")


if __name__ == "__main__":
    ft_data_alchemist()
