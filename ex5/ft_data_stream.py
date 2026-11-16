import random
import typing

PLAYERS = ["bob", "alice", "dylan", "charlie", "chris", "nico"]
ACTIONS = [
    "run",
    "eat",
    "sleep",
    "grab",
    "move",
    "climb",
    "code",
    "swim",
]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(PLAYERS), random.choice(ACTIONS))


def consume_event(
    event_list: list[tuple[str, str]],
) -> typing.Generator[tuple[str, str], None, None]:
    while event_list:
        idx = random.randint(0, len(event_list) - 1)
        item = event_list.pop(idx)
        yield item


def ft_data_stream() -> None:
    print("=== Game Data Stream Processor ===")
    events = gen_event()
    for i in range(1000):
        player, action = next(events)
        print(f"Event {i}: Player {player} did action {action}")

    event_list: list[tuple[str, str]] = []
    for _ in range(10):
        player, action = next(events)
        event_list.append((player, action))
    print(f"Built list of 10 events: {event_list}")
    for item in consume_event(event_list):
        print(f"Got event from list: {item}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    ft_data_stream()
