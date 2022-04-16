#include <stdio.h>

int main()
{
		int a,b,c;
		int sum;
		float div;
		
		
		scanf("%d %d %d" , &a , &b , &c);
		
		sum=a+b+c;
		div=(float)sum/3;
		
		printf("%d\n" , sum);
		printf("%.1f" , div);
	
	return 0;
}