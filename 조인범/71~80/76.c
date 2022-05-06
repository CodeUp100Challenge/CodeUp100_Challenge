#include <stdio.h>
int main(){

char x='a';
char y;

scanf("%c" , &y );

do {
printf("%c " , x);
x++;
    
}while(y>=x);
}