#include "FastLED.h"
#define NUM_LEDS 24
int fb =255;
CRGB leds[NUM_LEDS];
CRGB leds2[NUM_LEDS];
void setup() { FastLED.addLeds<NEOPIXEL, 8>(leds, NUM_LEDS); 
 FastLED.addLeds<NEOPIXEL, 9>(leds, NUM_LEDS);}
void loop() {
  for (int i=0; i<NUM_LEDS;i++){
      leds[i] =  CRGB(30 ,30, 30);; FastLED.show(); delay(50);
  }

  delay(1000);
  
  for (int i=30; i<fb;i++){
     for (int j=0; j<NUM_LEDS;j++){
        leds[j] =  CRGB(i ,i, i);
     }
     delay(20);
     FastLED.show(); 
  }
delay(1000);

 for (int i=0; i<NUM_LEDS;i++){
      leds[i] =  CRGB(130 ,255, 255);; FastLED.show(); delay(150);
  }
 
 delay(2000);
 for (int i=0; i<NUM_LEDS;i++){
      leds[i] =  CRGB(255 ,255, 255);; FastLED.show(); delay(150);
  }
 delay(2000);
 
  for (int i=fb; i>=10;i--){
     for (int j=0; j<NUM_LEDS;j++){
        leds[j] =  CRGB(i ,i, i);
    }
      delay(30);
     FastLED.show(); 
  }

delay(1000);
 for (int i=0; i<NUM_LEDS;i++){
      leds[i] =  CRGB(5 ,5, 5);; FastLED.show(); delay(200);
  }

   delay(2000);

    
  for (int i=0; i<10;i++){
     for (int j=0; j<NUM_LEDS;j++){
        leds[j] =  CRGB(30 ,30, 30);  
     }
     FastLED.show();
    delay(50);
       for (int j=0; j<NUM_LEDS;j++){
        leds[j] =  CRGB(0 ,0, 0);   
     }
     FastLED.show();
  delay(50);
   
  }
   delay(2000);
}
