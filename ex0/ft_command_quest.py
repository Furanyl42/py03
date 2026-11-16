import sys


def ft_command_quest() -> None:
    print("=== Command Quest ===")
    name = sys.argv[0]
    total_args = sys.argv[1:]

    print(f"Program name: {name}")
    if not total_args:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(total_args)}")
        for i, arg in enumerate(total_args, start=1):
            print(f"Argument {i}: {arg}")

    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    ft_command_quest()
