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

emoji = ["♈🀄🃏🎴💾💽💿📀⛔"]
element = ["a","b","c","d","e","f","g","h"]
class cardMonster:
    def __init__(self, id, attack, deffence, element, weakAgainst, strongAgainst, Influence):
        self.id = id;
        self.attack = attack;
        self.deffence = deffence;
        self.element = element;
        self.weakAgainst = weakAgainst;
        self.strongAgainst = strongAgainst;
        self.Influence = Influence;
        self.type="monster"

class cardTerrain:
    def __init__(self, id, weakerAgainst, strongerAgainst, Influence):
        self.id = id;
        self.weakerAgainst = weakerAgainst;
        self.strongerAgainst = strongerAgainst;
        self.Influence = Influence;
        self.type="Terain"

#generate deck
for x in range(deckSize):
    if(round(randrange(0,3))!=0):
        deck.append(cardMonster(x,randrange(0,9),randrange(0,9),randrange(0,9),randrange(0,9),randrange(0,9),randrange(0,9)));
    else:
        deck.append(cardTerrain(x,randrange(0,9),randrange(0,9),randrange(0,9)));

shuffle(deck);
deckOne = deck;

shuffle(deck);
deckTwo = deck;

#Draw phase
handOne = deckOne[-3:];
deckOne = deckOne[:-3];

#Draw phase
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
    print("id="str(handOne[xx].id)+"attack="str(handOne[xx].attack)+"deffence="str(handOne[xx].deffence)+"id="str(handOne[xx].id)+"id="str(handOne[xx].id)+)

#card info
