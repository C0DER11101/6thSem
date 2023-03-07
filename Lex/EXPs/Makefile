depend=lex.yy.c
output=a.out

$(output): $(depend)
	gcc $(depend) -ll

$(depend): $(File)
	lex $(File)

.PHONY: clean

clean:
	-rm $(depend) $(output)
