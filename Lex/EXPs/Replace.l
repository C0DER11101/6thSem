/* write a program in lex to replace every keyword "float" in a C program with the keyword "double". */

%{
%}

%%

"float" {fputs("double", yyout);}

[A-Za-z0-9]float[A-Za-z0-9] {ECHO;}


%%

int main(void)
{
	yyin=fopen("main2.c", "r");

	yyout=fopen("main3.c", "w");
	yylex();

	fclose(yyin);
	fclose(yyout);
	return 0;
}
