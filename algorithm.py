import numpy as np
import pandas as pd

def init():
    scraped = pd.read_csv('hero_data.csv')
    scraped = scraped.as_matrix()
    scraped = scraped[1:][:]
    numHeroes = scraped.shape[0]
    return (numHeroes, scraped)

def add(newRate, currRate):
    return newRate + currRate

def picker(numHeroes, enemyTeam, pickedHeroes, scraped):
    for enemyHero in enemyTeam:
        for i in range(numHeroes):
            winRate[i] = (add(scraped[i][enemyHero], winRate[i][1]), i)
    winrate.sort()
    bestHeroes = []
    for i in range(110):
        if winrate[-i][1] not in pickedHeroes:
            bestHeroes.add(winRate[-i][1])
        if bestHeroes.length == 5:
            break
    return bestHeroes

def main(enemyTeam, ourTeam):
    numHeroes, scraped =  init()
    for i in range(numHeroes):
        winRate[i]=(0, i)
    pickedHeroes = enemyTeam + ourTeam
    bestHeroes = picker(numHeroes, enemyTeam, pickedHeroes, scraped)
    return bestHeroes