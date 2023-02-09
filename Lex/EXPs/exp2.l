/* lex program to check for digits in an input sentence */

%{

%}

%%
[0-9] { printf("\n%s is a digit\n", yytext); }
. { printf(" "); }
\n { return 0; }
%%

int main(void)
{
	yylex();
	return 0;
}
