/* input a number and check if it is positive or negative */

%{
%}

%%

\-[0-9]+ { printf("%s is negative!!\n", yytext); }

[0-9]+ { printf("%s is positive!!\n", yytext); }

[a-zA-Z] { return 0; }

%%

int main(void)
{
	yylex();

	return 0;
}
