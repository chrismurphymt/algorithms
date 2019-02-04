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

void print_array(int arp[], int n) {
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
  return p;

}

int * MergeSort(int arr[], int len) {

  if (len <= 1) {
    return arr;
  }
  // Find the half way index of the array
  int half;
  int half2;

  if (len%2 == 1) {
    half = len/2+1;
    half2 = len/2;

  } else {
    half = len/2;
    half2 = half;
  }

  //allocate two arrays of half the sze of arr.
  int * first_half = malloc(half * sizeof(int));
  int * second_half = malloc(half2 * sizeof(int));

  memcpy(first_half, arr, half * sizeof(int));
  memcpy(second_half, arr + half, half2 * sizeof(int));

  // print_array(first_half, half);
  // print_array(second_half, half);

  first_half = MergeSort(first_half, half);
  second_half = MergeSort(second_half, half2);


  int * result = malloc(len * sizeof(int));

  //memcpy(result, arr, len * sizeof(int));

  int first_index = 0;
  int second_index = 0;
  int result_index = 0;
  while(first_index < half && second_index < half2) {
    if (first_half[first_index] < second_half[second_index]) {
        printf("1 result %d, fist %d\n\n", result[result_index], first_half[first_index]);
      result[result_index++] = first_half[first_index++];

    } else if (first_half[first_index] > second_half[second_index]) {
      printf("2 result %d, secod %d\n\n", result[result_index], second_half[second_index]);
      result[result_index++] = second_half[second_index++];
    } else {
      printf("3 result %d, fist %d\n", result[result_index], first_half[first_index]);
      printf("result %d, secod %d\n\n", result[result_index+1], second_half[second_index]);
      result[result_index++] = first_half[first_index++];
      result[result_index] = second_half[second_index++];
    }

  }
  while (first_index < half) {
    result[result_index++] = first_half[first_index++];
  }
  while (second_index < half2) {
    result[result_index++] = second_half[second_index++];
  }

  return result;
}
