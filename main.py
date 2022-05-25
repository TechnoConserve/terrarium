import datetime as dt
import logging

from link import indicate_on, indicate_off, indicate_thunderstorm, setup, set_low
from weather import get_current_condition

SALT_LAKE_CITY_TIME_OFFSET = -6
SLC_TZ_INFO = dt.timezone(dt.timedelta(hours=SALT_LAKE_CITY_TIME_OFFSET))

logging.basicConfig(
    filename='terrarium_main.log', 
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p %Z'
    )

logger = logging.getLogger(__name__)


def in_between(now, start, end):
    """https://stackoverflow.com/a/33681543/1175701"""
    if start <= end:
        return start <= now < end
    else: # over midnight e.g., 23:30-04:15
        return start <= now or now < end

def main():
    setup()

    current_time = dt.datetime.now(SLC_TZ_INFO).time()
    logger.debug(f'Current time: {current_time}')

    # If daytime, do the things
    if not in_between(now=current_time, start=dt.time(23), end=dt.time(7, 30)):
        logger.debug('It is daytime.')
        indicate_on()
        current = get_current_condition()

        logger.debug(f'Current weather condition: {current}')

        # Set everything back to low
        set_low()
        
        if current == 'Thunderstorm':
            logger.debug('Indicating a thunderstorm...')
            indicate_thunderstorm()

    else:
        logger.debug('It is nighttime.')
        # Tell arduino the lights should be off
        indicate_off()


if __name__ == '__main__':
    logger.debug('Starting script...')
    main()
    logger.debug('...ending script.')
