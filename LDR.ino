void setup()
{
  pinMode(11, OUTPUT);
  pinMode(A0, INPUT);
}

void loop()
  
{
  
 int value= analogRead(A0);
  
  if(value<100)
  {
    digitalWrite(11, HIGH);
  }
  else
  {
     digitalWrite(11, LOW);

  }
}
