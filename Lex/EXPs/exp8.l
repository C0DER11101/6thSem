/* check if a number is even or odd */

%{
%}

%%

\d*[02468]$ {printf("\nEven!!\n");}
\d*[13579]$ {printf("\nOdd!!\n");}
[a-zA-Z] {return 0;}

%%

int main(void)
{
	yylex();

	return 0;
}
