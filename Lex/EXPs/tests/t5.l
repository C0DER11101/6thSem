/* check if a string contains characters other than alphabets */

%{
	enum okay
	{
		onlyAlpha,
		alphaOther,
	};

	enum okay ok;
%}

%%
[ \t]*[a-zA-Z][ \t]* {;}
\n {ok=onlyAlpha;return 0;}
[^a-zA-Z] {ok=alphaOther; return 0;}
%%

int main(void)
{
	yylex();

	if(ok==alphaOther)
		printf("\nString contains characters other than alphabets!!\n");

	else if(ok==onlyAlpha)
		printf("\nString contains only alphabets!!\n");

	return 0;
}
