int smDirectionPin = 2; //Direction pin
int smStepPin = 3; //Stepper pin
int smDirectionPin2 = 4; //Direction pin
int smStepPin2 = 5; //Stepper pin
int instruction = 0;
int dobEngin =0;

String x;
String y;
 
void setup(){
  //Sets all pin to output; the microcontroller will send them(the pins) bits, it will not expect to receive any bits from thiese pins.*/
  pinMode(smDirectionPin, OUTPUT);
  pinMode(smStepPin, OUTPUT);
  pinMode(smDirectionPin2, OUTPUT);
  pinMode(smStepPin2, OUTPUT);
  digitalWrite (smDirectionPin, LOW);
  digitalWrite (smStepPin, LOW);
  digitalWrite (smDirectionPin2, LOW);
  digitalWrite (smStepPin2, LOW);
 
  Serial.begin(115200);
}
 
void loop(){
  if(instruction==1){
    digitalWrite(smDirectionPin, HIGH);
    for (int i = 0; i < 1600; i++){
      digitalWrite(smStepPin, HIGH);
      delayMicroseconds(700);
      digitalWrite(smStepPin, LOW);
      delayMicroseconds(700);
    }
  }else if(instruction==2){
    digitalWrite(smDirectionPin, LOW);
    for (int i = 0; i < 1600; i++){
      digitalWrite(smStepPin, HIGH);
      delayMicroseconds(700);
      digitalWrite(smStepPin, LOW);
      delayMicroseconds(700);
    }
  }
 if(instruction==3){
    digitalWrite(smDirectionPin2, HIGH);
    for (int i = 0; i < 1600; i++){
      digitalWrite(smStepPin2, HIGH);
      delayMicroseconds(700);
      digitalWrite(smStepPin2, LOW);
      delayMicroseconds(700);
    }
  }else if(instruction==4){
    digitalWrite(smDirectionPin2, LOW);
    for (int i = 0; i < 1600; i++){
      digitalWrite(smStepPin2, HIGH);
      delayMicroseconds(700);
      digitalWrite(smStepPin2, LOW);
      delayMicroseconds(700);
    }
  }
  if (dobEngin==1){
     digitalWrite(smDirectionPin, HIGH);
     digitalWrite(smDirectionPin2, HIGH);
    for (int i = 0; i < 1600; i++){
      digitalWrite(smStepPin, HIGH);
      digitalWrite(smStepPin2, HIGH);
      delayMicroseconds(700);
      digitalWrite(smStepPin, LOW);
      digitalWrite(smStepPin2, LOW);
      delayMicroseconds(700);
    }
  }      
   if (dobEngin==2){
     digitalWrite(smDirectionPin, LOW);
     digitalWrite(smDirectionPin2, LOW);
    for (int i = 0; i < 1600; i++){
      digitalWrite(smStepPin, HIGH);
      digitalWrite(smStepPin2, HIGH);
      delayMicroseconds(700);
      digitalWrite(smStepPin, LOW);
      digitalWrite(smStepPin2, LOW);
      delayMicroseconds(700);
  }
   }
   if (dobEngin==3){
     digitalWrite(smDirectionPin, HIGH);
     digitalWrite(smDirectionPin2, LOW);
    for (int i = 0; i < 1600; i++){
      digitalWrite(smStepPin, HIGH);
      digitalWrite(smStepPin2, HIGH);
      delayMicroseconds(700);
      digitalWrite(smStepPin, LOW);
      digitalWrite(smStepPin2, LOW);
      delayMicroseconds(700);
  }
   }
   if (dobEngin==4){
     digitalWrite(smDirectionPin, LOW);
     digitalWrite(smDirectionPin2, HIGH);
    for (int i = 0; i < 1600; i++){
      digitalWrite(smStepPin, HIGH);
      digitalWrite(smStepPin2, HIGH);
      delayMicroseconds(700);
      digitalWrite(smStepPin, LOW);
      digitalWrite(smStepPin2, LOW);
      delayMicroseconds(700);
  }
   }
  
dobEngin = 0;
  instruction = 0;
}            
void serialEvent() {
  while (Serial.available()) {
    x = Serial.readStringUntil('\r');
    instruction = x.toInt();
    Serial.println(instruction);
   
    y = Serial.readStringUntil('\r');
    dobEngin = y.toInt();
    Serial.println(dobEngin);
   
  }
}
