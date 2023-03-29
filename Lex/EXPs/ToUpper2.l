/* write a program in lex to convert a string of lower case characters into upper case characters */

%{
	#include<ctype.h>
%}


%%

[a-z] {printf("%c", toupper(yytext[0]));}

\. {return 0;}

%%

int main(void)
{
	yylex();
	return 0;
}
