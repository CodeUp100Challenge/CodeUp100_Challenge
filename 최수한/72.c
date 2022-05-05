#include <stdio.h>


int main()
{
	int a,b;

	scanf("%d", &b);

    re:
	
	if (b-- != 0) {
		scanf("%d", &a);
		printf("%d\n", a);
		goto re;
	}



}
