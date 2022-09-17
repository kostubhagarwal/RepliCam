/****************************************************************************** 
 * Firmware code to control scanning rig.
******************************************************************************/
//Declare pin functions on Arduino
#define stp 2
#define dir 3
#define MS1 4
#define MS2 5
#define MS3 6
#define EN  7
#define BUTTON_PIN 8

//Variable Definitions
int turnTableState;
int lastButtonState;
int currentButtonState;

void setup() {
  pinMode(stp, OUTPUT);
  pinMode(dir, OUTPUT);
  pinMode(MS1, OUTPUT);
  pinMode(MS2, OUTPUT);
  pinMode(MS3, OUTPUT);
  pinMode(EN, OUTPUT);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  resetBEDPins(); //Set step, direction, microstep and enable pins to default states
  Serial.begin(9600); //Open Serial connection for debugging
}

//Main loop
void loop() {
  digitalWrite(EN, LOW); //Pull enable pin low to set FETs active and allow motor control
  pollButtonState();
  if (turnTableState) {
    StepForward(100);
    delayWithButtonPolling(1000);
  }
  resetBEDPins();
  delay(25);
}

void pollButtonState() {
  lastButtonState    = currentButtonState;      // save the last state
  currentButtonState = digitalRead(BUTTON_PIN); // read new state
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

//Reset Big Easy Driver pins to default states
void resetBEDPins()
{
  digitalWrite(stp, LOW);
  digitalWrite(dir, LOW);
  digitalWrite(MS1, LOW);
  digitalWrite(MS2, LOW);
  digitalWrite(MS3, LOW);
  digitalWrite(EN, HIGH);
}

//Default microstep mode function
void StepForward(int durationMS)
{
  digitalWrite(dir, LOW); //Pull direction pin low to move "forward"
  for(int x = 0; x < durationMS && turnTableState == HIGH; x++)  //Loop the forward stepping enough times for motion to be visible
  {
    digitalWrite(stp,HIGH); //Trigger one step forward
    delay(1);
    digitalWrite(stp,LOW); //Pull step pin low so it can be triggered again
    delay(1);
    pollButtonState();
  }
}
