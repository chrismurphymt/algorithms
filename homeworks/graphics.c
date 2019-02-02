#include <stdio.h>
#include <funcs.h>
#include <stdlib.h>

int main()
{
  //Inital unsorted list creation
  int n = 8;
  int * arr = malloc(n * sizeof(int));
  for (int i=0;i<n;i++) {
    arr[i] = rand() % 20;
  }
  print_array(arr, n);
  //
  // //allocate array and run selection sort
  // int * arp;
  // arp = SelectionSort(arr,n);
  // print_array(arp, n);
  // free(arp);
  //
  // //MergeSort setup
  // int * arrMerge;
  // arrMerge = MergeSort(arr,n);
  // print_array(arrMerge, n);
  // free(arrMerge);

  //one less than is in the array
  int nn = n-1;
  int start = 0;
  QuickSort(&arr, start, nn);
  print_array(arr, n);


  //FREEEDDOOOOMMM
  free(arr);
  return 0;
}
