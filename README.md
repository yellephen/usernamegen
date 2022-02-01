# usernamegen

Python script that generates usernames based on first and last name and optionally middle name. Other options available as below.

```
usage: usernamegen.py [-h] [-m MIDDLENAME] [-d DELIMETERS] [-ds DOMAINSUFFIX] [-i] [-sc SUFFIXCOUNT] [-O OUTFILE] firstname lastname

positional arguments:
  firstname             The first name to use in the gen.
  lastname              The last name to use in the gen.

optional arguments:
  -h, --help            show this help message and exit
  -m MIDDLENAME, --middlename MIDDLENAME
                        [Optional] The middle name to use in the gen.
  -d DELIMETERS, --delimeters DELIMETERS
                        [Optional] Delimeters to use in the gens. Defaults to '._-'
  -ds DOMAINSUFFIX, --domainsuffix DOMAINSUFFIX
                        [Optional] Domain suffix to append to the end of the gens.
  -i, --includecasing   [Optional] If specified, includes uppercase variants.
  -sc SUFFIXCOUNT, --suffixcount SUFFIXCOUNT
                        [Optional] If specified will append digits up to and including input.
  -O OUTFILE, --outfile OUTFILE
                        [optional] If present, output is written to the specified file otherwise to stdout.
 ```
