# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_achievement_tracker.py                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: nide-wil <nide-wil@student.42belgium.be>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/11/13 16:44:51 by nide-wil          #+#    #+#              #
#    Updated: 2026/11/13 16:54:04 by nide-wil         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

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


def gen_rand_achievements(achievements: list[str]) -> set[str]:
    nbr = random.randint(1, len(achievements))
    sample = random.sample(achievements, nbr)
    return set(sample)


def ft_achievement_tracker():
    player_names = ["Alice", "Bob", "Charlie", "Dylan"]
    player_sets: dict[str, set[str]] = {
        name: gen_rand_achievements(ACHIEVEMENTS) for name in player_names
    }

    print("=== Achievement Tracker System ===\n")
    for name, achievements in player_sets.items():
        print(f"Player {name}: {achievements}")
    print()
    all_achievements = set(ACHIEVEMENTS)
    sets_list = list(player_sets.values())
    distinct_ach = set.union(*sets_list)
    common_ach = set.intersection(*sets_list)
    print(f"All distinct achievements: {distinct_ach}\n")
    print(f"Common achievements: {common_ach}\n")
    for name, achievements in player_sets.items():
        other_ach = [ach for others, ach in player_sets.items() if others != name]
        other_ach_unioned = set.union(*other_ach)
        exclu = achievements.difference(other_ach_unioned)
        print(f"Only {name} has {exclu}")
    print()
    for name, achievements in player_sets.items():
        missing = achievements.difference(all_achievements)
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    ft_achievement_tracker()
