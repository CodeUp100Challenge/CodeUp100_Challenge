#include <stdio.h>
int main(){
    
    int a,sum=0;
    scanf("%d" , &a);
    
    for(int i=0; i<=a; i++)
    {
    if(i%2==0)
        sum=sum+i;
    }
    printf("%d" , sum);
}