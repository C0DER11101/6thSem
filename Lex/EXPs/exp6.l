/* write a C-program in a file and show how many keywords, constants and special characters are present in your file. */

%{
	int countKey=0, countId=0, countSym=0;
%}

%%

[^A-Za-z0-9]int[^A-Za-z0-9] |
[^A-Za-z0-9]float[^A-Za-z0-9] |
[^A-Za-z0-9]char[^A-Za-z0-9] |
[^A-Za-z0-9]double[^A-Za-z0-9] |
[^A-Za-z0-9]long[^A-Za-z0-9] |
[^A-Za-z0-9]short[^A-Za-z0-9] |
[^A-Za-z0-9]signed[^A-Za-z0-9] |
[^A-Za-z0-9]unsigned[^A-Za-z0-9] |
[^A-Za-z0-9]typedef[^A-Za-z0-9] |
[^A-Za-z0-9]struct[^A-Za-z0-9] |
[^A-Za-z0-9]if[^A-Za-z0-9] |
[^A-Za-z0-9]else[^A-Za-z0-9] |
[^A-Za-z0-9]for[^A-Za-z0-9] |
[^A-Za-z0-9]while[^A-Za-z0-9] |
[^A-Za-z0-9]goto[^A-Za-z0-9] |
[^A-Za-z0-9]continue[^A-Za-z0-9] |
[^A-Za-z0-9]break[^A-Za-z0-9] |
[^A-Za-z0-9]union[^A-Za-z0-9] |
[^A-Za-z0-9]switch[^A-Za-z0-9] |
[^A-Za-z0-9]case[^A-Za-z0-9] |
[^A-Za-z0-9]default[^A-Za-z0-9] |
[^A-Za-z0-9]const[^A-Za-z0-9] |
[^A-Za-z0-9]void[^A-Za-z0-9] |
[^A-Za-z0-9]extern[^A-Za-z0-9] |
[^A-Za-z0-9]auto[^A-Za-z0-9] |
[^A-Za-z0-9]static[^A-Za-z0-9] |
[^A-Za-z0-9]do[^A-Za-z0-9] |
[^A-Za-z0-9]return[^A-Za-z0-9] |
[^A-Za-z0-9]enum[^A-Za-z0-9] |
[^A-Za-z0-9]sizeof[^A-Za-z0-9] |
[^A-Za-z0-9]volatile[^A-Za-z0-9] |
[^A-Za-z0-9]register[^A-Za-z0-9] { ++countKey; }

[A-Za-z0-9] {++countId;}

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
