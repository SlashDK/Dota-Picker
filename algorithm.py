def init(): #put in constructor
    numHeroes=110
    enemyTeam=[]
    ourTeam=[]
    with open('herodata.csv', 'rb') as csvfile:
        scraped = csv.reader()
    return (numHeroes, enemyTeam, ourTeam,  scraped)

def add(newRate,currRate):
    return newRate+currRate

def picker(numHeroes, enemyTeam, pickedHeroes, scraped):
    for enemyHero in enemyTeam:
        for i in range(numHeroes):
            winRate[i] = (add(scraped[i][enemyHero], winRate[i][1]),i)
    winrate.sort()
    bestHeroes = []
    for i in range (110):
        if (winrate[-i][1] not in pickedHeroes):
            bestHeroes.add(winRate[-i][1])
        if (bestHeroes.length == 5):
            break
    return bestHeroes

def takeInput(enemyTeam, ourTeam):
    team = input("Enter 0 for your team, 1 for enemy team.")
    heroNum = input("Enter hero num.")
    if (team == 0):
        ourTeam.add(heroNum)
    elif (team == 1):
        enemyTeam.add(heroNum)
    return (enemyTeam, ourTeam)


def main():
    numHeroes, enemyTeam, ourTeam, scraped =  init()
    while enemyTeam.length<=5:
        for i in range(numHeroes):
            winRate[i]=(0,i)
        enemyTeam, ourTeam = takeInput(enemyTeam, ourTeam)
        pickedHeroes = enemyTeam + ourTeam
        bestHeroes = picker(numHeroes, enemyTeam, pickedHeroes, scraped)
        return bestHeroes