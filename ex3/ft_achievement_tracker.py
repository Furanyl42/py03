import random

ACHIEVEMENTS = [
    "Crafting Genius",
    "World Savior",
    "Master Explorer",
    "Collector Supreme",
    "Untouchable",
    "Boss Slayer",
    "Strategist",
    "Speed Runner",
    "Survivor",
    "Treasure Hunter",
    "First Steps",
    "Sharp Mind",
    "Unstoppable",
]


def gen_player_achievements(achievements: list[str]) -> set[str]:
    nbr = random.randint(1, len(achievements))
    sample = random.sample(achievements, nbr)
    return set(sample)


def ft_achievement_tracker() -> None:
    player_names = ["Alice", "Bob", "Charlie", "Dylan"]
    player_sets: dict[str, set[str]] = {
        name: gen_player_achievements(ACHIEVEMENTS) for name in player_names
    }

    print("=== Achievement Tracker System ===\n")
    for name, achievements in player_sets.items():
        print(f"Player {name}: {achievements}")
    print()
    all_achievements = set(ACHIEVEMENTS)
    distinct_ach = set.union(*player_sets.values())
    common_ach = set.intersection(*player_sets.values())
    print(f"All distinct achievements: {distinct_ach}\n")
    print(f"Common achievements: {common_ach}\n")
    for name, achievements in player_sets.items():
        other_sets = [
            other for player, other in player_sets.items() if player != name
        ]
        other_ach_unioned = set.union(*other_sets)
        exclu = set.difference(achievements, other_ach_unioned)
        print(f"Only {name} has: {exclu}")
    print()
    for name, achievements in player_sets.items():
        missing = set.difference(all_achievements, achievements)
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    ft_achievement_tracker()
