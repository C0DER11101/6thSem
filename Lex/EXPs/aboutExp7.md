# [exp7.l](https://github.com/C0DER11101/6thSem/blob/6thSem/Lex/EXPs/exp7.l)

Here, I first wrote this:

```lex
^[-][0-9]+ {printf....blah....blah} check in exp7.l
```

`^[-][0-9]+` means any string that starts with a `-` and has one or more digits between `0` and `9`. That means that in a string like this:

`-90 12 -80`

The first number `-90` will be considered as negative because it matches the regex given above, but `-80` will no be taken as negative as it doesn't start with `-` but rather it is just a "substring" of the string that starts with a `-`(for 90). So it doesn't match the pattern given above.

A regex like this:

```lex
[-][0-9]+ |
[ \t\n]+[-][0-9]+ {printf...blah..blah}
```
will match `-80` because here we have not mentioned that the string should start with a `-`. `-90 12 -80`; here `-90` will be considered as negative, `12` will be positive and `-80` will be negative because `-80` is not a subtring of `-90 12 -80`, but instead it's itself a string that has a `-` before it. So it matches the regex: `[-][0-9]+ | [ \t\n]+[-][0-9]+`.


<p align="center">
&#9678; &#9678; &#9678;
</p>
