#!/usr/bin/python3
import sys
import argparse

def moosh(firstName,lastName,middleName,delimeters):
	output=[]
	output.append(f'{firstName}{lastName}')
	if middleName != "":
		output.append(f'{firstName}{middleName[0]}{lastName}')
	for delimeter in delimeters :
		output.append(f'{firstName[0]}{delimeter}{lastName}')
		output.append(f'{firstName}{delimeter}{lastName[0]}')
		if middleName != "":
			output.append(f'{firstName}{delimeter}{middleName[0]}{delimeter}{lastName}')
			output.append(f'{firstName}{middleName[0]}{delimeter}{lastName}')				
	return output

class InputName:
	def __init__(self, *args):
		if len(args) == 3:
			self.firstName = args[0]
			self.middleName = args[1]
			self.lastName = args[2]
		elif len(args) == 1:
			if len(args[0]) == 2:
				self.firstName = args[0][0]
				self.lastName = args[0][1]
				self.middleName = ""
			elif len(args[0]) == 3:
				self.firstName = args[0][0]
				self.middleName = args[0][1]
				self.lastName = args[0][2]

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('firstname', help="The first name to use in the gen.")
	parser.add_argument('lastname', help="The last name to use in the  gen.")
	parser.add_argument('-I', '--infile',default="", help="[Optional]Space or comma delimited [FirstName][MiddleName][LastName] or [FirstName][LastName]")
	parser.add_argument('-m', '--middlename', default="", help="[Optional] The middle name to use in the  gen.")
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
	inFile = args.infile
	outFile = args.outfile
	output=[]

	inputNames = []

	if inFile != "":
		f = open(inFile, "r")
		for line in f:
			lineStripped = line.replace(","," ")
			lineStripped = lineStripped.replace("\n","")
			lineStripped = lineStripped.split(" ")
			if lineStripped != ['']:
				inputNames.append(InputName(lineStripped))
	else:
		inputNames.append(InputName(firstName,middleName,lastName))

	for name in inputNames:
		output.extend(moosh(name.firstName, name.lastName, name.middleName, delimeters))
		if includeCasing:
			output.extend(moosh(name.firstName.capitalize(),name.lastName, name.middleName, delimeters))
			output.extend(moosh(name.firstName,name.lastName.capitalize(), name.middleName, delimeters))
			output.extend(moosh(name.firstName.capitalize(),name.lastName.capitalize(), name.middleName, delimeters))
			output.extend(moosh(name.firstName.capitalize(),name.lastName, name.middleName.capitalize(), delimeters))

		suffixAdditions = []
		if suffixCount != None:
			for i in range(len(output)):
					for j in range(suffixCount+1):
						suffixAdditions.append(f'{output[i]}{j}')
			output.extend(suffixAdditions)

		if domain != "":
			for i in range(len(output)):
					output[i] = f'{output[i]}@{domain}'

	#There are a few dupes due to calling moosh with capitlised middlename and moosh adding first+last. Dedupe here.
	output = list(set(output))

	for i in range(len(output)):
		if outFile != "":
			with open(outFile,'a') as f:
				f.write(output[i])
				f.write("\n")
		else:
			print(output[i])

if __name__ == "__main__":
    main()