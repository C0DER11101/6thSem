/* write a lex program to copy a C program after replacing every keyword float by the keyword double */

%{
%}

%%

"float" {fputs("double", yyout);}

[A-Za-z0-9]float[A-Za-z0-9] {;}

%%

int main(void)
{
	yyin=fopen("input.c", "r");
	yyout=fopen("output.c", "w");
	yylex();

	fclose(yyin);
	fclose(yyout);
	return 0;
}
