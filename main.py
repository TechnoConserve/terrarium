import os

from weather import get_current_condition


def main():
    current = get_current_condition()
    print(current)

if __name__ == '__main__':
    main()
