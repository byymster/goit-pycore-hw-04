import colorama
from sys import argv
from pathlib import Path


def parse_args() -> Path:
    arg = argv[1] if len(argv) == 2 else None
    if arg is None:
        raise ValueError("No arguments provided")
    path = Path(arg)
    if not path.is_dir():
        raise ValueError("Invalid directory path provided")

    return path


def generate_dir_tree(path: Path, prefix=""):
    try:
        for item in path.iterdir():
            if item.is_dir():
                print(f"{prefix}├── {colorama.Fore.BLUE}{item.name}{colorama.Style.RESET_ALL}")
                generate_dir_tree(item, prefix + "│   ")
            elif item.is_symlink():
                print(f"{prefix}├── {colorama.Fore.CYAN}{item.name}{colorama.Style.RESET_ALL}")
            elif item.is_file():
                print(f"{prefix}├── {colorama.Fore.GREEN}{item.name}{colorama.Style.RESET_ALL}")
            else:
                print(f"{prefix}├── {colorama.Fore.WHITE}{item.name}{colorama.Style.RESET_ALL}")
    except PermissionError:
        print(f"{prefix}├── {colorama.Fore.RED}{path.name}{colorama.Style.RESET_ALL} [Permission Denied]")


def main():
    try:
        path = parse_args()
        print(f"Directory tree for: {str(path)}")
        generate_dir_tree(path)
    except ValueError as e:
        print(str(e))
        return


if __name__ == "__main__":
    main()