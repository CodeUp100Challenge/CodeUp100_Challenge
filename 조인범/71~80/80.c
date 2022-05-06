#include <stdio.h>
int main(){
    int num;
    int a=0;
    int sum=0;
    scanf("%d" , &num);
    
    while(sum<num){
        a++;
        sum=a+sum;
    }
    printf("%d" , a);
}