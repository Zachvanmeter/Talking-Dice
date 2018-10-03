Hello, I'm Zach or u/leonidizzil

I wrote this script in the hopes that it make make Table Top Roleplaying games more accessible to the visually impaired. This
program is equiped with its own Text to Speech reader which can be enabled and disabled by pressing the enter key.

You can view the customization options below, or in the MyCharStats.txt file which is automatically generated.

You can fill the characters folder with as many as 10 different characters and macro sets. Once the program loads, if it detects
more than one character, it will assign each character to a number key, and you can pick who you will be playing today.


below is an example of a functioning macro

####################
###	a, 1d20cs19 + 5 #Longsword Attack
####################

The first letter indicates which letter on the keyboard you would prefer to use

The number following the comma indicates how many dice should be rolled. in this case, we've chosen 1, but 
placing any number here would is acceptable

After the 'd' you'll find the size of the die, or a range between 1 and a variable you would like to use. In this case
the possible die results range between 1 and 20.

The number after cs indicates which number, if equalled or succeeded, would result in a critical hit. You do not need to
specify this number. If left blank, the program will announce a natural critical hit of 20.

After the + sign, you will find the bonus you would like added on to the roll. Note that this bonus is added after the
total value of all dice are rolled, and is therefore applied once.

See some more examples below. It is perfectly acceptable to include spaces or notes between the lines of your character's file
provided that the notes begin with the '#' sign

Commands can be bound to the following keys without error: a-z, A-Z, 0-9, `~!@$%^&*()-=_+[]{}\|;':",./<>?
Commands can NOT be bound to advanced keys: #, backspace, enter, arrow keys, function keys, ins, home, del, end, shift, alt, etc

#Update 1.0.3 introduced felxible command lines!
1, 1d4 #d4
2, 1d6-6 #d6
3, 1 d 8  +  0  #d8
4,1d10+ #d10
5, 1d12- #d12
6, 1d20+0 


#This is a good example!
1, 1d4 #d4
2, 1d6 #d6
3, 1d8 #d8
4, 1d10 #d10
5, 1d12 #d12
6, 1d20 #d20
7, 1d100 #d100

#Here are my favorite rolls!
a, 1d20cs19+5 #Longsword Attack
s, 1d8+3 #Longsword Damage
d, 1d20+5 #Crossbow Attack
f, 1d8+1 #Crossbow Damage
g, 1d20+8 #Perception Check

#Sometimes it is nice to spell certain words and abbreviations phonetically!
h, 4d6 #Fireball dee see 19


j, 1d20+5 #Fortitude Save
k, 1d20+2 #Will Save
l, 1d20+4 #Reflex Save
;, 1d20+5 #Combat Maneuver Bonus

#This is my friend's magic weapon, he is letting me borrow it.
q,1d20cs15+6 #+1 Keen Scimitar
w,1d6+5 #Scimitar Damage
