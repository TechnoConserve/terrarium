import os

from link import indicate_thunderstorm, setup
from weather import get_current_condition


def main():
    setup()
    current = get_current_condition()
    
    if current == 'Thunderstorm':
        indicate_thunderstorm()

if __name__ == '__main__':
    main()
