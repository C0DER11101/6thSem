/* lex program to check if the entered word is verb or not */

%{

%}

%%
is |
was |
were |
be |
have |
walk |
code |
program |
are |
had |
run |
will |
would |
can |
could |
throw |
sleep |
sweep |
weep |
type |
read |
break |
die |
dry |
talk  { printf("%s is a verb!!\n", yytext); }

[a-zA-Z]+ { printf("%s is not a verb\n", yytext); }
\n { return 0; }
%%

int main(void)
{
	yylex();

	return 0;
}
