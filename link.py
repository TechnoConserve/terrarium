# Communicate with the arduino controlling the lights using the GPIO pins
import atexit
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

THUNDERSTORM_GPIO_PIN = 16

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(THUNDERSTORM_GPIO_PIN, GPIO.OUT, initial=GPIO.LOW)
    
    atexit.register(exit_handler)

def indicate_thunderstorm():
    GPIO.output(THUNDERSTORM_GPIO_PIN, GPIO.HIGH)

def set_low():
    GPIO.output(THUNDERSTORM_GPIO_PIN, GPIO.LOW)

def exit_handler():
    GPIO.cleanup()
