/* write a C-program in a file and show how many keywords, constants and special characters are present in your file. */

%{
	int countKey=0, countId=0, countSym=0;
%}

%%

[^a-zA-Z]int[^a-zA-Z] |
[^a-zA-Z]float[^a-zA-Z] |
[^a-zA-Z]char[^a-zA-Z] |
[^a-zA-Z]double[^a-zA-Z] |
[^a-zA-Z]long[^a-zA-Z] |
[^a-zA-Z]short[^a-zA-Z] |
[^a-zA-Z]signed[^a-zA-Z] |
[^a-zA-Z]unsigned[^a-zA-Z] |
[^a-zA-Z]typedef[^a-zA-Z] |
[^a-zA-Z]struct[^a-zA-Z] |
[^a-zA-Z]if[^a-zA-Z] |
[^a-zA-Z]else[^a-zA-Z] |
[^a-zA-Z]for[^a-zA-Z] |
[^a-zA-Z]while[^a-zA-Z] |
[^a-zA-Z]goto[^a-zA-Z] |
[^a-zA-Z]continue[^a-zA-Z] |
[^a-zA-Z]break[^a-zA-Z] |
[^a-zA-Z]union[^a-zA-Z] |
[^a-zA-Z]switch[^a-zA-Z] |
[^a-zA-Z]case[^a-zA-Z] |
[^a-zA-Z]default[^a-zA-Z] |
[^a-zA-Z]const[^a-zA-Z] |
[^a-zA-Z]void[^a-zA-Z] |
[^a-zA-Z]extern[^a-zA-Z] |
[^a-zA-Z]auto[^a-zA-Z] |
[^a-zA-Z]static[^a-zA-Z] |
[^a-zA-Z]do[^a-zA-Z] |
[^a-zA-Z]return[^a-zA-Z] |
[^a-zA-Z]enum[^a-zA-Z] |
[^a-zA-Z]sizeof[^a-zA-Z] |
[^a-zA-Z]volatile[^a-zA-Z] |
[^a-zA-Z]register[^a-zA-Z] { ++countKey; }

[^0-9][a-zA-z] {++countId;}

%%

int main(void)
{
	yyin=fopen("main.c", "r");
	yylex();
	printf("\nthere are %d keywords in the file!!\n", countKey);
	printf("\nthere are %d identifiers in the file!!\n", countId);


	fclose(yyin);
	return 0;
}
