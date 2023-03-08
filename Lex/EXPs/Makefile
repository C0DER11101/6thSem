obj=main.o # just in case there is any need to write C files!!
exe:$(obj)
	gcc $(obj) -o exe

$(obj):$(f)
	gcc -c $(f)

.PHONY: cls

cls:
	-rm $(obj) exe


depend=lex.yy.c
output=a.out

$(output): $(depend)
	gcc $(depend) -ll

$(depend): $(f)
	lex $(f)

.PHONY: clean

clean:
	-rm $(depend) $(output)
