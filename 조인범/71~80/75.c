#include <stdio.h>
int main(){
    
    int a;
    scanf("%d" , &a);
    a-=1;
    for(a; a>=0; a--)
    printf("%d \n" , a);
}