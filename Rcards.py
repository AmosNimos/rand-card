# NOT YET WORKING/COMPLETED
#Fri Jan 29 03:29:31 PM EST 2021
from random import randrange
from random import shuffle
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
xx=0;
emoji = ["🀄🃏🎴💾💽💿📀⛔"];
signs = ["[Aries ♈]","[Taurus ♉]","[Gemini ♊]","[Cancer ♋]","[Leo ♌]","[Virgo ♍]","[Libra ♎]","[Scorpius ♏]","[Sagittarius ♐]","[Capricornus ♑]"];
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
        self.type="Terain"
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

#player two hand
handTwoSize=len(handTwo);
for x in range(handTwoSize):
        handTwoView += "🎴";
print(handTwoView);

#field
field=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
def display():
    linetxt=""
    for y in range(4):
        print(linetxt);
        linetxt="";
        for x in range(3):
            if x==xx and y ==yy:
				linetxt+=colored("#",'red');
            elif field[x][y]==0:
                linetxt+=colored(".",'white');
            else:
                linetxt+=colored("🎴",'white');


def displayHandOne():
    global handOneView
    global xx
    global handOne
    #player one hand
    handOneSize=len(handOne);
    for x in range(handOneSize):
        if x == xx:
            handOneView += "🃏";
        else:
            handOneView += "🎴";
    print(handOneView);

    if(handOne[xx].type=="monster"):
        selectionsign = str(signs[handOne[xx].signs]);
        name = str(handOne[xx].name);
        print("Name: "+name);
        print("Type: Monster");
        print("Sign: "+selectionsign);
        print("Attack="+str(handOne[xx].attack)+" Deffence="+str(handOne[xx].deffence));

        signsAttack = str(signs[handOne[xx].strAffectedBy]);
        if(handOne[xx].infAttack>0):
            print("Attack +"+str(handOne[xx].infAttack)+" against "+signsAttack);
        elif(handOne[xx].infAttack<0):
            print("Attack "+str(handOne[xx].infAttack)+" against "+signsAttack);


        signsDeffence = str(signs[handOne[xx].defAffectedBy]);
        if(handOne[xx].infDeffence>0):
            print("Deffence +"+str(handOne[xx].infDeffence)+" against "+signsDeffence);
        elif(handOne[xx].infDeffence<0):
            print("Deffence "+str(handOne[xx].infDeffence)+" against "+signsDeffence);
    else:
        print("Card type: Terrain");
        print("id="+str(handOne[xx].id)+" attack="+str(handOne[xx].weakerAgainst)+" deffence="+str(handOne[xx].strongerAgainst))

displayHandOne();
