#include "FastLED.h"
#define NUM_LEDS 144
CRGB leds[NUM_LEDS];
void setup() { FastLED.addLeds<NEOPIXEL, 8>(leds, NUM_LEDS); }
void loop() {
  for (int i=0; i<NUM_LEDS;i++){
  leds[i] =  CRGB(150 ,150, 150);; FastLED.show(); delay(0);
  }
  for (int i=0; i<NUM_LEDS;i++){
  leds[i] =  CRGB(0 ,0, 0);; FastLED.show(); delay(0);
  }
   for (int i=0; i<NUM_LEDS;i++){
  leds[i] =  CRGB(10 ,10, 10);; FastLED.show(); delay(20);
  }
  delay(3000);
  for (int i=0; i<NUM_LEDS;i++){
  leds[i] =  CRGB(0 ,0, 0);; FastLED.show(); delay(20);
  }
  delay(3000);
  
}
