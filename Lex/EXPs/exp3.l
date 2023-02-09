/* lex program to count the number of characters in a given input statement */
%{
	int count_chars=0;
%}

%%
[a-zA-Z | .] { ++count_chars; }
"!" |
"@" |
"#" |
"$" |
"%" |
"^" |
"*" |
"(" |
")" |
"_" |
"-" |
"=" |
"+" |
"[" |
"]" |
"{" |
"}" |
":" |
";" |
"'" |
"," |
"<" |
">" |
"?" |
"/"  { ++count_chars; }
[0-9] { }
\n { return 0; }
%%

int main(void)
{
	yylex();
	printf("\nthere are %d characters in the given input statement!\n", count_chars);
	return 0;
}
