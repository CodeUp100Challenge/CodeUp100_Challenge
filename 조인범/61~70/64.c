#include <stdio.h>
int main()
{
int a,b,c;

scanf("%d %d %d" , &a ,&b ,&c);

printf("%d" , (a>b ? b:a)>c ? c :(a>b ? b:a));

return 0;
}