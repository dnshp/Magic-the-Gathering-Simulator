#include "csv_reader.h"

char** read_line(FILE* file) {
  char** strings = (char**) malloc(sizeof(char*) * 18128);
  int index = 0;
  unsigned long num_cards = 0;
  int c = fgetc(file);
  int last_newline = 0;
  int buffer_capacity = BUF_CAP;
  int buffer_size = 0;
  char* buffer = (char*) malloc(sizeof(char) * buffer_capacity);
  while (c != EOF) {
    if (buffer_size == buffer_capacity) {
      char* temp = (char*) malloc(sizeof(char) * buffer_capacity * 2);
      memcpy(temp, buffer, sizeof(char) * buffer_capacity);
      buffer_capacity = buffer_capacity * 2;
      free(buffer);
      buffer = temp;
    }
    buffer[buffer_size] = c;
    buffer_size = buffer_size + 1;
    if (c == (int) '\n') {
      if (last_newline == 0) {
        last_newline = 1;
      } else {
        strings[index] = (char*) malloc(sizeof(char) * buffer_size);
        memcpy(strings[index], buffer, sizeof(char) * buffer_size);
        memset(buffer, (char) 0, buffer_capacity);
        index = index + 1;
        buffer_size = 0;
      }
    } else {
      last_newline = 0;
    }
    c = fgetc(file);
  }
  return strings;
}

// int main() {
//   FILE* all_cards = fopen("AllCards.txt", "r");
//   char** data = read_line(all_cards);
//   for (int i = 0; i < 18128; i++) {
//     printf("%i\n", i);
//     printf("%s", data[i]);
//   }
// }
