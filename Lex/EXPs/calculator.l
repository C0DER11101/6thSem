%{
#include<stdlib.h>
double a, b;
int opt=0, count=0;
void calculate();
%}

%%

[0-9]+ {calculate();}
[+] {opt=1;}
[-] {opt=2;}
[/] {opt=3;}
[*] {opt=4;}
exit {return 0;}

%%

void calculate()
{
	if(count==0)
	{
		a=atof(yytext);
		count++;
	}

	else if(count>0)
	{
		b=atof(yytext);
	}
	switch(opt)
	{
		case 1:
			a=a+b;
			printf("Result: %.2lf\n", a);
			a=b=0.0;
			count=0;
			opt=0;
			break;

		case 2:
			a=a-b;
			printf("Result: %.2lf\n", a);
			a=b=0.0;
			count=0;
			opt=0;
			break;

		case 3:
			a=a/b;
			printf("Result: %.2lf\n", a);
			a=b=0.0;
			count=0;
			opt=0;
			break;

		case 4:
			a=a*b;
			printf("Result: %.2lf\n", a);
			a=b=0.0;
			count=0;
			opt=0;
			break;
	}
}

int main(void)
{
	yylex();
	return 0;
}
