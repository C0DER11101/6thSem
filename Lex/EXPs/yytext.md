# Observation

_yytext_ changes its nature depending on the pattern provided to it.

Suppose the pattern provided is:

```lex
[a-z] {..some action...}
```
`[a-z]` means any character between `a and z`(both inclusive). Since it's "any character", so _yytext_ characters read will be stored only in the $0^{th}$ index i.e. it will read one character at a time and each character read will be stored in the $0^{th}$ index.

But if the pattern is:
```lex
[0-9]+ {..some action..}
```
Then the input string will be stored in consecutive indices.

Say, if the input string for the pattern above is: `0912`, then this string will be stored as:
```
yytext[0]='0', yytext[1]='9', yytext[2]='1', yytext[3]='2'
```
because the pattern above means "one or  more digits between 0 and 9(both inclusive)".

Now, what I said in [Note.md](https://github.com/C0DER11101/6thSem/blob/6thSem/Lex/EXPs/Note.md) was for patterns similar to the pattern `[a-z]`.

# More observation

Consider a pattern:

```lex
[-+*/]*[A-Za-z0-9][-+*/]*
```

`[-+*/]*` means 0 or more occurrences of either - or + or * or /.
`[A-Za-z0-9]` means one or more alphanumeric characters.

Here _yytext_ will change its way of storing the input string according to the pattern above.

Say, the input string is `hello` then _yytext_ will store the input string as:

```
first character: yytext[0]='h', next character: yytext[0]='e', next character: yytext[0]='l', and so on...
```

But if the input string is `a+b`

Then:
```
yytext[0]='a', yytext[1]='+' and yytext[0]='b'
```


Consider this pattern:
```lex
[A-Za-z0-9][-+*/]*[A-Za-z0-9] {..some action..}
```

Here for the input string: `hello`, _yytext_ will store it like this:
```
yytext[0]='h'(matches the first [A-Za-z0-9]), yytext[1]='e'(matches the second [A-Za-z0-9]). After this again:

yytext[0]='l'(again matches the first [A-Za-z0-9]), yytext[1]='l'(matches the second [A-Za-z0-9]). Again:

yytext[0]='o'(matches the first [A-Za-z0-9]). But keep in mind when you press enter key, then a newline character will be taken as input and for 'o' even though it mathces the first [A-Za-z0-9] the newline character won't match the second [A-Za-z0-9] and so 'o' along with the newline character will be discarded. Here it's shown just for explanation purpose.
```

For the string: `a+b-c`, _yytext_ will store it as:

```
yytext[0]='a'(mathces first [A-Za-z0-9]), yytext[1]='+'(matches [-+*/]*) and yytext[2]='b'(matches second [A-Za-z0-9])

reaches '-' and checks in the first [A-Za-z0-9] which results in failure in matching('-' is a symbol) so no more input is taken.
```
_yytext_ discards taking '-' and 'c' as inputs(it's much like DFA(here it's like epsilon NFA as there is an epsilon transition), where after taking one character we move back to previous state in some cases).

<p align="center">
&#9678; &#9678; &#9678;
</p>
