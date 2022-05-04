#include <stdio.h>
int main()
{
	long long int a, b, c;
	scanf("%lld %lld %lld", &a, &b, &c);
	printf("%lld\n", a + b + c);
	printf("%.1f", (float)(a + b + c) / 3);
}