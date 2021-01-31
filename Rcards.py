# NOT YET WORKING/COMPLETED
#Fri Jan 29 03:29:31 PM EST 2021
from random import randrange
from random import shuffle
from random import sample
import os
#external dependency
from termcolor import colored, cprint
import namegenerator
from curtsies import Input

#variables
handOneSize = 0;
handTwoSize = 0;
deckSize = 30;
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
#playerTurn = randrange(0,2);
playerTurn =0;
playerLastAction="";

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
		#what type are affected
		self.strAffectedBy = strAffectedBy;
		self.defAffectedBy = defAffectedBy;
		#influence amount
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
		#monster
		deck.append(cardMonster(x,randrange(0,20),randrange(0,10),randrange(0,6),randrange(0,9),randrange(0,9),randrange(-9,9),randrange(-9,9)));
	else:
		#terrain
		deck.append(cardTerrain(x,randrange(1,9),randrange(1,9),randrange(-9,9),randrange(-9,9)));

shuffle(deck);
deckOne = sample(deck,len(deck));

shuffle(deck);
deckTwo = sample(deck,len(deck));

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
				infoText += margin+signsAttack+" get +"+str(getPos.infAttack)+" attack"+ lineEnd;
			elif(getPos.infAttack<0):
				infoText += margin+signsAttack+" get "+str(getPos.infAttack)+" attack"+ lineEnd;

			#print("defAf: "+str(handOne[cursorX].defAffectedBy))
			#print(str(signs))
			signsDeffence = str(signs[getPos.defAffectedBy]);
			if(getPos.infDeffence>0):
				infoText += margin+signsDeffence+" get +"+str(getPos.infDeffence)+" deffence"+ lineEnd;
			elif(getPos.infDeffence<0):
				infoText += margin+signsDeffence+" get "+str(getPos.infDeffence)+" deffence"+ lineEnd;
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
	global playerTwoDrew;
	global deckOne;
	global handOne;
	global playerTurn;

	endTurn=False;
	if playerOneDrew == False:
		drawAmount=2;
		if(len(handOne)>3):
			drawAmount=1;
		if(len(handOne)<4):
			handOne += deckOne[-drawAmount:];
			deckOne = deckOne[:-drawAmount];
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
			if(playerOnePick.type=="monster" or len(handOne)<1):
				endTurn=True;
			playerOnePick="";
			playerTwoDrew = False;
			if(endTurn==True):
				playerTurn=1;

def playerTwoTurn():
	global fieldWidth;
	global fieldHeight;
	global playerTwoDrew;
	global playerOneDrew;
	global deckTwo;
	global handTwo;
	global playerTurn;

	if playerTwoDrew == False:
		drawAmount=2;
		if(len(handTwo)>3):
			drawAmount=1;
		if(len(handTwo)<4):
			handTwo += deckTwo[-drawAmount:];
			deckTwo = deckTwo[:-drawAmount];
		playerTwoDrew = True;

	handTwoSize = len(handTwo);
	pick = randrange(handTwoSize)
	playerTwoPick=handTwo[pick];
	del handTwo[pick]
	pickX = randrange(fieldWidth-1);
	pickY = randrange(fieldHeight/2);
	field[pickX][pickY] = playerTwoPick;
	if(playerTwoPick.type=="monster" or len(handTwo)<1):
		endTurn=True;
	playerTwoPick="";
	playerOneDrew = False;
	if(endTurn==True):
		playerTurn = 2;
	else:
		answer=input("End turn y/n ");
		if(answer=="y"):
			playerTurn = 2;

def damageTurn():
	global field;
	global playerTurn;
	global healthOne;
	global healthTwo;
	attackEffect=[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]];
	deffenceEffect=[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]];
	#attackEffect [row][sign] = amount

	for x in range(fieldWidth):
		for y in range(fieldHeight):
			if field[x][y] != 0:
				influence = field[x][y].infAttack;
				sign = field[x][y].strAffectedBy;
				attackEffect[x][sign]+=influence;

	for x in range(fieldWidth):
		for y in range(fieldHeight):
			if field[x][y] != 0:
				influence = field[x][y].infDeffence;
				sign = field[x][y].defAffectedBy;
				deffenceEffect[x][sign]+=influence;
	
	#total attack and deffence per row per player
	deffenceTotalOne=[0,0,0,0,0];
	attackTotalOne=[0,0,0,0,0];
	deffenceTotalTwo=[0,0,0,0,0];
	attackTotalTwo=[0,0,0,0,0];

	#player one side
	for x in range(fieldWidth):
		for y in range(2,4):
			if field[x][y] != 0 and field[x][y].type=="monster":
				print("side two "+str(field[x][y].name))
				sign = field[x][y].signs;
				influenceDeffence = deffenceEffect[x][sign];
				influenceAttack = attackEffect[x][sign];
				deffenceTotalOne[x]+=field[x][y].deffence+influenceDeffence;
				print(deffenceTotalOne[x]);
				attackTotalOne[x]+=field[x][y].attack+influenceAttack;

	for x in range(fieldWidth):
		#player two side
		for y in range(0,2):
			if field[x][y] != 0 and field[x][y].type=="monster":
				print("side two "+str(field[x][y].name))
				sign = field[x][y].signs;
				influenceDeffence = deffenceEffect[x][sign];
				influenceAttack = attackEffect[x][sign];
				deffenceTotalTwo[x]+=field[x][y].deffence+influenceDeffence;
				print(deffenceTotalTwo[x]);
				attackTotalTwo[x]+=field[x][y].attack+influenceAttack;

	damageOne=0;
	damageTwo=0;

	for x in range(fieldWidth):
		if attackTotalTwo[x]>0:
			damageOne = attackTotalTwo[x]-deffenceTotalOne[x];
		if attackTotalOne[x]>0:
			damageTwo = attackTotalOne[x]-deffenceTotalTwo[x];

	playerLastAction = "dmg1= "+str(damageOne)+" dmg2= "+str(damageTwo);
	print(playerLastAction);
	healthOne-=damageOne;
	healthTwo-=damageTwo;

	print(str(attackEffect[x]));
	print(str(deffenceEffect[x]));
	playerTurn = 0;

def GameOver():
	if(healthTwo==healthOne):
		print("~DRAW~");
	if(healthTwo>healthOne):
		print("~Player two win~");
	else:
		print("~Player one win~");

os.system('clear')
displayTop();
print("");
displayField();
print("");
displayHandOne();

while True:
	playerLastAction="";
	keypress = main();

	if playerTurn == 0:
		playerOneTurn(keypress);
	elif playerTurn == 1:
		playerTwoTurn();
	elif playerTurn == 2:
		damageTurn();
	elif playerTurn ==3:
		GameOver();

	if(cursorX<0):
		cursorX=0;
	if(cursorY<0):
		cursorY=0;
	if cursorX>fieldWidth-1 and cursorY<fieldHeight:
		cursorX=fieldWidth-1;
	if cursorY>fieldHeight:
		cursorY=fieldHeight;



	os.system('clear');
	if(healthOne<1 or healthTwo<1 or len(deckOne)<1 or len(deckTwo)<1):
		playerTurn=3;
		GameOver();

	if(playerTurn!=3):
		displayTop();
		print("");
		displayField();
		print("");
		displayHandOne();
		print("");

		if(playerOnePick!=""):
			playerLastAction ="Holding: "+str(playerOnePick.name);

		print(margin+playerLastAction);
		print(margin+"[Info]--------------------------------------");
		print(infoText);

	if keypress == '\x1b':
		debug = "Exit";
		print(debug);
		exit();

