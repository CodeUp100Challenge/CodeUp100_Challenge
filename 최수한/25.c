#include <stdio.h>
int main()
{
	int a,b,c,d,e;
	scanf("%1d%1d%1d%1d%1d",&a,&b,&c,&d,&e);
	printf("[%1d]\n", a*10000);
	printf("[%1d]\n", b*1000);
	printf("[%1d]\n", c*100);
	printf("[%1d]\n", d*10);
	printf("[%1d]", e);

	return 0;
}