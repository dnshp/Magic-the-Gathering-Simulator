#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <time.h>
#include "csv_reader.h"

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

enum TYPES {
  ARTIFACT = 0,
  CREATURE = 1,
  ENCHANTMENT = 2,
  INSTANT = 3,
  LAND = 4,
  PLANESWALKER = 5,
  SORCERY = 6,
  TRIBAL = 7
};

enum CSV_ARGS {
  NAME = 0,
  COST = 1,
  TYPE = 2,
  TYPELINE = 3,
  POWER = 4,
  TOUGHNESS = 5,
  TEXT = 6,
};

Deck* create_deck(int cap);
Card* create_card(char* name, char* cost, int type, char* typeline, char* text, int power, int toughness);
void add_card_to_deck(Deck* d, Card* c, int copies);
void shuffle_deck(Deck* d);
Card* draw_from_deck(Deck* d);
void read_card(Card* c);
Hand* create_hand();
void draw_card(Hand* h, Deck* d);
void draw_x(Hand* h, Deck* d, int x);
void view_hand(Hand* h);
void read_hand(Hand* h);
Card** import_cards(char** strings);
Card* find_card(char* name, int length, Card** cards);
