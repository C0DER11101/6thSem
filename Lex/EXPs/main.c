#include<stdio.h>

int fact(int);

int main(void)
{
	int num, _0int;

	printf("enter a number: ");
	scanf("%d", &num);

	printf("%d! = %d\n", num, fact(num));

	return 0;
}

int fact(int num)
{
	if(num==0)
		return 1;
	return (num*fact(num-1));
}
