# Why yytext[0]???

Turns out that even though _yytext_ is a string(actually a pointer-to-character, not exactly a string), it reads the input string one character at a time.

Suppose the input string is:

`"hello"`

So, initially _yytext_ will be `"h"`(not `'h'` which is a character), next it will be `"e"`. So if we want to access the character rather than the string we need to write `yytext[0]` which basically accesses the character at the $0^{th}$ index.


<p align="center">
&#9678; &#9678; &#9678;
</p>
