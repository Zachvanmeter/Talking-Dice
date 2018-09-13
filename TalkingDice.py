import random
import msvcrt
from gtts import gTTS
from win32com.client import Dispatch

#
#	pyinstaller --onefile --icon=Data\d20.ico Data\TalkingDice.py
#


def domytexttospeech(total,aug,mytext):		#I believe this is windows specific, would love 
											#if someone could implement a similar iOS function
	speak = Dispatch("SAPI.SpVoice")
	speak.Speak(aug+mytext)
	speak.Speak(str(total))

def generateroll(maths):	
	aug=''
	total=0
	die,sep,tail=maths.partition('+')
	count,sep,sizeCS=die.partition('d')
	size,sep,crit=sizeCS.partition('cs')
	bonus,sep,mytext=tail.partition(' ')
	mytext=mytext.replace('#','').replace('\n','')
	
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
		
def doloop(mydict):
	while True:
		if msvcrt.kbhit():
			keypress = msvcrt.getch()
			keypress = str(keypress).replace("'",'')[1]
			if not '\\' in keypress:
				for key, value in mydict.items():
					if keypress == key:
						total,aug,mytext = generateroll(value)
						print(mytext,total)
						domytexttospeech(total,aug,mytext)
						
def checkstats():							#This exists to establish an example file if the 
											#stats.txt file does not exist
	path='Stats.txt'
	try:
		with open('Stats.txt', 'r') as f:
			pass
	except FileNotFoundError:
		mylist = [
			'#Shortcut, Die roll, Bonus',
			'a,1d20cs19+5 #Longsword Attack',
			's,1d8+3 #Longsword Damage',
			'd,1d20+5 #Crossbow Attack',
			'f,1d8+1 #Crossbow Damage',
			'g,1d20+8 #Perception Check',
			'h,4d6+0 #Fireball dee see 19',
			'j,1d20+5 #Fortitude Save',
			'k,1d20+2 #Will Save',
			'l,1d20+4 #Reflex Save',
			';,1d20+5 #Combat Maneuver Bonus',
			'',
			'',
			'q,1d20cs15+6 #+1 Keen Scimitar',
			'w,1d6+5 #Scimitar Damage'
			]
		with open('Stats.txt', 'a') as f:
			for line in mylist:
				f.write(line+'\n')
					
def go():
	mydict={}
	with open('stats.txt','r') as f:
		lines=f.readlines()
	for line in lines:
		if not line[0] == '#' and not len(line)<5:
			shortcut,sep,maths=line.partition(',')
			mydict[shortcut] = maths
	doloop(mydict)	
			
if __name__ == '__main__':
	checkstats()
	go()
