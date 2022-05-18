#include <stdio.h>
int main(){

long long int h,b,c,s;
double kb;
double mb;
scanf("%ld %ld %ld %ld" , &h , &b , &c , &s);

kb=(double)(h*b*c*s)/(8*1024*1024);


printf("%.1lf MB" , kb);

}