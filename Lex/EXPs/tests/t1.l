%{
%}

%%

[0-9]+ {printf("%c\n%c\n%c\n%c", yytext[0], yytext[1], yytext[2], yytext[3]);}

%%

int main(void)
{
	yylex();
	return 0;
}
