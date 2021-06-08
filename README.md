# string-matching
Fuzzy string matching using Levenshtein distance

## Execution
1. Clone the repo
2. Run the 'run' file

```console
$ python3 run.py
```

3. Enter a sample string to match

## Sample Output

```console
Enter a string to validate :: honesy is the best polic

-------------------------------------------------------
| Original Word |   Dictionary Word 	|    Ratio     |
-------------------------------------------------------
| honesy                honesty               0.923     
-------------------------------------------------------
| is                    is                    1.0       
-------------------------------------------------------
| the                   the                   1.0       
-------------------------------------------------------
| best                  best                  1.0       
-------------------------------------------------------
| polic                 policy                0.909     
-------------------------------------------------------

```