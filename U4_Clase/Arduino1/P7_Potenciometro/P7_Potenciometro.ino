//voltaje de referencia: 5v
//bits de resolucion: 18 bits de resolucion...1024 valor positivo
//pines.     1.     2.    3.
//           GND    A0    SV

//Pin 1 y 3 son intercambiables (no importa cual es cual)
//Son los extremos del potenciometro
int potenciometro = A0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  //nota: un pin analogico soo es de entrada
}
int valor;
void loop() {
  // put your main code here, to run repeatedly:
  valor = analogoRead(potenciometro);
  Serial.println(valor);
  dalay(100);
}
