/* remove single space from a file */

%{
%}

%%
[ \t][ \t]+ {fputc(' ', yyout);}
[ \t] {;}
. {fputc(yytext[0], yyout);}
%%

int main(void)
{
	yyin=fopen("wspace", "r");
	yyout=fopen("Wspace", "w");
	yylex();

	fclose(yyin);
	fclose(yyout);
	return 0;
}
