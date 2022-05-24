from link import indicate_thunderstorm, setup, set_low
from weather import get_current_condition


def main():
    setup()
    current = get_current_condition()

    # Set everything back to low
    set_low()
    
    if current == 'Thunderstorm':
        indicate_thunderstorm()

if __name__ == '__main__':
    main()
