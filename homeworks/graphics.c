#include <stdio.h>
#include <funcs.h>
#include <stdlib.h>

int main()
{
  //SelectionSort setup
  int n = 13;
  int * arr = malloc(n * sizeof(int));
  for (int i=0;i<n;i++) {
    arr[i] = rand() % 20;
  }
  int * arp;
  arp = SelectionSort(arr,n);
  myPrintHelloMake(arp, n);

  //MergeSort setup
  int * arrMerge;
  arrMerge = MergeSort(arr,n);

  
  free(arr);
  return 0;
}
