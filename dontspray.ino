// C++ code
//
#include <LiquidCrystal.h>

const int rs = 12, en = 11, d4 = 5, d5 = 4, d6= 3, d7 = 2;
LiquidCrystal lcd(rs,en,d4,d5,d6,d7);
int heldFor;
int sprayCounter = 0;
bool sameSpray = false;
void setup()
{

  pinMode(9, INPUT);
  pinMode(13, OUTPUT);
  lcd.begin(16,2);
  lcd.print("Dont Spray");
  Serial.begin(9600);

}

void loop()
{
  //when mouse button pressed
  if (digitalRead(9) == HIGH) {
    //give an 800 ms buffer
    if (heldFor < 8) {
      lcd.clear();
      heldFor += 1;
      lcd.print("Time: " + String(heldFor*100) + "ms!"); 
      delay(100);
    }

    //after 800 ms you are considered spraying so you get sprayed
    else {
      lcd.clear();
      sameSpray = true;

      //you're sprayed (5 + number of times sprayed this game) times
      for (int i = 0; i <= 5+sprayCounter; i++) {
        digitalWrite(13, HIGH);
        delay(100);
        digitalWrite(13, LOW);
        delay(200);
      }

      lcd.print("You fucked up..."); 
      delay(1000);
    } 
  }
  //once mouse button let go, reset variables
  if (digitalRead(9) == LOW) {
    heldFor = 0;
    digitalWrite(13, LOW);
    if (sameSpray == true) {
      sameSpray = false;
      sprayCounter += 1;
      lcd.clear();
      lcd.print("Sprayed " + String(sprayCounter) + " times");
    }
  }

}
