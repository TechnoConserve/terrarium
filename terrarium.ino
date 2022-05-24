// Simple strand test for Adafruit Dot Star RGB LED strip.
// This is a basic diagnostic tool, NOT a graphics demo...helps confirm
// correct wiring and tests each pixel's ability to display red, green
// and blue and to forward data down the line.  By limiting the number
// and color of LEDs, it's reasonably safe to power a couple meters off
// the Arduino's 5V pin.  DON'T try that with other code!

#include <Adafruit_DotStar.h>
// Because conditional #includes don't work w/Arduino sketches...
#include <SPI.h>         // COMMENT OUT THIS LINE FOR GEMMA OR TRINKET
//#include <avr/power.h> // ENABLE THIS LINE FOR GEMMA OR TRINKET

#define NUMPIXELS 60 // Number of LEDs in strip

// Here's how to control the LEDs from any two pins:
#define DATAPIN    11
#define CLOCKPIN   13

#define THUNDER_PI_PIN  9

// Generally, you should use "unsigned long" for variables that hold time
// The value will quickly become too large for an int to store
unsigned long previousMillis = 0;

// Aims to use all 1000 free weather queries allowed per day
const long interval = 86400;
const int initial_brightness = 100;

int storm_state = 0;
int strip_brightness = 100;

// The last parameter is optional -- this is the color data order of the
// DotStar strip, which has changed over time in different production runs.
// Your code just uses R,G,B colors, the library then reassigns as needed.
// Default is DOTSTAR_BRG, so change this if you have an earlier strip.

// Hardware SPI is a little faster, but must be wired to specific pins
// (Arduino Uno = pin 11 for data, 13 for clock, other boards are different).
Adafruit_DotStar strip(NUMPIXELS, DOTSTAR_BRG);

void setup() {

#if defined(__AVR_ATtiny85__) && (F_CPU == 16000000L)
  clock_prescale_set(clock_div_1); // Enable 16 MHz on Trinket
#endif
  pinMode(THUNDER_PI_PIN, INPUT);  // set thunderstorm indicator pin as input
  
  strip.begin(); // Initialize pins for output
  strip.setBrightness(initial_brightness);
  strip.show();  // Turn all LEDs off ASAP

  set_strip_color(strip.Color(0, 255, 0));
  storm_state = digitalRead(THUNDER_PI_PIN);

  //Serial.begin(9600);
}

void loop() {
  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis >= interval) {
    // save the last time you blinked the LED
    previousMillis = currentMillis;

    storm_state = digitalRead(THUNDER_PI_PIN);
  }
  
  if (storm_state == HIGH) {
    thunderstorm();
  } else {
    // Back to normal
    strip.setBrightness(initial_brightness);
    set_strip_color(strip.Color(0, 255, 0));
  }
}

void set_strip_color(uint32_t color) {
  for (int i = 0; i < NUMPIXELS; i++)
  {
    strip.setPixelColor(i, color); // 'On' pixel at head
    strip.show();
  }                     
}

void thunderstorm() {
  // More likely it stays red so it's not constantly flashing
  if (random(10) >= 7) {
    // Random number of iterations to make the "lightning" seem more natural
    for (int i = 0; i < random(10); i++) {
      strip_brightness = random(255);
      strip.setBrightness(strip_brightness);
      set_strip_color(strip.Color(255, 255, 255));
      strip.show();
      delay(random(100));
      set_strip_color(strip.Color(0, random(255), 0));
      strip.show();
      delay(random(100));
    }
  } else {
    delay(random(5000, 10000));
  }
}
