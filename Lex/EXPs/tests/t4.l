%{
char str[1000];
int id=0;
%}

%%

[-+*/]*[A-Za-z0-9][-+*/]* {for(int i=0; yytext[i]!='\0'; i++) str[id++]=yytext[i];}
\n {return 0;}


%%

int main(void)
{
	printf("String: ");
	yylex();
	printf("String: %s\n", str);

	return 0;
}
