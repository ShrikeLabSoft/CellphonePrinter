int sWaterDir = 2; //Direction pin
int sWaterStep = 3; //Stepper pin

int puWaterDir = 4; //Direction pin
int puWaterStep = 5; //Stepper pin

int puInkDir = 6; //Direction pin
int puInkStep = 7; //Stepper pin

int zMoveDir = 8; //Direction pin
int zMoveStep = 9; //Stepper pin

int switchZ = 10;
int switchWater = 11;
int switchInk = 12;

int instruction = 0;
int direct = 0;
int speedd = 0;

String x;
String y, z;

boolean direccion = HIGH;

int volumeToInput = 1600;
 
void setup(){
  pinMode(sWaterDir, OUTPUT);
  pinMode(puWaterDir, OUTPUT);
  pinMode(puInkDir, OUTPUT);
  pinMode(zMoveDir, OUTPUT);

  pinMode(sWaterStep, OUTPUT);
  pinMode(puWaterStep, OUTPUT);
  pinMode(puInkStep, OUTPUT);
  pinMode(zMoveStep, OUTPUT);

  pinMode(switchZ, INPUT);
  pinMode(switchWater, INPUT);
  pinMode(switchInk, INPUT);
  
  digitalWrite (sWaterDir, LOW);
  digitalWrite (puWaterDir, LOW);
  digitalWrite (puInkDir, LOW);
  digitalWrite (zMoveDir, LOW);
 
  Serial.begin(115200);
}
 
void loop(){

  if(direct<0){
    direccion = LOW;
  }else{
    direccion = HIGH;
  }
  
  if(instruction==1){                     //inkinput 1
    digitalWrite(puInkDir, direccion);
    for (int i = 0; i < volumeToInput; i++){
      digitalWrite(puInkStep, HIGH);
      delayMicroseconds(speedd);
      digitalWrite(puInkStep, LOW);
      delayMicroseconds(speedd);
    }
  }else if(instruction==2){              //Water input 2
    digitalWrite(puWaterDir, direccion);
    for (int i = 0; i < volumeToInput; i++){
      digitalWrite(puWaterStep, HIGH);
      delayMicroseconds(speedd);
      digitalWrite(puWaterStep, LOW);
      delayMicroseconds(speedd);
    }
  }else if(instruction==3){              //Water pull 3
    digitalWrite(sWaterDir, !direccion);
    for (int i = 0; i < volumeToInput; i++){
      digitalWrite(sWaterStep, HIGH);
      delayMicroseconds(speedd);
      digitalWrite(sWaterStep, LOW);
      delayMicroseconds(speedd);
    }
  }else if(instruction==4){              //Z move printing 4
    digitalWrite(zMoveDir, direccion);
    for (int i = 0; i < volumeToInput; i++){
      digitalWrite(zMoveStep, HIGH);
      delayMicroseconds(speedd);
      digitalWrite(zMoveStep, LOW);
      delayMicroseconds(speedd);
    }
  }else if(instruction==5){              //Water pull and push
    digitalWrite(sWaterDir, !direccion);
    digitalWrite(puWaterDir, direccion);
    for (int i = 0; i < volumeToInput*1.4; i++){
      digitalWrite(sWaterStep, HIGH);
      digitalWrite(puWaterStep, HIGH);
      delayMicroseconds(speedd);
      digitalWrite(sWaterStep, LOW);
      digitalWrite(puWaterStep, LOW);
      delayMicroseconds(speedd);
    }
  }else if(instruction==6){              //Water pull and ink push
    digitalWrite(sWaterDir, !direccion);
    digitalWrite(puInkDir, direccion);
    for (int i = 0; i < volumeToInput*1.4; i++){#
      digitalWrite(sWaterStep, HIGH);
      digitalWrite(puInkStep, HIGH);
      delayMicroseconds(speedd);
      digitalWrite(sWaterStep, LOW);
      digitalWrite(puInkStep, LOW);
      delayMicroseconds(speedd);
    }
  }
  
  instruction = 0;
}            
void serialEvent() {
  while (Serial.available()) {
    x = Serial.readStringUntil('\r');
    y = Serial.readStringUntil('\r');
    z = Serial.readStringUntil('\r');
    instruction = x.toInt();
    direct = y.toInt();
    speedd = z.toInt();
    Serial.print(instruction);
    Serial.print(direct);
    Serial.println(speedd);
  }
}
