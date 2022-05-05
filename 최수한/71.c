#include <stdio.h>


int main()
{
	int a;

    re:
	scanf("%d", &a);
	if (a != 0) {
		printf("%d\n", a);
		goto re;
	}



}
