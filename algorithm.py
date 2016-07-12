
def init(): #put in constructor
    numHeroes=110
    for i in range(numHeroes):
        winRate[i]=(0,i)
    enemyTeam=[]
    ourTeam=[]

def add(newRate,currRate):
    return newRate+currRate

def pickedHeroes():


def picker():
    for enemyHero in enemyTeam:
        for i in range(numHeroes):
            winRate[i] = (add(scraped[i][enemyHero], winRate[i][1]),i)
    winrate.sort()
    bestHeroes = []
    for i in range (110):
        if(winrate[-i][1] not in pickedHeroes):
            bestHeroes.add(winRate[-i][1])
        if(bestHeroes.length == 5):
            break
    return bestHeroes

