/* count words that have a length greater than 5 and less than 10 */

%{
	int len=0, output=0;
%}

%%
[A-Za-z0-9] {++len;}

[ \t] {len=len>5 && len<10?output++:len; len=0;}

\n {len=len>5 && len<10?output++:len; return 0;}

%%

int main(void)
{
	yylex();

	printf("Output: %d\n", output);
	return 0;
}
