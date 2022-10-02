#!/usr/bin/python3
import sys
import argparse

def makecombos(firstname,lastname,delimeters,domainsuffix,suffixcount):
	delimeters = list(delimeters)
	delimeters.insert(0,"")
	if suffixcount == None:
		suffixcount = ""
	for delimeter in delimeters:
		print(f'{firstname}{delimeter}{lastname}{suffixcount}{domainsuffix}')
		print(f'{lastname}{delimeter}{firstname}{suffixcount}{domainsuffix}')
		print(f'{firstname[0]}{delimeter}{lastname}{suffixcount}{domainsuffix}')
		print(f'{lastname[0]}{delimeter}{firstname}{suffixcount}{domainsuffix}')
		print(f'{firstname}{delimeter}{lastname[0]}{suffixcount}{domainsuffix}')
		print(f'{lastname}{delimeter}{firstname[0]}{suffixcount}{domainsuffix}')

def makeifcasingcombos(firstname,lastname,delimeters,domainsuffix,suffixcount,includecasing):
	makecombos(firstname,lastname,delimeters,domainsuffix,suffixcount)
	if(includecasing):
		makecombos(firstname.lower().capitalize(),lastname.lower(),delimeters,domainsuffix,suffixcount)
		makecombos(firstname.lower(),lastname.lower().capitalize(),delimeters,domainsuffix,suffixcount)

def do(firstname,lastname,delimeters,domainsuffix,suffixcount,includecasing):
	makeifcasingcombos(firstname,lastname,delimeters,domainsuffix,"",includecasing)
	if suffixcount != 0:
		for i in range(0,suffixcount+1):
			makeifcasingcombos(firstname,lastname,delimeters,domainsuffix,i,includecasing)

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', '--firstname', default="", help="The first name to use in the combination.")
	parser.add_argument('-l', '--lastname', default="", help="The last name to use in the  combination.")
	parser.add_argument('-i', '--infile',default="", help="[Optional]One entry on each line. Space delimited FirstName LastName.")
	parser.add_argument('-d', '--delimeters',default="._-", help="[Optional] Delimeters to use in the output. Defaults to '._-'")
	parser.add_argument('-o', '--domainsuffix',default="", help="[Optional] Domain suffix to append to the end of the output.")
	parser.add_argument('-c', '--includecasing', action="store_true", help="[Optional] If specified, includes uppercase variants.")
	parser.add_argument('-s','--suffixcount', type=int, default=0, help="[Optional] If specified will append incrementing digits up to and including the specified number.")
	args = parser.parse_args()

	if args.infile != "":
		f = open(args.infile, "r")
		for line in f:
			firstname, lastname = line.split(' ')
			lastname=lastname.replace("\n","")
			do(firstname,lastname,args.delimeters,args.domainsuffix,args.suffixcount,args.includecasing)
	else:
		do(args.firstname,args.lastname,args.delimeters,args.domainsuffix,args.suffixcount,args.includecasing)
if __name__ == "__main__":
    main()
