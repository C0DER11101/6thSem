#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<stdbool.h>

/* regex: (0|1)* */

int main(void)
{
	bool accepted=true;
	char*str=malloc(1000*sizeof(char));
	printf("\nRegeX: (0|1)*\n");

	printf("enter a string: ");
	fscanf(stdin, "%s", str);

	for(int i=0; str[i]!='\0'; i++)
	{
		if(str[i]!='0' && str[i]!='1')
		{
			accepted=false;
			break;
		}
	}

	if(accepted==true)
		printf("\nString accepted!!\n");
	else
		printf("\nString rejected!!\n");

	free(str);
	return 0;
}
