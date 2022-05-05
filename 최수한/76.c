#include <stdio.h>


int main()
{
	char a;
	char ch = 'a';
	
	scanf("%c", &a);

	do {
		printf("%c ", ch++);

	} while (a >= ch);
}
