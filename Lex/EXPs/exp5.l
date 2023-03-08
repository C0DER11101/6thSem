/* write a lex program to remove space from an input file and show in the output file */

%{
%}

%%
[ \t\n]+ {;}
. {fputs(yytext, yyout);}
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
