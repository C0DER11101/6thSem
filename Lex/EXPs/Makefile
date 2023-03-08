depend=lex.yy.c
output=a.out

$(output): $(depend)
	gcc $(depend) -ll

$(depend): $(f)
	lex $(f)

.PHONY: clean

clean:
	-rm $(depend) $(output)
