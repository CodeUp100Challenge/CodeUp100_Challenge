#include <stdio.h>
int main(){
    int r,g,b;
    int sum=0;
    scanf("%d %d %d" , &r , &g , &b );
    
    for(int x=0; x<r; x++)
        for(int y=0; y<g; y++)
            for(int z=0; z<b; z++)
            {
            printf("%d %d %d\n" , x, y ,z);
            sum++;
            }
    printf("%d" , sum);
}