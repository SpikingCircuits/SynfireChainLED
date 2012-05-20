int nb_neurons;
int input;

void setup() {                
  nb_neurons = 13;
  for (int i = 2; i < nb_neurons; i++) {
     pinMode(i, OUTPUT);
  }
  
  Serial.begin(38400);
  Serial.flush();  
  
}

void loop() {
 
   //for (int i = 2; i < nb_neurons; i++) {
     // digitalWrite(i, LOW);
  //}
  
  input = Serial.read();
  if (input == '-1') {}

  else
  {
      if (input == '2'){ledBlink(2);}
      if (input == '3'){ledBlink(3);}
      if (input == '4'){ledBlink(4);}
      if (input == '5'){ledBlink(5);}
      if (input == '6'){ledBlink(6);}
      if (input == '7'){ledBlink(7);}
      if (input == '8'){ledBlink(8);}
      if (input == '9'){ledBlink(9);}
      if (input == 'a'){ledBlink(10);}
    }
    
}

void ledBlink(int pin) {
     digitalWrite(pin, HIGH);
     delay(50);
     digitalWrite(pin, LOW);
}
