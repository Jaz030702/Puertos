
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); //Inicializa la comunicacion serial...
  //valores a los que se comunica arduino con otros dispositivos...
  //es una instruccion en Arduino que inicializa la comunicacion serial entre la placa Arduino y el monitor serial de la computadora
  //MODULO UART (Comunicacion serial por UART)
  //9600 la unicdad minima que lo trasmite y 
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println(" hola!");
  delay(500);//milisecs
}
