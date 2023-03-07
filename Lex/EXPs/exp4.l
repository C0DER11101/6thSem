/* Simply read a file and display */

%{
	char ch;
%}

%%

%%


int main(void)
{
	FILE* fout=fopen("test.txt", "r");

	while((ch=fgetc(fout))!=EOF)
		printf("%c", ch);

	
	fclose(fout);

	return 0;
}
