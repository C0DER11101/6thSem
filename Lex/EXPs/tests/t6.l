/* copy contents of one file into another */

%{
%}

%%
. |
\n {fputc(yytext[0], yyout);}

%%

int main(void)
{
	yyin=fopen("file1", "r");
	yyout=fopen("file2", "w");
	yylex();
	fclose(yyin);
	fclose(yyout);
	return 0;
}
