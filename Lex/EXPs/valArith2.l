%{
	char stack[1000]={'\0'};
	int top=-1;
%}


%%

[-+*/]*[A-Za-z0-9][-+*/]* {for(int i=0; yytext[i]!='\0'; i++){ stack[++top]=yytext[i]; printf("%d\n", i);}}

\n {return 0;}



%%


int main(void)
{
	printf("enter a string: ");
	yylex();
	printf("String: %s\n", stack);
	return 0;
}
