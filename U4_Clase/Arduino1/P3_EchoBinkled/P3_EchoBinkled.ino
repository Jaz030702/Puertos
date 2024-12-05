
int led = 13; //especifica el pin del led

// el pinMode le vamos a dar el valor del pin

void setup() {
  Serial.begin(9600);

  pinMode(led,OUTPUT);

}

void loop() {
  digitalWrite(led,HIGH);
  Serial.println("led prendido");
  delay(1000);
  digitalWrite(led,LOW);
  Serial.println("Led Apagado");
  delay(1000);
}
