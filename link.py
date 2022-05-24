# Communicate with the arduino controlling the lights using the GPIO pins
import atexit
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

THUNDERSTORM_GPIO_PIN = 16
ON_OFF_PIN = 23  # Tell arduino if lights should be on or off

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(THUNDERSTORM_GPIO_PIN, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(ON_OFF_PIN, GPIO.OUT, initial=GPIO.HIGH)
    
    atexit.register(exit_handler)

def indicate_thunderstorm():
    GPIO.output(THUNDERSTORM_GPIO_PIN, GPIO.HIGH)

def indicate_off():
    GPIO.output(ON_OFF_PIN, GPIO.LOW)

def indicate_on():
    GPIO.output(ON_OFF_PIN, GPIO.HIGH)

def set_low():
    """Set weather indicators to LOW"""
    GPIO.output(THUNDERSTORM_GPIO_PIN, GPIO.LOW)

def exit_handler():
    GPIO.cleanup()
