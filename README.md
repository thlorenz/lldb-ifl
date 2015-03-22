# lldb-ifl

Adds *gdb* `info registers eflags` feature to lldb.

## Installation

```sh
curl -L https://raw.githubusercontent.com/thlorenz/lldb-ifl/master/ifl.py > ifl.py
```

## Usage

```
(lldb) command script import ifl.py
(lldb) ifl
rflags: 0x0000000000000246 ['PF', 'ZF', 'IF']
```

## Flags Docs

Learn about what the abbreviations mean [on this Flags register page](http://en.wikipedia.org/wiki/FLAGS_register).

How various flags [affect jump instructions](http://unixwiz.net/techtips/x86-jumps.html).

## Caveats

Reserved flags (i.e. Bit# 1) are ignored in the abbreviated output.

## License

MIT
