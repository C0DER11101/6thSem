/* input a number and check if it is positive or negative and also display the number of positive numbers and negative numbers */

%{
	int countPos=0, countNeg=0;
%}

%%

[ \t\n]+[-][0-9]+ |
[-][0-9]+ {printf("%s is negative!!\n", yytext); countNeg++;}

[0-9]+ { printf("%s is positive!!\n", yytext); countPos++;}


[a-zA-Z] { return 0; }

%%

int main(void)
{
	yylex();
	printf("\nPositive numbers: %d\n", countPos);
	printf("\nNegative numbers: %d\n", countNeg);

	return 0;
}
