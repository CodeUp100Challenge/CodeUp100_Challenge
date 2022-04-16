#include <stdio.h>
int main()
{
    int a;
    
    notzero:
    scanf("%d" , &a);
    if(a!=0)
       {
        printf("%d\n" , a);
        goto notzero;
        }
    
}