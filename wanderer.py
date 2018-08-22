'''
	author: rachel stern & jo ramaswamy
	original version in c started on may 20 2018
	python version started june 6 2018
	last updated july 6 2018
'''

import time
import random
choice0 = 0

inventory = [] #inventory array

def main():
	print "welcome to\n WANDERER"
	time.sleep(1)
	print "instructions: this is a text-based adventure game with snarky commentary. to make a choice, simply type the character corresponding to that choice. enjoy!"
	time.sleep(5)
	print "you're in your room, doing nothing."
	time.sleep(1)
	print "(as usual)"
	time.sleep(1)
	print "why don't you take a walk outside?"
	time.sleep(1)
	print "wait, maybe you should take something with you before you go."
	time.sleep(3)
	print "what do you want to take? \nyour options are: (1) a paintbrush. it's clean... you think. (2) an empty water bottle. maybe you can fill it up with rain? (3) an old map? what area even is this... it doesn't look familiar to you."
	choice0 = input("pick with 1, 2, or 3. ")
	if choice0 == 1:
		choice1 = "the clean paintbrush"
	elif choice0 == 2:
		choice1 = "the empty water bottle"
	elif choice0 == 3:
		choice1 = "the strange map"
	else:
		print "wtf? that's not even an option."
		ending()
		return;
	print "you picked: " + choice1
	inventory.append(choice1)
	#print_inv(inventory)
	choice0=0
	choice1=""
	time.sleep(3)
	print "you walk downstairs, and outside."
	time.sleep(1)
	print "it's still raining. where do you wanna go?"
	time.sleep(1)
	print "1: your backyard. 2: into the woods. 3: go back inside."
	choice0 = input("pick with 1, 2, or 3. ")
	if choice0 == 1:
		choice1 = "your backyard"
		print "you picked: your backyard"
		backyardadventure();
	elif choice0 == 2:
		choice1 = "into the woods"
		print "you picked: into the woods"
		intothewoods()
	else:
		print "well, that's pretty lame."
		ending()

def ending():
	print "cool, that's it. your adventure is over now."
	time.sleep(1)
	print "thanks for playing."
	time.sleep(2)
	print ("now, you should go on a /real/ adventure.")
	return "bye."

def print_inv(inventory):
	print "so far, your inventory contains: "
	for i in inventory:
		print i+", "

def backyardadventure():
	print "well here you are... your backyard."
	time.sleep(2)
	print "the only thing of interest here is a strange tree that, oddly enough, you feel you haven't seen before. go check it out."
	time.sleep(2)
	print "there's a branch on the ground. you take it."
	inventory.append("the broken branch")
	print_inv(inventory)
	time.sleep(2)
	print "there's a split in the tree, large enough to fit a human. wanna go investigate? "
	choice0 = 0
	choice0 = input("1 (yes) or 2 (no)? ")
	if choice0 == 1:
		print "you decided to go investigate the split inside the tree."
		time.sleep(2)
		print "nervously, you edge closer... and peer inside."
		time.sleep(2)
		print "you can't see anything inside there... you lean into it just a bit more..."
		time.sleep(2)
		print "suddenly, you lose your balance, and fall in!"
		time.sleep(3)
		print "..."
		time.sleep(2)
		print "..."
		time.sleep(2)
		print "at what seems to be the bottom of a pit, you gain your bearings."
		time.sleep(2)
		print "it sure is dark in here."
		time.sleep(2)
		print "you feel around in the darkness for something... anything..."
		time.sleep(2)
		print "your hand touches something. a box?"
		time.sleep(2)
		print "you pick it up, and shake it. seems like it's a box of matches."
		time.sleep(2)
		print "there's eleven matches inside. you decide to take the box."
		time.sleep(2)
		nomatches = 11
		inventory.append("a box of matches")
		print_inv(inventory);
		time.sleep(2)
		"{} {}".format("# of matches you have left: ", nomatches)
		time.sleep(2)
		print "light one? it could help you find your way around. "
		choice0 = input("1 (yes) or 2 (no)? ")
		if choice0 == 1:
			nomatches-=1
			print "you lit a match."
			print "{} {}".format("# of matches you have left: ", nomatches)
			litamatch(nomatches)
		else:
			print "no? guess you'll never find your way out of here."
			ending()
	else:
		ending()

def litamatch(nomatches):
	time.sleep(2)
	print "through the limited glow of the match, you begin to make out your surroundings."
	time.sleep(2)
	print "it seems like a maze..."
	time.sleep(2)
	print "make your decisions quickly. one match will last for one decision, and you can make decisions until you run out of matches."
	time.sleep(2)

	correct_guess = 0

	while (1):
		if nomatches == 0:
			print "you don't have any matches left. isn't that a shame?"
			time.sleep(2)
			print "guess you'll never find your way out of here."
			return ending()

		right_decision = random.randint(0,1)
		choice0 = input("0 (left) or 1 (right)? ")

		if choice0 == right_decision:
			correct_guess = correct_guess + 1
			if correct_guess == 5:
				break

		nomatches = nomatches - 1
		#print "{} {}".format("the right decision was: + ", right_decision)
		print "{} {}".format("# of matches you have left: ", nomatches)
	outofmaze()

# test this part!!!
def intothewoods():
	print "you enter the woods."
	time.sleep(2)
	print "the atmosphere is slowly becoming more and more mysterious."
	time.sleep(2)
	print "have you been here before?"
	time.sleep(2)
	print "or do the trees all look the same?"
	time.sleep(2)
	print "it's hard to tell."
	time.sleep(2)
	print "suddenly, you hear a voice..."
	time.sleep(2)
	print "\"...Oh! Hello! Pardon my manners... it has been so long since anyone has come to these parts.\""
	time.sleep(2)
	print "you look around. who is that talking?"
	time.sleep(2)
	print "\"That said... what could you be doing here? There isn't much to see, or do.\""
	time.sleep(2)
	print "you look down, and see a small man, as tall as your shoe. he has a long beard and green hat. he reminds you of a wizard."
	time.sleep(2)
	print "he continues... \"Still, you still insist on going forward? Interesting.... you have piqued my interest, wanderer.\""
	time.sleep(2)

def outofmaze():
	print "good job, you made it out of the maze."
	time.sleep(2)
	print "in your haste to get as far from the maze as possible, you dropped the box of matches..."
	time.sleep(2)
	inventory.pop()
	print_inv(inventory)

main()
