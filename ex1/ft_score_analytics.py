import sys


def process_args() -> list[int]:
    total_args = sys.argv[1:]
    scores: list[int] = []
    for arg in total_args:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    return scores


def get_total_score(scores: list[int]) -> int:
    total_score = 0
    for score in scores:
        total_score += score
    return total_score


def get_minmax_score(scores: list[int]) -> tuple[int, int]:
    return (max(scores), min(scores))


def ft_score_analytics() -> None:
    scores = process_args()
    total_players = len(scores)
    if not scores:
        print("No scores provided.", end=" ")
        print(f"Usage: python3 {sys.argv[0]} <score1> <score2> ...")
        return
    total_score = get_total_score(scores)
    high_score, low_score = get_minmax_score(scores)
    score_range = high_score - low_score
    average_score = total_score / total_players

    print("=== Player Score Analytics ===")
    print(f"Scores processed: {scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    ft_score_analytics()
