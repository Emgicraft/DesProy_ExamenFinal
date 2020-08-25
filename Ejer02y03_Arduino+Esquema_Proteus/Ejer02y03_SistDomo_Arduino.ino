/*Ejer02 - Sistema Domótico
 * 
 * Autor: Magh
*/

byte leds[4]={10, 11, 12, 13};

void setup() {
  for(int i=0; i<4; i++){
    pinMode(leds[i], OUTPUT);
    digitalWrite(leds[i], 0);
  }
  Serial.begin(9600);
  Serial.println("Bienvenido Magh ;D");
}

int flag=0;

void loop() {
  if(Serial.available()>0){
    char dato=Serial.read();
    //Serial.print(dato);
    for(int i=0; i<4; i++){
      if((int)dato-48==i+1){
        //Serial.print((int)dato-48);
        if(digitalRead(leds[i])==LOW){
          digitalWrite(leds[i], HIGH);
        } else {
          digitalWrite(leds[i], LOW);
        }
        //flag ^= 1;
        delay(10);
      }
    }
  }
}
