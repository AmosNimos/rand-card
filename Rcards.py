# NOT YET WORKING/COMPLETED
#Fri Jan 29 03:29:31 PM EST 2021
from random import randrange
from random import shuffle

#variables
handOneSize = 0;
handTwoSize = 0;
deckSize = 15;
deck=[]
deckOne = []
handOne = []
healthOne = []
handOneView = ""
handTwoView = ""
xx=0;
emoji = ["🀄🃏🎴💾💽💿📀⛔"];
element = ["♈","♉","♊","♋","♌","♍","♎","♏","♐","♑"];
selectionElement = ""

class cardMonster:
    def __init__(self, id, attack, deffence, element, strAffectedBy, defAffectedBy, infAttack, infDeffence):
        self.id = id;
        self.attack = attack;
        self.deffence = deffence;
        self.element = element;
        self.strAffectedBy = strAffectedBy;
        self.defAffectedBy = defAffectedBy;
        self.infAttack = infAttack;
        self.infDeffence = infDeffence;
        self.type="monster"

class cardTerrain:
    def __init__(self, id, weakerAgainst, strongerAgainst, infAttack, infDeffence):
        self.id = id;
        self.weakerAgainst = weakerAgainst;
        self.strongerAgainst = strongerAgainst;
        self.infAttack = infAttack;
        self.infDeffence = infDeffence;
        self.type="Terain"

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

#player two hand
handTwoSize=len(handTwo);
for x in range(handTwoSize):
        handTwoView += "🎴";
print(handTwoView);

#field
#field=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

#player one hand
handOneSize=len(handOne);
for x in range(handOneSize):
    if x == xx:
        handOneView += "🃏";
    else:
        handOneView += "🎴";
print(handOneView);

if(handOne[xx].type=="monster"):
    selectionElement = str(element[handOne[xx].element]);
    print("Card type: Monster");
    print("Card element: "+selectionElement);
    print("Attack="+str(handOne[xx].attack)+" Deffence="+str(handOne[xx].deffence));

    elementAttack = str(element[handOne[xx].strAffectedBy]);
    if(handOne[xx].infAttack>0):
        print("Attack +"+str(handOne[xx].infAttack)+" against "+elementAttack);
    elif(handOne[xx].infAttack<0):
        print("Attack "+str(handOne[xx].infAttack)+" against "+elementAttack);


    elementDeffence = str(element[handOne[xx].defAffectedBy]);
    if(handOne[xx].infDeffence>0):
        print("Deffence +"+str(handOne[xx].infDeffence)+" against "+elementDeffence);
    elif(handOne[xx].infDeffence<0):
        print("Deffence "+str(handOne[xx].infDeffence)+" against "+elementDeffence);
else:
    print("Card type: Terrain");
    print("id="+str(handOne[xx].id)+" attack="+str(handOne[xx].weakerAgainst)+" deffence="+str(handOne[xx].strongerAgainst))
