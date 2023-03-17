/* lex program to detect assembly language instructions */

%{
	#include<stdbool.h>
	bool accepted=true;
%}

%%

[2-9] {accepted=false;return 0;}

0 {accepted=true;}
1 {accepted=true;}

\n {return 0;}

%%

int main(void)
{
	yylex();

	if(accepted==false)
		printf("\nNot accepted!!\n");
	else
		printf("\nAccepted!!\n");

	return 0;
}
