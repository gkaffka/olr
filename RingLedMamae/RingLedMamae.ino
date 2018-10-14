#include "FastLED.h"
#define NUM_LEDS 24
int fb = 255;
CRGB leds[NUM_LEDS];
CRGB leds2[NUM_LEDS];

void setup() {
  FastLED.addLeds<NEOPIXEL, 8>(leds, NUM_LEDS);
  FastLED.addLeds<NEOPIXEL, 9>(leds2, NUM_LEDS);
  Serial.begin(9600);
}
void loop() {
   clearLed();
  if (Serial.available() > 0) {
    // read the incoming byte:
    char incomingByte = Serial.read();
    if (incomingByte == 'F')
       ob1 (58,0, 239);
    else if(incomingByte == 'E')
       ob1 (158,0, 0);
    else if(incomingByte == 'I')
       ob1 (204,2, 255);
    else if(incomingByte == 'M')
       ob1 (130,45, 248);
    else if(incomingByte == 'A')
       ob1 (200,45, 20);     
    else if(incomingByte == 'D')
       ob2 (255,198, 2);   
  }


}

void ob1 (int r, int g, int b)
{  
  // Leds apagados, acendem um a um na cor branca com pouco brilho e ficam 1 segundo acesos
  for (int i=0; i<NUM_LEDS;i++){
      leds[i] =  CRGB(30 ,30, 30);; FastLED.show(); delay(30);
  }
  delay(1000);

   // Leds tem o brilho intensificados e ficam no estado de brilho máximo por 1 segundo
  for (int i=30; i<fb;i++){
     for (int j=0; j<NUM_LEDS;j++){
        leds[j] =  CRGB(i ,i, i);
     }
   delay(10);
     FastLED.show(); 
  }
 delay(700);

  // Leds mudam para azul um a um e permnecem azuis por 1 segundos
 for (int i=0; i<NUM_LEDS;i++){
      leds[i] =  CRGB(r ,g, b);; FastLED.show(); delay(50);
  }
 delay(1000);

  // Leds mudam para branco um a um e seguem para a proxima etapa
 for (int i=0; i<NUM_LEDS;i++){
      leds[i] =  CRGB(255 ,255, 255);; FastLED.show(); delay(50);
  }

   // Leds tem intensidade reduzida até apagarem e permancem apagados por 1 segundo
  for (int i=fb; i>=0;i--){
     for (int j=0; j<NUM_LEDS;j++){
        leds[j] =  CRGB(i ,i, i);
    }
     FastLED.show(); 
  }

   delay(200);

     // Leds piscam por 10 vezes e apagam por 1 segundo
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
   delay(1000);
  }

void ob2 (int r, int g, int b)
{  
  for (int i=0; i<10;i++){
     for (int j=0; j<NUM_LEDS;j++){
        leds[j] =  CRGB(30 ,30, 30);  
     }
     FastLED.show();
    delay(150);
       for (int j=0; j<NUM_LEDS;j++){
        leds[j] =  CRGB(0 ,0, 0);   
     }
     FastLED.show();
  delay(150);
   
  }
 }

 void ob3 (int r, int g, int b)
{  
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
 }
void clearLed() {
  for (int i = 0; i < NUM_LEDS; i++) {
    leds[i] =  CRGB(0 , 0, 0);
  }
  FastLED.show();
}
