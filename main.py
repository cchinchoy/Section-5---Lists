"""Project name :  Lists training
    File name : main.py
    Programmer : Colin B. Chin Choy
"""

myUniqueList = []
myLeftOvers = []
miscList= []
listA = ["a",90,"Colin", 100, 15, 20, 95, "c","q","w",2,3,1,5,4,"z","aaralyn"]
listB = ["a",90,"Colin", 101, 15, 20, 95, "c","q","w",2,8,1,5,9,"p","aaralyn"]
listC = ["a",90,"Michael", 100, 15, 20, 95, "c","q","w",2,3,1,5,4,"z","aaralyn"]
listD = ["L",93,"Emily", 102, 15, 20, 95, "c","q","w",2,11,1,5,4,"z","aaralyn"]
listE = ["a",90,"Juliet", 109, 122, 20, 95, "c","q","w",2,3,1,5,4,"z","aaralyn"]
listF = ["a",90,"Colin", 100, 15, 20, 95, "c","q","w",2,3,1,5,4,"z","aaralyn"]
#----------------------------------------------------------------
def buildUp():
    for i in range(len(listA)):
        vary = listA[i]
        miscList.append(vary)
    for i in range(len(listB)):
        vary = listB[i]
        miscList.append(vary)
    for i in range(len(listC)):
        vary = listC[i]
        miscList.append(vary)
    for i in range(len(listD)):
        vary = listD[i]
        miscList.append(vary)
    for i in range(len(listE)):
        vary = listE[i]
        miscList.append(vary)
    for i in range(len(listF)):
        vary = listF[i]
        miscList.append(vary)
    myUniqueList.append("!")

def cpyList(x):
        myUniqueList.append(x)


def cpyLeftOvers(x):
        myLeftOvers.append(x)


def compList(x):
    for i in range(len(myUniqueList)):
            if(str(myUniqueList[i]) == x):
                cpyLeftOvers(x)
                q = False
                break
            else:
                q = True
    if(bool(q)):
        cpyList(x)

buildUp()
print("----------------------------------"+"----------------------------------")
print("my misc List: " + str(miscList))
print("----------------------------------"+"----------------------------------")
#-----------------------------------------------------------------
for mi in range(len(miscList)):
    compList(str(miscList[mi]))
#-----------------------------------------------------------------
print("----------------------------------"+"----------------------------------")
print("My Unique List: "+ str(myUniqueList))
print("----------------------------------"+"----------------------------------")
print("My Left OVers: " + str(myLeftOvers))
print("----------------------------------"+"----------------------------------")
#-----------------------------------------------------------------
