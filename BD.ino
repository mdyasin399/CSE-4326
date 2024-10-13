#define D1 494
#define n1 524
#define S 588
#define R 660
#define G 740
#define M 784
#define P 880




#define b 150
int speakerPin = 23;
int numTones = 28;

int tones[] = { M, P, G, M, G, R, S, R, S, n1, D1, D1, n1, S, S, R, G, M, G, R, S, R, n1, S, R, G, R, S };

int beat[] = { 2*b, 2*b, 2*b, 2*b, 2*b, 2*b, 2*b, b, b, 2*b, 6*b, 2*b, 2*b, 2*b, b, b, b, b, 2*b, 2*b, b, b, 2*b, 4*b, 2*b, 2*b, 2*b, 8*b};




void setup()
{

    for (int i = 0; i < numTones; i++)
  {

    tone(speakerPin, tones[i]);

    delay(beat[i]);
    }
    noTone(speakerPin);

}


void loop()
{

  
}
