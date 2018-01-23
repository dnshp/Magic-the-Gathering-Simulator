#include "goldfish.h"

Deck* create_deck(int cap) {
  Deck* d = (Deck*) malloc(sizeof(Deck));
  d->capacity = cap;
  d->size = 0;
  d->cards = (Card*) malloc(sizeof(Card) * cap);
  return d;
}

Card* create_card(char* name, char* cost, int type, char* typeline, char* text, int power, int toughness) {
  Card* c = (Card*) malloc(sizeof(Card));
  c->name = (char*) malloc(sizeof(char*));
  c->name = name;
  c->cost = cost;
  c->typeline = typeline;
  c->text = text;
  c->power = power;
  c->toughness = toughness;
  c->type = type;
  return c;
}

void add_card_to_deck(Deck* d, Card* c, int copies) {
  for (int i = 0; i < copies; i++) {
    if (d->size < d->capacity) {
      d->cards[d->size].name = c->name;
      d->cards[d->size].cost = c->cost;
      d->cards[d->size].type = c->type;
      d->cards[d->size].typeline = c->typeline;
      d->cards[d->size].text = c->text;
      d->cards[d->size].power = c->power;
      d->cards[d->size].toughness = c->toughness;
      d->size = d->size + 1;
    }
  }
}

void shuffle_deck(Deck* d) {
  srand(time(NULL));
  for (int i = d->size - 1; i > 0; i--) {
    int j = rand() % (i + 1);
    Card temp = d->cards[i];
    d->cards[i] = d->cards[j];
    d->cards[j] = temp;
  }
}

Card* draw_from_deck(Deck* d) {
  if (d->size > 0) {
    d->size--;
    return &(d->cards[d->size]);
  } else {
    return &(d->cards[d->size]);
  }
}

void read_card(Card* c) {
  printf("%s", c->name);
  if (!(c->type & (1 << LAND))) {
    printf(" (%s)", c->cost);
  }
  printf("\n");
  printf("%s\n", c->typeline);
  printf("%s\n", c->text);
  if (c->type & (1 << CREATURE)) {
    printf("%i / %i\n", c->power, c->toughness);
  }
  printf("\n");
}

Hand* create_hand() {
  Hand* h = (Hand*) malloc(sizeof(Hand));
  h->size = 0;
  h->capacity = 8;
  h->cards = (Card*) malloc(h->capacity * sizeof(Card));
  return h;
}

void draw_card(Hand* h, Deck* d) {
  if (h->size == h->capacity) {
    Card* temp = (Card*) malloc(h->capacity * 2 * sizeof(Card));
    for (int i = 0; i < h->size; i++) {
      memcpy(temp + i, h->cards + i, sizeof(Card));
    }
    free(h->cards);
    h->cards = temp;
  }
  h->cards[h->size] = *(draw_from_deck(d));
  h->size = h->size + 1;
}

void draw_x(Hand* h, Deck* d, int x) {
  for (int i = 0; i < x; i++) {
    draw_card(h, d);
  }
}

void view_hand(Hand* h) {
  printf("Hand:\n");
  for (int i = 0; i < h->size; i++) {
    printf("%s\n", h->cards[i].name);
  }
}

void read_hand(Hand* h) {
  for (int i = 0; i < h->size; i++) {
    read_card(h->cards + i);
  }
}

Card** import_cards(char** strings) {
  Card** cards = (Card**) malloc(sizeof(Card*) * 18128);
  Card* current;
  char* name;
  char* cost;
  int type;
  char* typeline;
  char* text;
  int power;
  int toughness;
  char* temp_str;
  int j;
  int start;
  int end;
  int arg = NAME;
  for (int i = 0; i < 18128; i++) {
    start = 0;
    end = 0;
    j = 0;
    arg = NAME;
    while (strings[i][j]) {
      if ((strings[i][j] == (int) DELIMITER) && (arg != TEXT)) {
        end = j;
        // printf("Start: %i\n", start);
        // printf("End: %i\n", end);
        if (arg == NAME) {
          name = (char*) malloc(sizeof(char) * (end - start));
          memcpy(name, &strings[i][start], (end - start) * sizeof(char));
          // printf("Name: %s\n", name);
        } else if (arg == COST) {
          cost = (char*) malloc(sizeof(char) * (end - start));
          memcpy(cost, &strings[i][start], (end - start));
          // printf("Cost: %s\n", cost);
        } else if (arg == TYPE) {
          temp_str = (char*) malloc(sizeof(char) * (end - start));
          memcpy(temp_str, &strings[i][start], (end - start));
          type = atoi(temp_str);
          // printf("Type: %i\n", type);
          memset(temp_str, (char) 0, (end - start) * sizeof(char));
          free(temp_str);
        } else if (arg == TYPELINE) {
          typeline = (char*) malloc(sizeof(char) * (end - start));
          memcpy(typeline, strings[i] + start, (end - start));
          // printf("Typeline: %s\n", typeline);
        } else if (arg == POWER) {
          temp_str = (char*) malloc(sizeof(char) * (end - start));
          memcpy(temp_str, &strings[i][start], (end - start));
          power = atoi(temp_str);
          // printf("Power: %i\n", power);
          memset(temp_str, (char) 0, (end - start) * sizeof(char));
          free(temp_str);
        } else if (arg == TOUGHNESS) {
          temp_str = (char*) malloc(sizeof(char) * (end - start));
          memcpy(temp_str, &strings[i][start], (end - start));
          toughness = atoi(temp_str);
          // printf("Toughness: %i\n", toughness);
          memset(temp_str, (char) 0, (end - start) * sizeof(char));
          free(temp_str);
        }
        arg = arg + 1;
        start = end + 1;
      }
      j = j + 1;
    }
    end = j - 1;
    text = (char*) malloc(sizeof(char) * (end - start));
    memcpy(text, strings[i] + start, (end - start));
    // printf("Text: %s\n", text);
    cards[i] = create_card(name, cost, type, typeline, text, power, toughness);
    // memset(text, (char) 0, (end - start) * sizeof(char));
  }
  return cards;
}

