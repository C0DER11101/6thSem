/* write a lex program to check if an arithmetic expression is valid or not and determine the operators. */

%{
	char stack[1000]={'\0'};
	int top=-1;
	void validity();
%}

%%

[-+*/]*[A-Za-z0-9][-+*/]* {for(int i=0; yytext[i]!='\0'; i++) stack[++top]=yytext[i];}
\n {validity(); return 0;}

%%

void validity()
{
	char lastScanned='\0';
	int op=0;
	while(stack[top]!='\0')
	{
		if((stack[top]<65 || stack[top]>122) && (stack[top]<48 || stack[top]>57) && lastScanned=='\0')
		{
			printf("\nInvalid expression!!\n");
			return;
		}

		switch(stack[top])
		{

			case '-': case '+': case '/': case '*':
				op++;
				if(stack[top]=='*' || stack[top]=='/' && top==0)
				{

					printf("\nInvalid expression!!\n");
					return;
				}

				else if(lastScanned=='-' || lastScanned=='+' || lastScanned=='/' || lastScanned=='*')
				{
					printf("\nInvalid expression!!\n");
					return;
				}

				else
				{
					lastScanned=stack[top--];
				}

				break;

			default:
				lastScanned=stack[top--];
		}

	}

	if(op==0)
	{
		printf("\nInvalid expression!!\n");
		return;
	}

	printf("\nExpression is valid!!\n");
	top=-1;
}

int main(void)
{
	yylex();
	printf("Expression: %s\n", stack);
	return 0;
}
