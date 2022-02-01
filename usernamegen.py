#!/usr/bin/python3
import sys
import argparse

def moosh(firstName,lastName,middlename,delimeters):
	delimeters.append("")
	for delimeter in delimeters :
		output.append(f'{firstName}{delimeter}{lastName}')
		output.append(f'{firstName[0]}{delimeter}{lastName}')
		output.append(f'{firstName}{delimeter}{lastName[0]}')
		if middleName != None:
			if(delimeter == ""):
				output.append(f'{firstName}{middleName[0]}{lastName}')
			else:
				output.append(f'{firstName}{delimeter}{middleName[0]}{delimeter}{lastName}')
				output.append(f'{firstName}{middleName[0]}{delimeter}{lastName}')
				output.append(f'{firstName}{middleName[0]}{lastName}')

parser = argparse.ArgumentParser()
parser.add_argument('firstname', help="The first name to use in the gen.")
parser.add_argument('lastname', help="The last name to use in the  gen.")
parser.add_argument('-m', '--middlename', help="[Optional] The middle name to use in the  gen.")
parser.add_argument('-d', '--delimeters',default="._-", help="[Optional] Delimeters to use in the gens. Defaults to '._-'")
parser.add_argument('-ds', '--domainsuffix',default="", help="[Optional] Domain suffix to append to the end of the gens.")
parser.add_argument('-i', '--includecasing', action="store_true", help="[Optional] If specified, includes uppercase variants.")
parser.add_argument('-sc','--suffixcount', type=int, help="[Optional] If specified will append digits up to and including input.")
parser.add_argument('-O', '--outfile', default="", help="[optional] If present, output is written to the specified file otherwise to stdout.")
args = parser.parse_args()

firstName = args.firstname.lower()
lastName = args.lastname.lower()
middleName = args.middlename
if middleName != None:
	middleName = middleName.lower()
domain = args.domainsuffix
delimeters = list(args.delimeters)
includeCasing = args.includecasing
suffixCount = args.suffixcount
outFile = args.outfile
output=[]

print("usernamegen. mooshing names.")

moosh(firstName, lastName, middleName, delimeters)

if includeCasing:
	moosh((firstName[0].upper() + firstName[1:]),lastName, middleName, delimeters)
	moosh((firstName),(lastName[0].upper() + lastName[1:]), middleName, delimeters)
	moosh((firstName[0].upper() + firstName[1:]),(lastName[0].upper() + lastName[1:]), middleName, delimeters)
	if middleName != None:
		moosh((firstName[0].upper() + firstName[1:]),lastName, (middleName[0].upper() + middleName[1:]), delimeters)

suffixAdditions = []
if suffixCount != None:
	for i in range(len(output)):
			for j in range(suffixCount+1):
				suffixAdditions.append(f'{output[i]}{j}')
	output.extend(suffixAdditions)

if domain != "":
	for i in range(len(output)):
			output[i] = f'{output[i]}@{domain}'

for i in range(len(output)):
	if outFile != "":
		with open(outFile,'a') as f:
			f.write(output[i])
			f.write("\n")
	else:
		print(output[i])

print("Done")