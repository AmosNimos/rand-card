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
import pyttsx3

#variables
handOneSize = 0;
handTwoSize = 0;
deckSize = 30;
handLimit = 4;
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
fieldWidth= 4;
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
singAmount=5;

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
cardBackSymbol="🔳";
cardFrontSymbol="🔍";
emptySpaceSymbol="⬛";
signs = ["[Aries ♈]","[Sagittarius ♐]","[Taurus ♉]","Aquarius ♒","[Libra ♎]","[Scorpius ♏]","Aquarius ♒", "[Pisces ♓],[Ophiuchus ⛎]"];
emoji = ["🀄🃏🎴💾💽💿📀⛔?🔳⬛⬜🔍"];

engine = pyttsx3.init();

mute = input("mute y/n");

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
		deck.append(cardMonster(x,randrange(0,20),randrange(0,10),randrange(0,singAmount),randrange(0,singAmount),randrange(0,5),randrange(-9,9),randrange(-9,9)));
	else:
		#terrain
		deck.append(cardTerrain(x,randrange(1,singAmount),randrange(1,singAmount),randrange(-9,9),randrange(-9,9)));

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
			else:
				answer = input("End turn y/n: ");
				if(answer=="y"):
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

	endTurn=False;
	if playerTwoDrew == False:
		drawAmount=1;
		if(len(handTwo)<4):
			handTwo += deckTwo[-drawAmount:];
			deckTwo = deckTwo[:-drawAmount];
			text = "Player 2 draw "+str(drawAmount)+" card!"
			print(text);
			saySound(text);
		playerTwoDrew = True;

	handTwoSize = len(handTwo);
	pick = randrange(handTwoSize)
	playerTwoPick=handTwo[pick];
	del handTwo[pick]
	pickX = randrange(fieldWidth-1);
	pickY = randrange(fieldHeight/2);
	field[pickX][pickY] = playerTwoPick;
	text = "Player 2 digitalise "+str(playerTwoPick.name)+" to the field!";
	print(text);
	saySound(text);
	if(playerTwoPick.type=="monster" or len(handTwo)<1):
		endTurn=True;
	playerTwoPick="";
	playerOneDrew = False;
	if(endTurn==True):
		text = "Player 2 end his turn.";
		print(text);
		saySound(text);
		input("Press Enter to continue...")
		playerTurn = 2;
	else:
		answer = randrange(0,2);
		if(answer=="1"):
			text = "Player 2 end his turn.";
			print(text);
			saySound(text);
			input("Press Enter to continue...")
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
	defenceTotalOne=[[0,0,0,0,0],[0,0,0,0,0]];
	attackTotalOne=[[0,0,0,0,0],[0,0,0,0,0]];
	defenceTotalTwo=[[0,0,0,0,0],[0,0,0,0,0]];
	attackTotalTwo=[[0,0,0,0,0],[0,0,0,0,0]];
	monsterOneName=[["","","","",""],["","","","",""]];
	monsterTwoName=[["","","","",""],["","","","",""]];

	#player one side
	for x in range(fieldWidth):
		for y in range(2,4):
			if field[x][y] != 0 and field[x][y].type=="monster":
				#monsterOneName[y][x] = str(field[x][y].name);
				sign = field[x][y].signs;
				influenceDeffence = deffenceEffect[x][sign];
				influenceAttack = attackEffect[x][sign];
				defenceTotalOne[y-2][x]=field[x][y].deffence+influenceDeffence;
				attackTotalOne[y-2][x]=field[x][y].attack+influenceAttack;
			#print("x= "+str(x)+","+"y= "+str(y-2));

	for x in range(fieldWidth):
		#player two side
		for y in range(0,2):
			if field[x][y] != 0 and field[x][y].type=="monster":
				#monsterTwoName[y][x] = str(field[x][y].name);
				sign = field[x][y].signs;
				influenceDeffence = deffenceEffect[x][sign];
				influenceAttack = attackEffect[x][sign];
				defenceTotalTwo[y][x]+=field[x][y].deffence+influenceDeffence;
				attackTotalTwo[y][x]+=field[x][y].attack+influenceAttack;
			#print("x= "+str(x)+","+"y= "+str(y));

	damageOne=0;
	damageTwo=0;
	#for each x
	# scan y of x attack de j1[2,4] - deffence j2[0,2] = damageTwo[x]

	for x in range(fieldWidth):
		if (attackTotalTwo[0][x]+attackTotalTwo[1][x])!=0:
			damageOne += (attackTotalTwo[0][x]+attackTotalTwo[1][x])-(defenceTotalOne[0][x]+defenceTotalOne[1][x]);

		if (attackTotalOne[0][x]+attackTotalOne[1][x])!=0:
			damageTwo += (attackTotalOne[0][x]+attackTotalOne[1][x])-(defenceTotalTwo[0][x]+defenceTotalTwo[1][x]);
				#text = "Player 1 "+str(monsterOneName[x])+" attack with "+str(attackTotalOne[x])+" power point!\n";
				#text += "Player 2 "+str(monsterTwoName[x])+" block with "+str(attackTotalOne[x])+" armor point!";
				#print(text);
				#engine.say(text);
				#engine.runAndWait();

	playerLastAction = "Player 1 get "+str(-damageOne)+" health!\n";
	playerLastAction += "Player 2 get "+str(-damageTwo)+" health!";
	print(playerLastAction);
	saySound(playerLastAction);
	healthOne-=damageOne;
	healthTwo-=damageTwo;
	input("Press Enter to continue...")
	playerTurn = 0;

def saySound(text):
	global mute;
	if mute != "y":
		engine.say(text);
		engine.runAndWait();

def GameOver():
	if(healthTwo==healthOne):
		print("Draw!");
	if(healthTwo>healthOne):
		text="Player two win!";
		print(text);
		saySound(text);
	else:
		text="Player one win!";
		print(text);
		saySound(text);

os.system('clear')
displayTop();
print("");
displayField();
print("");
displayHandOne();

while True:
	playerLastAction="";

	if playerTurn == 0:
		keypress = main();
		playerOneTurn(keypress);
	elif playerTurn == 1:
		playerTwoTurn();
	elif playerTurn == 2:
		damageTurn();
	elif playerTurn ==3:
		keypress = main();
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

	if(playerTurn<2):
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
