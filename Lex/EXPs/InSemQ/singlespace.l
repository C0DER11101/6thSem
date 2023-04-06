/* write a lex program to replace any number of whitespaces by a single blank. */

%{
%}

%%

[ \t]+ {fputs(" ", yyout);}


%%

int main(void)
{
	yyin=fopen("input.txt", "r");
	yyout=fopen("output.txt", "w");
	yylex();
	fclose(yyin);
	fclose(yyout);
	return 0;
}
