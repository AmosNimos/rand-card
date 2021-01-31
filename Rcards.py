# NOT YET WORKING/COMPLETED
#Fri Jan 29 03:29:31 PM EST 2021
from random import randrange
from random import shuffle
import os
#external dependency
from termcolor import colored, cprint
import namegenerator
from curtsies import Input

#variables
handOneSize = 0;
handTwoSize = 0;
deckSize = 12;
handLimit = 6;
firstDraw=3;
deck=[]
deckOne = [];
handOne = [];
healthOne = 100;
healthTwo = 100;
handOneView = "";
handTwoView = "";
cursorX=0;
cursorY=0;
selectionsign = "";
fieldWidth= 5;
fieldHeight = 4;
infoText="";
lineEnd = "\n";
margin = "  ";
playerOne="";
playerOnePick="";
playerTwoPick="";
playerTurn = randrange(0,2);

if(playerTurn==0):
	playerOneDrew=False;
	playerTwoDrew=True;
else:
	playerOneDrew=True;
	playerTwoDrew=False;
#field
field=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]];

# symbol
cantPlaceSymbol = "x" #red
lookAtCardSymbol = "?" #green for monster and yellow for Terrain
holdingCardSymbol ="%" #green for monster and yellow for Terrain
cursorSymbol = "*" #white for empty
monsterCardSymbol = "#" #green for monster
TerrainCardSymbol = "@" #yellow for Terrain
cardBackSymbol="⬜";
cardFrontSymbol="💠";
emptySpaceSymbol="⬛";
signs = ["[Aries ♈]","[Taurus ♉]","[Gemini ♊]","[Cancer ♋]","[Leo ♌]","[Virgo ♍]","[Libra ♎]","[Scorpius ♏]","[Sagittarius ♐]","[Capricornus ♑]","Aquarius ♒", "[Pisces ♓],[Ophiuchus ⛎]"];
emoji = ["🀄🃏🎴💾💽💿📀⛔?🔳⬛⬜"];


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
	def __init__(self, id, defAffectedBy, strAffectedBy, infAttack, infDeffence):
		self.id = id;
		self.defAffectedBy = defAffectedBy;
		self.strAffectedBy = strAffectedBy;
		self.infAttack = infAttack;
		self.infDeffence = infDeffence;
		self.type="Terain";
		self.name = namegenerator.gen();

#generate deck
for x in range(deckSize):
	if(round(randrange(0,3+1))!=0):
		deck.append(cardMonster(x,randrange(0,9),randrange(0,9),randrange(0,9),randrange(0,9),randrange(0,9),randrange(-9,9),randrange(-9,9)));
	else:
		deck.append(cardTerrain(x,randrange(0,9),randrange(0,9),randrange(-9,9),randrange(-9,9)));

shuffle(deck);
deckOne = deck;

shuffle(deck);
deckTwo = deck;

#first Draw phase
handOne = deckOne[-firstDraw:];
deckOne = deckOne[:-firstDraw];

#first Draw phase
handTwo = deckTwo[-firstDraw:];
deckTwo = deckTwo[:-firstDraw];

def main():
	with Input(keynames='curses') as input_generator:
		for e in input_generator:
			return e

def displayTop():
	global healthOne
	global healthTwo
	global handTwo
	global handTwoView
	print("")
	print(margin+"Turn: "+str(playerTurn));
	print(margin+"Player one health: ["+str(healthOne)+"]");
	print(margin+"Player two health: ["+str(healthTwo)+"]");
	print("");
	#player two hand
	handTwoSize=len(handTwo);
	handTwoView="";
	for x in range(handTwoSize):
		handTwoView += cardBackSymbol;
	while(len(handTwoView)<handLimit):
		handTwoView+=emptySpaceSymbol;
	print(margin+handTwoView);

def displayField():
	global infoText;
	linetxt="";
	for y in range(fieldHeight):
		linetxt="";
		for x in range(0,fieldWidth):
			#print(str(x)+","+str(y));
			spaceColor='white';
			if x == cursorX and y == cursorY:
				#cursor there
				#spaceColor='red';
				linetxt+=colored(cardFrontSymbol,spaceColor);
				if field[x][y]!=0:
					infoText = getInfo(field[x][y]);
				else:
					infoText = "";
			elif field[x][y]==0:
				#empty there
				linetxt+=colored(emptySpaceSymbol,spaceColor);
			else:
				#card there
				linetxt+=colored(cardBackSymbol,spaceColor);

		print(margin+linetxt);

def displayHandOne():
	global cursorX;
	global cursorY;
	global handOne;
	global handOneView;
	global signs;
	global infoText;


	#player one hand
	handOneSize=len(handOne);

	#cursor limitation
	if(cursorX>handOneSize-1 and cursorY==4):
		cursorX=handOneSize-1;

	handOneView="";
	for x in range(handOneSize):
		if x == cursorX and cursorY==4:
			handOneView += cardFrontSymbol;
		else:
			handOneView += cardBackSymbol;
	while(len(handOneView)<handLimit):
		handOneView+=emptySpaceSymbol;
	print(margin+handOneView);


	if cursorY==4 and len(handOne)>0:
		infoText = getInfo(handOne[cursorX]);

def getInfo(getPos):
	infoText = "";
	if(getPos!=0):
		if(getPos.type=="monster"):
			selectionsign = str(signs[getPos.signs]);
			name = str(getPos.name);
			infoText += margin+"Name: "+name + lineEnd;
			infoText += margin+"Type: Monster" + lineEnd;
			infoText += margin+"Sign: "+selectionsign + lineEnd;
			infoText += margin+"Attack="+str(getPos.attack)+" Deffence="+str(getPos.deffence) + lineEnd;
			infoText += margin+"Effect:"+ lineEnd;
			#print("defAf: "+str(handOne[cursorX].strAffectedBy))
			#print(str(signs))
			signsAttack = str(signs[getPos.strAffectedBy]);
			if(getPos.infAttack>0):
				infoText += margin+"Attack +"+str(getPos.infAttack)+" against "+signsAttack + lineEnd;
			elif(getPos.infAttack<0):
				infoText += margin+"Attack "+str(getPos.infAttack)+" against "+signsAttack + lineEnd;

			#print("defAf: "+str(handOne[cursorX].defAffectedBy))
			#print(str(signs))
			signsDeffence = str(signs[getPos.defAffectedBy]);
			if(getPos.infDeffence>0):
				infoText += margin+"Deffence +"+str(getPos.infDeffence)+" against "+signsDeffence + lineEnd;
			elif(getPos.infDeffence<0):
				infoText += margin+"Deffence "+str(getPos.infDeffence)+" against "+signsDeffence + lineEnd;
		else:
			name = str(getPos.name);
			infoText += margin+"Name: "+name + lineEnd;
			infoText += margin+"Card type: Terrain" + lineEnd;
			infoText += margin+"Effect:"+ lineEnd;

			signsAttack = str(signs[getPos.strAffectedBy]);
			if(getPos.infAttack>0):
				infoText += margin+signsAttack+" get +"+str(getPos.infAttack)+" attack "+ lineEnd;
			elif(getPos.infAttack<0):
				infoText += margin+signsAttack+" get "+str(getPos.infAttack)+" attack "+ lineEnd;

			#print("defAf: "+str(handOne[cursorX].defAffectedBy))
			#print(str(signs))
			signsDeffence = str(signs[getPos.defAffectedBy]);
			if(getPos.infDeffence>0):
				infoText += margin+signsDeffence+" get +"+str(getPos.infDeffence)+" deffence "+ lineEnd;
			elif(getPos.infDeffence<0):
				infoText += margin+signsDeffence+" get "+str(getPos.infDeffence)+" deffence "+ lineEnd;
	return infoText

def playerOneTurn(keypress):
	global cursorX;
	global cursorY;
	global playerOnePick;
	global playerOneDrew;
	global deckOne;
	global handOne;
	global playerTurn;

	if playerOneDrew == False:
		handOne += deckOne[-1:];
		deckOne = deckOne[:-1];
		playerOneDrew = True;

	if keypress == 'd':
		cursorX+=1;
	if keypress == 'a':
		cursorX-=1;
	if keypress == 'w':
		cursorY-=1;
	if keypress == 's':
		cursorY+=1;

	if keypress == '\n':
		if cursorY == fieldHeight and playerOnePick == "":
			#choose a card
			playerOnePick=handOne[cursorX];
			del handOne[cursorX];
		elif playerOnePick != "" and cursorY > 1 and cursorY < fieldHeight:
			#place a card
			field[cursorX][cursorY] = playerOnePick;
			playerOnePick="";
			playerTurn=1;
			playerTwoDrew = False;




	if keypress == '\x1b':
		debug = "Exit";
		print(debug)
		exit();

def playerTwoTurn():
	global fieldWidth;
	global fieldHeight;
	global playerTwoDrew;
	global playerOneDrew;
	global deckTwo;
	global handTwo;
	global playerTurn;
	if playerTwoDrew == False:
		handTwo += deckTwo[-1:];
		deckTwo = deckTwo[:-1];
		playerTwoDrew = True;

	handTwoSize = len(handTwo);
	pick = randrange(handTwoSize)
	playerTwoPick=handTwo[pick];
	del handTwo[pick]
	pickX = randrange(fieldWidth-1);
	pickY = randrange(fieldHeight/2);
	field[pickX][pickY] = playerTwoPick;
	playerTwoPick="";
	playerTurn = 2;
	playerOneDrew = False;

def damageTurn():
	global field;
	exit();


os.system('clear')
displayTop();
print("");
displayField();
print("");
displayHandOne();

while True:

	keypress = main();

	if playerTurn == 0:
		playerOneTurn(keypress);
	elif playerTurn == 1:
		playerTwoTurn();
	elif playerTurn == 2:
		damageTurn();

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
	print("");
	if(playerOnePick!=""):
		print("Holding: "+str(playerOnePick.name));

	print(margin+"[Info]--------------------------------------");
	print(infoText);
