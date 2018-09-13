Hello, I'm Zach or u/leonidizzil
I wrote this script to make Table Top Gaming more accessible for the visually impaired. This Python script generates and reads a list of dice, bonuses and descriptions, then uses text to speech to announce the roll and description.

You can view the customization options below, or in the stats.txt file which is automatically generated.


below is an example of a functioning macro

####################
###	a,1d20cs19+5 #Longsword Attack
####################

The first letter indicates which letter on the keyboard you would prefer to use

The number immediately following the comma indicates how many dice should be rolled. in this case, we've chosen 1, but 
placing something such as 4d here would also be acceptable

After the 'd' you'll find the size of the die, or which range between 1 and a variable you would like to use. In this case
the possible die results range between 1 and 20.

The number after cs indicates which number, if equalled or succeeded, would result in a critical hit. You do not need to
specify this number. If left blank, the program will announce a natural critical hit of 20.

After the + sign, you will find the bonus you would like added on to the roll. Note that this bonus is added after the
total value of all dice are rolled, and is therefore applied once. You must have at least a bonus of +0, or the program will
crash.

See some more examples below.




a,1d20cs19+5 #Longsword Attack
s,1d8+3 #Longsword Damage
d,1d20+5 #Crossbow Attack
f,1d8+1 #Crossbow Damage
g,1d20+8 #Perception Check
h,4d6+0 #Fireball dee see 19
j,1d20+5 #Fortitude Save
k,1d20+2 #Will Save
l,1d20+4 #Reflex Save
;,1d20+5 #Combat Maneuver Bonus


q,1d20cs15+6 #+1 Keen Scimitar
w,1d6+5 #Scimitar Damage
