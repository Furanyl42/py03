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
        index = 1
        for arg in total_args:
            print(f"Argument {index}: {arg}")
            index += 1

    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    ft_command_quest()
