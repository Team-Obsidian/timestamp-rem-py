#hello :)
import os
from pathlib import Path

quitProgram = False

def clear():
	# Clear Windows command prompt.
	if (os.name in ('ce', 'nt', 'dos')):
	    os.system('cls')

	# Clear the Linux terminal.
	elif ('posix' in os.name):
	    os.system('clear')

	else:
		print('you\'ve got a weird OS, comrade...')
		print("\n"*20)

def checkItem(fileName=''):
	global quitProgram

	if fileName == '':
		fileName = input('input name of file: ')
	else:
		print(f'auto-processing chosen file {fileName}')

	try:
		if fileName == 'exit':
			#print(f'quitProgram is {quitProgram}')
			quitProgram = True
		else:
			chooseDirect = Path(fileName)
			contents = chooseDirect.read_text().splitlines()#
			#print(f'contents are {contents}')
			tempString = ''
			for line in contents:
				tempString += f'{line[10:]}\n'
			Path(f'output/{fileName}-modified.txt').write_text(f'{tempString}\n')
			print('thing complete! files are stored in /output')
	except FileNotFoundError:
		clear()
		print('sorry, no file was found... let\'s try again.\n\n')
		#quitProgram = True

def checkFolder():
	global quitProgram

	inDirectory = input('Insert your directory here: ')
	if inDirectory == 'exit' or inDirectory == 'quit':
		quitProgram = True
	else:
		if inDirectory == '':
			inDirectory = '.'
		fileType = input('what file extension do you want?\n')
		inDirectory = Path(inDirectory)
		print('Here are your files.\n')
		allFiles = list(inDirectory.glob(f'*.{fileType}'))
		for fileName in allFiles:
			print(fileName)
		print('')

		toContinueLoop = True
		while toContinueLoop:
			toContinue = input('would you like to process them? [Y]es or [N]o\n').lower()
			if toContinue == 'y':
				print('cool!')
				toContinueLoop = False
				for fileName in allFiles:
					checkItem(fileName)
			elif toContinue == 'n':
				print('alright then.')
				toContinueLoop = False
				quitProgram = True
			else:
				pass
		#print(f'your inDirectory is {inDirectory}')




programType = input('Which program type do you want?\n\n1. Folder Scan\n2. Item Print\n\n')
if programType == 'exit':
	quitProgram = True
clear()

while quitProgram == False:
	if programType == '1':
		checkFolder()
	elif programType == '2':
		checkItem()
clear()
print('exiting program. thank you~!')
