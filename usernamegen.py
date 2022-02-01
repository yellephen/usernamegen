#!/usr/bin/python3
import sys

def moosh(firstName,lastName):
	output.append(f'{firstName}{lastName}')
	output.append(f'{firstName[0]}{lastName}')
	output.append(f'{firstName}{lastName[0]}')
	output.append(f'{firstName}.{lastName}')
	output.append(f'{firstName[0]}.{lastName}')
	output.append(f'{firstName}.{lastName[0]}')
	output.append(f'{firstName}-{lastName}')
	output.append(f'{firstName[0]}-{lastName}')
	output.append(f'{firstName}-{lastName[0]}')

if len(sys.argv) < 3:
	print("Incorrect number of parameters")
	print("Usage: python3 usernamegen.py [firstname] [lastname]")
	print("or")
	print("Usage: python3 usernamegen.py [firstname] [lastname] [domain]")
	sys.exit()
	

firstName = sys.argv[1].lower()
lastName = sys.argv[2].lower()
domain = ""
if len(sys.argv) == 4:
	domain = sys.argv[3]
output=[]
moosh(firstName,lastName)
moosh((firstName[0].upper() + firstName[1:]),lastName)
moosh((firstName),(lastName[0].upper() + lastName[1:]))

for i in range(len(output)):
	if domain == "":
		print(output[i])
	else:
		print(output[i]+"@"+domain)
