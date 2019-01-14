#include <stdio.h>
#include <funcs.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

struct Address
{
  char name[50];
  char street[100];
  char city[50];
  char state[20];
  int pin;
};

void myPrintHelloMake(int arp[], int n) {
  for (int i=0;i<n;i++) {
    printf("%d, ", arp[i]);
  }
  printf("\n");

  return;

}

int * SelectionSort(int  arr[], int len) {
  // int arr[NUM_OF_ELEMS];

  int * p = malloc(len * sizeof(int));
  memcpy(p, arr, len * sizeof(int));
  for (int i = 0; i<len; i++) {
    printf("%d, ", arr[i]);
    int min_index = i;
    for (int j = i+1;j<len;j++) {
      if (p[j] < p[min_index]) {
        min_index = j;
      }
    }
    int temp = p[min_index];
    p[min_index] = p[i];
    p[i] =temp;
  }
  printf("\n");
  return p;

}

int * MergeSort(int arr[], int len) {

  if (len <= 1) {
    return arr;
  }
  // Find the half way index of the array
  int half = len/2;

  //allocate two arrays of half the sze of arr.
  int * first_half = malloc(half * sizeof(int));
  int * second_half = malloc(half * sizeof(int));

  memcpy(p, arr, len * sizeof(int));



  return p;
}
