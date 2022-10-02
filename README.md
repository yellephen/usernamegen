# usernamegen

Python script that generates usernames based on first and last name. Other options available as below.

```
usage: usernamegen.py [-h] [-f FIRSTNAME] [-l LASTNAME] [-i INFILE] [-d DELIMETERS] [-o DOMAINSUFFIX] [-c] [-s SUFFIXCOUNT]

options:
  -h, --help            show this help message and exit
  -f FIRSTNAME, --firstname FIRSTNAME
                        The first name to use in the combination.
  -l LASTNAME, --lastname LASTNAME
                        The last name to use in the combination.
  -i INFILE, --infile INFILE
                        [Optional]One entry on each line. Space delimited FirstName LastName.
  -d DELIMETERS, --delimeters DELIMETERS
                        [Optional] Delimeters to use in the output. Defaults to '._-'
  -o DOMAINSUFFIX, --domainsuffix DOMAINSUFFIX
                        [Optional] Domain suffix to append to the end of the output.
  -c, --includecasing   [Optional] If specified, includes uppercase variants.
  -s SUFFIXCOUNT, --suffixcount SUFFIXCOUNT
                        [Optional] If specified will append incrementing digits up to and including the specified number.

 ```
