import sys


def process_args() -> list[int]:
    total_args = sys.argv[1:]
    scores = list[int]
    for arg in total_args:
        try:
            scores.append(int(arg))
        except ValueError:

def ft_score_analytics() -> None:

