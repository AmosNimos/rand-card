# NOT YET WORKING/COMPLETED
#Fri Jan 29 03:29:31 PM EST 2021
from random import randrange
from random import shuffle
import os
#external dependency
from termcolor import colored, cprint
import namegenerator
from curtsies import Input

print ()

#variables
handOneSize = 0;
handTwoSize = 0;
deckSize = 15;
deck=[]
deckOne = []
handOne = []
healthOne = 100;
healthTwo = 100;
handOneView = ""
handTwoView = ""
cursorX=0;
cursorY=0;
emoji = ["🀄🃏🎴💾💽💿📀⛔?"];
signs = ["[Aries ♈]","[Taurus ♉]","[Gemini ♊]","[Cancer ♋]","[Leo ♌]","[Virgo ♍]","[Libra ♎]","[Scorpius ♏]","[Sagittarius ♐]","[Capricornus ♑]"];
selectionsign = ""
fieldWidth= 5;
fieldHeight = 4;
cardBack="🀄";
cardFront="🃏";
emptySpace="🎴";


class cardMonster:
	def __init__(self, id, attack, deffence, signs, strAffectedBy, defAffectedBy, infAttack, infDeffence):
		self.id = id;
		self.attack = attack;
		self.deffence = deffence;
		self.signs = signs;
		self.strAffectedBy = strAffectedBy;
		self.defAffectedBy = defAffectedBy;
		self.infAttack = infAttack;
		self.infDeffence = infDeffence;
		self.type="monster"
		self.name = namegenerator.gen();

class cardTerrain:
	def __init__(self, id, weakerAgainst, strongerAgainst, infAttack, infDeffence):
		self.id = id;
		self.weakerAgainst = weakerAgainst;
		self.strongerAgainst = strongerAgainst;
		self.infAttack = infAttack;
		self.infDeffence = infDeffence;
		self.type="Terain";
		self.name = namegenerator.gen();

#generate deck
for x in range(deckSize):
	if(round(randrange(0,3))!=0):
		deck.append(cardMonster(x,randrange(0,9),randrange(0,9),randrange(0,9),randrange(0,9),randrange(0,9),randrange(-9,9),randrange(-9,9)));
	else:
		deck.append(cardTerrain(x,randrange(0,9),randrange(0,9),randrange(-9,9),randrange(-9,9)));

shuffle(deck);
deckOne = deck;

shuffle(deck);
deckTwo = deck;

#first Draw phase
handOne = deckOne[-3:];
deckOne = deckOne[:-3];

#first Draw phase
handTwo = deckTwo[-3:];
deckTwo = deckTwo[:-3];

def main():
	with Input(keynames='curses') as input_generator:
		for e in input_generator:
			return e

def displayTop():
	global healthOne
	global healthTwo
	global handTwo
	global handTwoView
	print("Player one health: ["+str(healthOne)+"]");
	print("Player two health: ["+str(healthTwo)+"]");
	print("");
	#player two hand
	handTwoSize=len(handTwo);
	handTwoView="";
	for x in range(handTwoSize):
		handTwoView += cardBack;
	print(handTwoView);

def displayField():
	linetxt="";
	for y in range(fieldHeight):
		linetxt="";
		for x in range(0,fieldWidth):
			#print(str(x)+","+str(y));
			spaceColor='white';
			if x == cursorX and y == cursorY:
				#cursor there
				#spaceColor='red';
				linetxt+=colored(cardFront,spaceColor);
			elif field[x][y]==0:
				#empty there
				linetxt+=colored(emptySpace,spaceColor);
			else:
				#card there
				linetxt+=colored(cardBack,spaceColor);
		print(linetxt);

def displayHandOne():
	global cursorX;
	global cursorY;
	global handOne;
	global handOneView;
	global signs;


	#player one hand
	handOneSize=len(handOne);

	#cursor limitation
	if(cursorX>handOneSize-1 and cursorY==4):
		cursorX=handOneSize-1;

	handOneView="";
	for x in range(handOneSize):
		if x == cursorX and cursorY==4:
			handOneView += cardFront;
		else:
			handOneView += cardBack;
	print(handOneView);


	if cursorY==4:
		print("");
		print("-[Info]-----------------------------------------------");

		if(handOne[cursorX].type=="monster"):
			selectionsign = str(signs[handOne[cursorX].signs]);
			name = str(handOne[cursorX].name);
			print("Name: "+name);
			print("Type: Monster");
			print("Sign: "+selectionsign);
			print("Attack="+str(handOne[cursorX].attack)+" Deffence="+str(handOne[cursorX].deffence));

			#print("defAf: "+str(handOne[cursorX].strAffectedBy))
			#print(str(signs))
			signsAttack = str(signs[handOne[cursorX].strAffectedBy]);
			if(handOne[cursorX].infAttack>0):
				print("Attack +"+str(handOne[cursorX].infAttack)+" against "+signsAttack);
			elif(handOne[cursorX].infAttack<0):
				print("Attack "+str(handOne[cursorX].infAttack)+" against "+signsAttack);

			#print("defAf: "+str(handOne[cursorX].defAffectedBy))
			#print(str(signs))
			signsDeffence = str(signs[handOne[cursorX].defAffectedBy]);
			if(handOne[cursorX].infDeffence>0):
				print("Deffence +"+str(handOne[cursorX].infDeffence)+" against "+signsDeffence);
			elif(handOne[cursorX].infDeffence<0):
				print("Deffence "+str(handOne[cursorX].infDeffence)+" against "+signsDeffence);
		else:
			print("Card type: Terrain");
			print("id="+str(handOne[cursorX].id)+" attack="+str(handOne[cursorX].weakerAgainst)+" deffence="+str(handOne[cursorX].strongerAgainst));

def playerOneTurn(keypress):
	global cursorX;
	global cursorY;
	if keypress == 'd':
		cursorX+=1;
		debug = "Move Right";
	if keypress == 'a':
		cursorX-=1;
		debug = "Move Left";
	if keypress == 'w':
		cursorY-=1;
		debug = "Move Up";
	if keypress == 's':
		cursorY+=1;
		debug = "Move Down";
	if keypress == '\x1b':
		debug = "Exit";
		print(debug)
		exit();

#field
field=[[0,0,1,1],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]];

#Get keypress from the main function

os.system('clear')
displayTop();
print("");
displayField();
print("");
displayHandOne();

while True:
	keypress = main();
	playerOneTurn(keypress);
	if(cursorX<0):
		cursorX=0;
	if(cursorY<0):
		cursorY=0;
	if cursorX>fieldWidth-1 and cursorY<fieldHeight:
		cursorX=fieldWidth-1;
	if cursorY>fieldHeight:
		cursorY=fieldHeight;
	os.system('clear');
	displayTop();
	print("");
	displayField();
	print("");
	displayHandOne();
