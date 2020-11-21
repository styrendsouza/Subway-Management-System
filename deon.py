# ------------------Classes---------------------
class Face:
    eyes = str()
    nose = str()
    mouth = str()
    def __init__(self,eyes = "",nose =  "",mouth = ""):
        self.defineFace(eyes,nose,mouth)
    
    def defineFace(self,eyes,nose,mouth):
        self.eyes = eyes
        self.nose = nose
        self.mouth = mouth

    def printFace(self):
        print("\tFace:")
        print("\t\tEyes:", self.eyes)
        print("\t\tNose:", self.nose)
        print("\t\tMouth:", self.mouth, "\n")

class Torso:
    hands = str()
    stomach = str()
    def __init__(self,hands = "",stomach =  ""):
        self.defineTorso(hands,stomach )
    
    def defineTorso(self,hands,stomach):
        self.hands = hands
        self.stomach = stomach

    def printTorso(self):
        print("\tTorso:")
        print("\t\tHands:", self.hands)
        print("\t\tStomach:", self.stomach,)

class LowerBody:
    legs = str()
    def __init__(self,legs = ""):
        self.defineLowerBody(legs)
    
    def defineLowerBody(self,legs):
        self.legs = legs

    def printLowerBody(self):
        print("\tLower Body:")
        print("\t\tLegs:", self.legs)

class Human (Face, Torso, LowerBody):
    def __init__(self,eyes = "",nose =  "",mouth = "",hands = "",stomach =  "",legs = ""):
        self.defineFace(eyes,nose,mouth)
        self.defineTorso(hands,stomach )
        self.defineLowerBody(legs)

# ------------------Functions---------------------
def createNewHuman(humanList):
    print("Enter Human Details :- ")
    eyes = input("\tEyes : ")
    nose = input("\tNose : ")
    mouth = input("\tMouth : ")
    hands = input("\tHands : ")
    stomach = input("\tStomach : ")
    legs = input("\tLegs : ")
    human = Human(eyes,nose,mouth,hands,stomach,legs)
    humanList.append(human)
    return humanList

def printHumans(humanList):
    i=0
    if len(humanList) > 0:
        for human in humanList:
            print("Human " , str(i) , " : ")
            human.printFace()
            human.printTorso()
            human.printLowerBody()
            i+=1
    else:
        print("No Humans There")

def deleteHuman(humanList, index):
    if(index>len(humanList)):
        humanList.pop(index)
    else:
        print("Invlaid Index")
    return list

# ------------------Main---------------------
print("Create Your Human : ")
humanList = list()
while True:
    choice = input("-------- Menu --------\n1. Create new Human\n2. Print Humans\n3. Delete a Human\n4. Exit\nEnter a Choice : ")
    if choice == "1":
        humanList = createNewHuman(humanList)
    elif choice == "2":
        printHumans(humanList)
    elif choice == "3":
        index = input("Enter the index of the Human to remove : ")
        deleteHuman(humanList,int(index))
    elif choice == "4":
        break
    else:
        print("Invalid Choice")

