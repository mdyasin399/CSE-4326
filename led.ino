#include <Adafruit_NeoPixel.h>

// Pin where the NeoPixel data line is connected
#define PIN 6

// Number of NeoPixels in the strip
#define NUMPIXELS 8

// Create an instance of the Adafruit_NeoPixel class
Adafruit_NeoPixel pixels(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  // Initialize the NeoPixel strip
  pixels.begin();
  // Set all pixels to off
  pixels.show(); 
}

void loop() {
  // Set all pixels to a single color (R, G, B)
  setSingleColor(255, 0, 0);  // Red
  delay(1000);                // Wait for 1 second

  setSingleColor(0, 255, 0);  // Green
  delay(1000);                // Wait for 1 second

  setSingleColor(0, 0, 255);  // Blue
  delay(1000);                // Wait for 1 second
}

// Function to set all NeoPixels to the same color
void setSingleColor(uint8_t r, uint8_t g, uint8_t b) {
  for (int i = 0; i < NUMPIXELS; i++) {
    pixels.setPixelColor(i, pixels.Color(r, g, b));
  }
  pixels.show();  // Update the strip to show the color
}
