import random
import msvcrt
from win32com.client import Dispatch
import traceback 
#
#	pyinstaller --onefile --icon=Data\d20.ico Data\TalkingDice.py
#

#$ I'd like to change the keypress dection method to enable the use of specialty keys(end, ins, arrow keys)

#$ implement Accessible Output 2, which offers braille support
	#it seems like Accessible output isnt Python 3 compatible?

def domytexttospeech(total,aug,mytext):			#I believe this is windows specific, would love 
												#to implement similar iOS, linux functions
	try:										
		print(mytext,total)
		speak = Dispatch("SAPI.SpVoice")
		speak.Speak(aug+mytext)
		speak.Speak(str(total))
	except Exception as e:
		tb = traceback.format_exc(2)
		handleerror(tb, e, e, 'domytexttospeech')
	
def generateroll(maths):	
	try:
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
	except Exception as e:
		tb = traceback.format_exc(2)
		handleerror(tb, e, e, 'generateroll')
		
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
			except UnicodeDecodeError:				
				pass
	except Exception as e:
		tb = traceback.format_exc(2)
		handleerror(tb, e, 'doloop')
						
def checkstats():								#This exists to establish an example file if the 
	try:										#stats.txt file does not exist
		path='Stats.txt'
		try:
			with open('Stats.txt', 'r') as f:
				pass
		except FileNotFoundError:
			mylist = [
				'#Get help and check for updates at',
				'#https://github.com/Zachvanmeter/Talking-Dice',
				'#Shortcut, Die roll, Bonus',
				'1,1d4+0 #d4',
				'2,1d6+0 #d6',
				'3,1d8+0 #d8',
				'4,1d10+0 #d10',
				'5,1d12+0 #d12',
				'6,1d20+0 #d20',
				'7,1d100+0 #d100',
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
	except Exception as e:
		tb = traceback.format_exc(2)
		handleerror(tb, e, 'checkstats')
					
def launch():
	try:
		mytext = 'Talking Dice is running...'
		domytexttospeech('','',mytext)
		mydict={}
		with open('stats.txt','r') as f:
			lines=f.readlines()
		for line in lines:
			if not line[0] == '#' and not len(line)<5:
				shortcut,sep,maths=line.partition(',')
				mydict[shortcut] = maths
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
			
if __name__ == '__main__':
	checkstats()
	launch()
