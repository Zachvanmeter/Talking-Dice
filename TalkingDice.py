import random
import msvcrt
from win32com.client import Dispatch
import traceback 
import time
import os
import glob
#
#	pyinstaller --onefile --icon=Data\d20.ico Data\TalkingDice.py
#

#$ I'd like to change the keypress dection method to enable the use of specialty keys(end, ins, arrow keys)

#$ implement Accessible Output 2, which offers braille support
	#it seems like Accessible output isnt Python 3 compatible?

def domytexttospeech(total,aug,mytext):		#I believe this is windows specific, would love 
	global enabletts						#to implement similar iOS, linux functions
	print(mytext,total)
	try:				
		if enabletts == True:
			speak = Dispatch("SAPI.SpVoice")
			speak.Speak(aug+mytext)
			speak.Speak(str(total))
		else:
			pass
	except Exception as e:
		tb = traceback.format_exc(2)
		handleerror(tb, e, e, 'domytexttospeech')
	
def generateroll(maths):	
	try:
		aug=''
		total=0
			#$#$#$#$#$#$#$#$#$
		maths,sep,mytext=maths.partition('#')
		mytext=mytext.replace('\n','')
		maths=maths.replace(' ','')
		if '+' in maths:
			die,sep,bonus=maths.partition('+')
			if bonus == '':
				bonus='0'
		elif '-' in maths:
			die,sep,bonus=maths.partition('-')
			if bonus == '':
				bonus='0'
			bonus=str(int(bonus)*-1)
		else:
			die = maths
			bonus = '0'
			
		count,sep,sizeCS=die.partition('d')
		size,sep,crit=sizeCS.partition('cs')
		
		for x in range(int(count)):	
			roll=random.randint(1,int(size))
			total+=roll		
			if size=='20':		
				if roll == 20:					#I put this bit in because people may want to track
					aug = 'Nat Twenty '			#critical failures and successes
				elif roll == 1:
					aug = 'Nat Zero '
				elif 'cs' in die:
					if roll >= int(crit):
						aug = 'Critical Hit '
		total+=int(bonus)
		return total,aug,mytext
	except Exception as e:
		tb = traceback.format_exc(2)
		handleerror(tb, e, 'generateroll')
		
def doloop(mydict):
	try:
		while True:
			try:
				if msvcrt.kbhit():					#not perfect, cant detect arrow keys without error
					keypress = msvcrt.getch().decode("utf-8") 
					if not '\\' in keypress:
						#print(keypress)
						keypress = str(keypress)
						for key, value in mydict.items():
							if keypress == key:
								total,aug,mytext = generateroll(value)
								domytexttospeech(total,aug,mytext)
					#print(keypress)
					if keypress == '\r':
						global enabletts
						if enabletts == True:
							mytext='Text to Speech is disabled'
							domytexttospeech('','',mytext)
							enabletts=False
						else:
							enabletts=True
							mytext='Text to Speech is enabled'
							domytexttospeech('','',mytext)
						
			except UnicodeDecodeError:				
				pass
			time.sleep(.5)
	except Exception as e:
		tb = traceback.format_exc(2)
		handleerror(tb, e, 'doloop')
						
def getstats():		
	x=0
	chardict={}
	readdict={}
	for filename in glob.iglob('Characters//*.txt', recursive=True):
		x+=1
		dir,sep,file=filename.partition('\\')
		#mytext='Press '+str(x)+' for '+file
		#domytexttospeech('','',mytext)
		readdict[str(x)] = file
		chardict[str(x)] = filename
	if x==0:
		return 'Characters//MyCharStats.txt'
	if x==1:
		return filename
	mychars=''
	for key, value in readdict.items(): 
		mychars=mychars+str('Press '+key+' for '+value+'\n')#readdict)
	mytext = mychars
	domytexttospeech('','',mytext)
	while True:
		try:
			if msvcrt.kbhit():					#not perfect, cant detect arrow keys without error
				keypress = msvcrt.getch().decode("utf-8") 
				if not '\\' in keypress:
					keypress = str(keypress)
					for key, value in chardict.items():
						if keypress == key:
							return value
					if keypress == '\r':
						global enabletts
						if enabletts == True:
							mytext='Text to Speech is disabled'
							domytexttospeech('','',mytext)
							enabletts=False
						else:
							enabletts=True
							mytext='Text to Speech is enabled'
							domytexttospeech('','',mytext)
		except UnicodeDecodeError:
			pass
						
def ensure_dir():
	file_path='Characters//'
	directory = os.path.dirname(file_path)
	if not os.path.exists(directory):
		os.makedirs(directory)
	value = getstats()
	return value
	
def checkstats():								#This exists to establish an example file if the 
	try:										#stats.txt file does not exist
		path = ensure_dir()
		try:
			with open(path, 'r') as f:
				pass
		except FileNotFoundError:
			mylist = [
				'#Get help and check for updates at',
				'#https://github.com/Zachvanmeter/Talking-Dice',
				'#Shortcut, Die roll, Bonus',
				'',
				'#Press Enter to toggle Text to Speech',
				'',
				'1, 1d4 #d4',
				'2, 1d6 #d6',
				'3, 1d8 #d8',
				'4, 1d10 #d10',
				'5, 1d12 #d12',
				'6, 1d20 #d20',
				'7, 1d100 #d100',
				'a, 1d20cs19+5 #Longsword Attack',
				's, 1d8+3 #Longsword Damage',
				'd, 1d20+5 #Crossbow Attack',
				'f, 1d8+1 #Crossbow Damage',
				'g, 1d20+8 #Perception Check',
				'h, 4d6 #Fireball dee see 19',
				'j, 1d20+5 #Fortitude Save',
				'k, 1d20+2 #Will Save',
				'l, 1d20+4 #Reflex Save',
				';, 1d20+5 #Combat Maneuver Bonus',
				'',
				'',
				'q,1d20cs15+6 #+1 Keen Scimitar',
				'w,1d6+5 #Scimitar Damage'
				]
			with open(path, 'a') as f:
				for line in mylist:
					f.write(line+'\n')
		mydict={}
		with open(path, 'r') as f:
			lines=f.readlines()
		for line in lines:
			if not line[0] == '#' and not len(line)<5:
				shortcut,sep,maths=line.partition(',')
				mydict[shortcut] = maths
		return mydict
	except Exception as e:
		tb = traceback.format_exc(2)
		handleerror(tb, e, 'checkstats')
					
def launch():
	try:
		
		mydict = checkstats()
		mytext = 'Talking Dice is running...'
		domytexttospeech('','',mytext)
		#print(mydict)
		doloop(mydict)
	except Exception as e:
		tb = traceback.format_exc(2)
		handleerror(tb, e, 'launch')	
	
def handleerror(tb, e,func):					#this is my prefered method of exception handling,  
		print(tb)								#as it allows users to report their issues more 
		print(e)								#clearly and without immediately crashing the program
		mytext = 'An error has occured. Press Enter to close'	
		domytexttospeech('','',mytext)
		input()
		exit()
			


enabletts = True
	
if __name__ == '__main__':
	launch()
