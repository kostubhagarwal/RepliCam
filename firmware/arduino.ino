/****************************************************************************** 
 * Firmware code to control scanning rig.
******************************************************************************/
//Declare pin functions on Arduino
#define A 2
#define B 3
#define C 4
#define D 5
#define BUTTON_PIN 8

//Variable Declarations
int turnTableState;
int lastButtonState;
int currentButtonState;

void setup() {
  pinMode(A,OUTPUT);
  pinMode(B,OUTPUT);
  pinMode(C,OUTPUT);
  pinMode(D,OUTPUT);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  Serial.begin(9600); //Open Serial connection for debugging
}

void write(int a,int b,int c,int d){
  digitalWrite(A,a);
  digitalWrite(B,b);
  digitalWrite(C,c);
  digitalWrite(D,d);
}

void stepForward(int steps){
  for (int i = 0; i < steps && turnTableState == HIGH; i++)
  {
    write(1,0,0,0);
    delay(2);
    write(1,1,0,0);
    delay(2);
    write(0,1,0,0);
    delay(2);
    write(0,1,1,0);
    delay(2);
    write(0,0,1,0);
    delay(2);
    write(0,0,1,1);
    delay(2);
    write(0,0,0,1);
    delay(2);
    write(1,0,0,1);
    delay(2); 
    pollButtonState();
  }
}

//Main loop
void loop() {
  pollButtonState();
  if (turnTableState) {
    stepForward(50);
    delayWithButtonPolling(1000);
  }
}

void pollButtonState() {
  lastButtonState    = currentButtonState;
  currentButtonState = digitalRead(BUTTON_PIN);
  if(lastButtonState == HIGH && currentButtonState == LOW) {
    Serial.println("The button is pressed");
    // toggle turn table
    turnTableState = !turnTableState;
  }
}

void delayWithButtonPolling(int milliseconds) {
  for(int x = 0; x < milliseconds; x++)
  {
    pollButtonState();
    delay(1);
  }
}