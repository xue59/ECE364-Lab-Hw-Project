/*
 * $Id$
 */

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
  int number;

  if(argc != 2) {
    printf("Bad arguments.\n");
    return 1;
  }

  number = atoi(argv[1]);
  if(number <= 0) {
    printf("Bad number.\n");
    return 2;
  }

  for(;number >= 0; number--) {
    printf("%d ", number);
  }

  printf("\n");

  return 0;
}
