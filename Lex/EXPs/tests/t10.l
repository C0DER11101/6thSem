/* check valid phone number */

%{
	int len=0;
%}

%%
[0-9] {++len;}
[A-Za-z0-9] {len=-1;return 0;}
\n {return 0;}
%%

int main(void)
{
	yylex();
	if(len==-1 || len>10)
		printf("\nInvalid mobile number!\n");
	else
		printf("\nValid mobile number!\n");
	return 0;
}
