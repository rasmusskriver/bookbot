import sys
from stats import the_last


def main():
    if len(sys.argv) == 2:
        print("true")
        secund_argument = sys.argv[1]
        return the_last(secund_argument)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


main()
