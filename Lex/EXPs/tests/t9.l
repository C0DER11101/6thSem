%{
%}

%%
[0-9]*[02468]$ {printf("\neven!\n");}
[0-9]*[13579]$ {printf("\nodd!\n");}

exit {return 0;}
%%

int main(void)
{
	yylex();
	return 0;
}
