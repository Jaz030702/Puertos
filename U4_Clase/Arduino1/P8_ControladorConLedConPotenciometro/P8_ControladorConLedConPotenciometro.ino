int potenciometro = A0; //Pin donde esta conectado el potenciometro
int led = 9;            //Pin PWM donde esta conetado el LED
int valor;              //Variable para almacenar el valor leido del potenciometro
int brillo;             //Variable para almacenar el valor ajustado dle brillo

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);   //Inicializa la comunicacion serial
  pinMode(led,OUTPUT);  //Configura el pin del LED como salida

}

void loop() {
  // put your main code here, to run repeatedly:
  valor = analogRead(potenciometro);  //Lee el valor del potenciometro (0 a 1023)
  brillo = map(valor,0,1023,0,255);   //Mapea el valor a un rango de 0 a 255

  analogWrite(led,brillo);            //Ajusta el brillo del LED segun el valor mapeado
  Serial.println(valor);              //Imprimir el valor del potenciometro para monitoreo

  delay(100);                         //Espera un poco antes de la siguiente lectura

}