Card* find_card(char* name, int length, Card** cards) {
  for (int i = 0; i < 18128; i++) {
    if (strncmp(name, cards[i]->name, length) == 0) {
      // printf("%s\n", cards[i]->name);
      return cards[i];
    }
  }
  return cards[0];
}

int main() {
  // Deck* deck1 = create_deck(60);
  // Hand* hand1 = create_hand();
  // Card* plains = create_card("Plains", "0", "00001000", "Basic Land - Plains", "T: add W to your mana pool.", 0, 0);
  // Card* island = create_card("Island", "0", "00001000", "Basic Land - Island", "T: add U to your mana pool.", 0, 0);
  // Card* swamp = create_card("Swamp", "0", "00001000", "Basic Land - Swamp", "T: add B to your mana pool.", 0, 0);
  // Card* mountain = create_card("Mountain", "0", "00001000", "Basic Land - Mountain", "T: add R to your mana pool.", 0, 0);
  // Card* forest = create_card("Forest", "0", "00001000", "Basic Land - Forest", "T: add G to your mana pool.", 0, 0);
  // Card* snapcaster_mage = create_card("Snapcaster Mage", "1U", "01000000", "Creature - Human Wizard", "Flash\nWhen Snapcaster Mage enters the battlefield, target instant or sorcery card in your graveyard gains flashback until end of turn. The flashback cost is equal to its mana cost.", 2, 1);
  // for (int i = 0; i < 10; i++) {
  //   add_card_to_deck(deck1, plains);
  //   add_card_to_deck(deck1, island);
  //   add_card_to_deck(deck1, swamp);
  //   add_card_to_deck(deck1, mountain);
  //   add_card_to_deck(deck1, forest);
  //   add_card_to_deck(deck1, snapcaster_mage);
  // }
  // shuffle_deck(deck1);
  // draw_x(hand1, deck1, 7);
  // read_hand(hand1);

  FILE* all_cards = fopen("AllCards.txt", "r");
  char** data = read_line(all_cards);
  Card** cards = import_cards(data);
  Deck* deck1 = create_deck(60);
  Hand* hand1 = create_hand();
  add_card_to_deck(deck1, find_card("Restoration Angel", 17, cards), 2);
  add_card_to_deck(deck1, find_card("Snapcaster Mage", 15, cards), 4);
  add_card_to_deck(deck1, find_card("Vendilion Clique", 16, cards), 2);
  add_card_to_deck(deck1, find_card("Ajani Vengeant", 14, cards), 1);
  add_card_to_deck(deck1, find_card("Cryptic Command", 15, cards), 3);
  add_card_to_deck(deck1, find_card("Electrolyze", 11, cards), 3);
  add_card_to_deck(deck1, find_card("Lightning Bolt", 14, cards), 4);
  add_card_to_deck(deck1, find_card("Lightning Helix", 15, cards), 2);
  add_card_to_deck(deck1, find_card("Mana Leak", 9, cards), 3);
  add_card_to_deck(deck1, find_card("Path to Exile", 13, cards), 3);
  add_card_to_deck(deck1, find_card("Shadow of Doubt", 15, cards), 2);
  add_card_to_deck(deck1, find_card("Spell Snare", 11, cards), 2);
  add_card_to_deck(deck1, find_card("Sphinx's Revelation", 19, cards), 2);
  add_card_to_deck(deck1, find_card("Think Twice", 11, cards), 1);
  add_card_to_deck(deck1, find_card("Arid Mesa", 9, cards), 3);
  add_card_to_deck(deck1, find_card("Celestial Colonnade", 19, cards), 4);
  add_card_to_deck(deck1, find_card("Glacial Fortress", 16, cards), 1);
  add_card_to_deck(deck1, find_card("Hallowed Fountain", 17, cards), 2);
  add_card_to_deck(deck1, find_card("Island", 6, cards), 2);
  add_card_to_deck(deck1, find_card("Mountain", 8, cards), 1);
  add_card_to_deck(deck1, find_card("Plains", 6, cards), 1);
  add_card_to_deck(deck1, find_card("Sacred Foundry", 14, cards), 1);
  add_card_to_deck(deck1, find_card("Scalding Tarn", 13, cards), 4);
  add_card_to_deck(deck1, find_card("Steam Vents", 11, cards), 2);
  add_card_to_deck(deck1, find_card("Sulfur Falls", 12, cards), 2);
  add_card_to_deck(deck1, find_card("Tectonic Edge", 13, cards), 3);
  for (int i = 0; i < 7; i++) {
    shuffle_deck(deck1);
  }
  draw_x(hand1, deck1, 7);
  view_hand(hand1);
}
