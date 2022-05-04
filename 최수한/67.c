#include <stdio.h>

int main()
{
	long long int a;

	scanf("%lld", &a);
	if (a < 0) 
		printf("minus\n");
	else printf("plus\n");
	

	if (a % 2 == 0) 
		printf("even\n");
	else printf("odd\n");
	


	return 0;
}