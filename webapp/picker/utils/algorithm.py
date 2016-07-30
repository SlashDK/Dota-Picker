import numpy as np
import pandas as pd
import os

def init():
    module_dir = os.path.dirname(__file__)
    scraped = pd.read_csv(os.path.join(module_dir,'hero_data.csv'), header=None).as_matrix()
    numHeroes = scraped.shape[0]
    return (numHeroes, scraped)

def add(newRate, currRate):
    return newRate + currRate

def picker(numHeroes, enemyTeam, pickedHeroes, scraped, winRate):
    for enemyHero in enemyTeam:
        for i in range(numHeroes):
            winRate[i] = (add(scraped[enemyHero][i], winRate[i][0]), i)
    winRate.sort()
    bestHeroes = []
    for i in range(numHeroes):
        if winRate[-i-1][1] not in pickedHeroes:
            bestHeroes.append(winRate[-i-1][1])
        if len(bestHeroes) == 5:
            break
    return bestHeroes

def main(enemyTeam, ourTeam):
    numHeroes, scraped =  init()
    winRate = []
    for i in range(numHeroes):
        temp=(0, i)
        winRate.insert(i,temp)
    pickedHeroes = enemyTeam + ourTeam
    bestHeroes = picker(numHeroes, enemyTeam, pickedHeroes, scraped, winRate)
    return bestHeroes

enemyTeam = []
ourTeam = []
bestHeroes = main(enemyTeam, ourTeam)
print(bestHeroes)
