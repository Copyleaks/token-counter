# Token Counter
Token Counter is a python script written by Copyleaks, to forecast credits usage for source code scans On the Copyleaks platform.

## Usage
```bash
python3 main.py -d /path/to/dir/containing/source/code/files
```

## Example
```bash
python3 main.py -d /path/to/dir/containing/source/code/files
```

<b>output</b>:

```bash
74 files found
*.py:
        Files: 36
        Tokens: 36,960
        Average Token count: 1,027

*.cs:
        Files: 21
        Tokens: 9,301
        Average Token count: 443

*.java:
        Files: 2
        Tokens: 6,189
        Average Token count: 3,095

*.js:
        Files: 5
        Tokens: 937
        Average Token count: 188

*.css:
        Files: 1
        Tokens: 125
        Average Token count: 125

*.php:
        Files: 2
        Tokens: 576
        Average Token count: 288

*.rb:
        Files: 2
        Tokens: 247
        Average Token count: 124

*.scala:
        Files: 2
        Tokens: 664
        Average Token count: 332

*.swift:
        Files: 2
        Tokens: 1,157
        Average Token count: 579
```

