import datetime as dt

from link import indicate_on, indicate_off, indicate_thunderstorm, setup, set_low
from weather import get_current_condition

SALT_LAKE_CITY_TIME_OFFSET = -6
SLC_TZ_INFO = dt.timezone(dt.timedelta(hours=SALT_LAKE_CITY_TIME_OFFSET))

def in_between(now, start, end):
    """https://stackoverflow.com/a/33681543/1175701"""
    if start <= end:
        return start <= now < end
    else: # over midnight e.g., 23:30-04:15
        return start <= now or now < end

def main():
    setup()

    # If daytime, do the things
    if not in_between(now=dt.datetime.now(SLC_TZ_INFO).time(), start=dt.time(23), end=dt.time(7, 30)):
        indicate_on()
        current = get_current_condition()

        # Set everything back to low
        set_low()
        
        if current == 'Thunderstorm':
            indicate_thunderstorm()

    else:
        # Tell arduino the lights should be off
        indicate_off()


if __name__ == '__main__':
    main()
