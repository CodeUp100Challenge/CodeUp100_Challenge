#include <stdio.h>
int main()
{
    int a,b;
    
    scanf("%d %d" , &a ,&b);
    
    for(int i=1; i<=a; i++){
        for(int x=1; x<=b; x++){
        printf("%d %d" , i , x );
        printf("\n");}
    }
    
    return 0;
}