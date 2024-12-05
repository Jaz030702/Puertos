int led = 13;
int led2 = 4;

//

void setup() {
    Serial.begin(9600);

    pinMode(led,OUTPUT);
    pinMode(led2,OUTPUT);

}

void loop() {
    digitalWrite(led,HIGH);
  delay(3000);
  digitalWrite(led,LOW);
  delay(1000);
    digitalWrite(led2,HIGH);
  delay(5000);
  digitalWrite(led2,LOW);
  delay(1000);


}
