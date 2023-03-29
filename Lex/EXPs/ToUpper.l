%{
	char upper[1000];
	int idx=0;
	void showStr();
%}

%%

[a-z] |
[ \t]+ {for(int i=0; yytext[i]!='\0'; i++){upper[idx++]=yytext[i]==' '?yytext[i]:yytext[i]-32;}}

[a-z]\n {upper[idx++]=yytext[0]-32;showStr();}

[A-Z] {for(int i=0; yytext[i]!='\0'; i++){upper[idx++]=yytext[i]==' '?yytext[i]:yytext[i]-0;}}

[A-Z]\n {upper[idx++]=yytext[0]; showStr();}

[0-9] {for(int i=0; yytext[i]!='\0'; i++){upper[idx++]=yytext[i]==' '?yytext[i]:yytext[i]-0;}}

[0-9]\n {upper[idx++]=yytext[0]; showStr();}

[~] {return 0;}

%%

void showStr()
{
	printf("%s\n", upper);
	idx=0;
	for(int i=0; upper[i]!='\0'; i++)
		upper[i]='\0';
}

int main(void)
{
	yylex();
	return 0;
}
