int led =2;


void setup() {
  // put your setup code here, to run once:
  pinMode(led,OUTPUT);
  Serial.begin(9600);
  Serial.setTimeout(10);
  //HIGH valor que le estamos mandando
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    int v=Serial.readString().toInt();
    digitalWrite(led,v); // el pin que deseamos controlar y el valor
    //// pin que vamos a controlar(2), vbalor qu edaremos que
  }

}
