#include <stdio.h>
int main()
{
	int y, m,d;
	scanf("%d.%d.%d", &y, &m,&d);
	printf("%d.%d.%02d", y, m,d);
	return 0;
}