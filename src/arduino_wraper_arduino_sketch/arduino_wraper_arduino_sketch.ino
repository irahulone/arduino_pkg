
int ledPin = 13;
int counter = 0;
int sensor_value = 404;

const long interval = 1000;
unsigned long previousMillis = 0;

void setup() 
{
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
  analogWrite(ledPin, 255);
}

void loop() 
{
  // check for serial data, if availabe then write the value to the pin
  if(Serial.available())
  {
    int x = Serial.parseInt();
    analogWrite(ledPin,x);
  }

  // send the values over serial periodically
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= interval) 
  {
    previousMillis = currentMillis;
    counter += 1;
    if (counter > 2) 
    counter = 0;
    Serial.print(counter);      Serial.print(",");
    Serial.print(sensor_value); Serial.println();
  }

    

}
