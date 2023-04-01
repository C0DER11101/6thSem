%{
%}

%%

[A-Za-z0-9][-+*/]*[A-Za-z0-9] {printf("%c\n%c\n%c\n", yytext[0], yytext[1], yytext[2]);}

%%

int main(void)
{
	yylex();
	return 0;
}
