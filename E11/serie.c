#include <stdio.h>
#include <math.h>
int fibonacci(int n){
  int f;
  if(n==1||n==2){
    return 1;
  }else if(n>2){
    return fibonacci(n-2)+fibonacci(n-1);
  }
}
double rapporto(int n){
  return (double)fibonacci(n)/fibonacci(n-1);
}
  