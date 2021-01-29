# NOT YET WORKING/COMPLETED
#Fri Jan 29 03:29:31 PM EST 2021
from random import randrange
from random import shuffle
#external dependency
from termcolor import colored, cprint
import namegenerator

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
emoji = ["πππ΄πΎπ½πΏπβ✅"];
signs = ["[Aries β]","[Taurus β]","[Gemini β]","[Cancer β]","[Leo β]","[Virgo β]","[Libra β]","[Scorpius β]","[Sagittarius β]","[Capricornus β]"];
selectionsign = ""


class cardMonster:
	def __init__(self, id, attack, deffence, signs, strAffectedBy, defAffectedBy, infAttack, infDeffence):
		self.id = id;
		self.attack = attack;
		self.deffence = deffence;
		self.signs = signs;
		self.strAffectedBy = strAffectedBy*2;
		self.defAffectedBy = defAffectedBy*2;
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

print("Player one health: ["+str(healthOne)+"]");
print("Player two health: ["+str(healthTwo)+"]");
print("");

#player two hand
handTwoSize=len(handTwo);
for x in range(handTwoSize):
        handTwoView += "π΄";
print(handTwoView);

#field
field=[[0,0,1,1],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]];


def display():
	linetxt="";
	for y in range(4):
		linetxt="";
		for x in range(0,5):
			#print(str(x)+","+str(y));
			if x == cursorX and y == cursorY:
				#cursor there
				linetxt+=colored("?",'red');
			elif field[x][y]==0:
				#empty there
				linetxt+=colored(".",'white');
			else:
				#card there
				linetxt+=colored("#",'white');
		print(linetxt);
				
def displayHandOne():
	global cursorX;
	global handOne;
	global handOneView;
	global signs;
	cursorX=0;
	#player one hand
	handOneSize=len(handOne);
	for x in range(handOneSize):
		if x == cursorX and cursorY==4:
			handOneView += "π";
		else:
			handOneView += "π΄";
	print(handOneView);

	if(handOne[cursorX].type=="monster"):
		selectionsign = str(signs[handOne[cursorX].signs]);
		name = str(handOne[cursorX].name);
		print("Name: "+name);
		print("Type: Monster");
		print("Sign: "+selectionsign);
		print("Attack="+str(handOne[cursorX].attack)+" Deffence="+str(handOne[cursorX].deffence));

		signsAttack = str(signs[handOne[cursorX].strAffectedBy]);
		if(handOne[cursorX].infAttack>0):
			print("Attack +"+str(handOne[cursorX].infAttack)+" against "+signsAttack);
		elif(handOne[cursorX].infAttack<0):
			print("Attack "+str(handOne[cursorX].infAttack)+" against "+signsAttack);

		signsDeffence = str(signs[handOne[cursorX].defAffectedBy]);
		if(handOne[cursorX].infDeffence>0):
			print("Deffence +"+str(handOne[cursorX].infDeffence)+" against "+signsDeffence);
		elif(handOne[cursorX].infDeffence<0):
			print("Deffence "+str(handOne[cursorX].infDeffence)+" against "+signsDeffence);
	else:
		print("Card type: Terrain");
		print("id="+str(handOne[cursorX].id)+" attack="+str(handOne[cursorX].weakerAgainst)+" deffence="+str(handOne[cursorX].strongerAgainst))
display();	
print("");
displayHandOne();
