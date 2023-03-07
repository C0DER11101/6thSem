/* simply read a file and display it */
%{
%}

%%

. { printf("%s", yytext); }

%%

int main(void)
{
	yyin=fopen("test.txt", "r");

	yylex();
	
	return 0;
}
