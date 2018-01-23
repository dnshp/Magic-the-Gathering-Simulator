typedef struct Card {
  char* name;
  char* cost;
  int type;
  char* typeline;
  char* text;
  int power;
  int toughness;
} Card;

typedef struct Deck {
  int capacity;
  int size;
  Card* cards;
} Deck;

typedef struct Hand {
  int size;
  int capacity;
  Card* cards;
} Hand;
