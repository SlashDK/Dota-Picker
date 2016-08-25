import numpy as np
import pandas as pd
import os

def mapHeroes(enemyTeam, ourTeam):
    enemyTeamMapped = []
    ourTeamMapped = []
    module_dir = os.path.dirname(__file__)
    with open(os.path.join(module_dir, 'hero_list.txt')) as f:
        heroList = f.read().splitlines()
        for hero in enemyTeam:
            enemyTeamMapped.append(heroList.index(hero.title()))
        for hero in ourTeam:
            ourTeamMapped.append(heroList.index(hero.title()))
    assert (len(enemyTeamMapped + ourTeamMapped) == len(set(enemyTeamMapped + ourTeamMapped)))
    return (enemyTeamMapped, ourTeamMapped)

def reverse_map_heroes(final_team):
    returnable_team = []
    module_dir = os.path.dirname(__file__)
    with open(os.path.join(module_dir, 'hero_list.txt')) as f:
        heroList = f.read().splitlines()
        for hero in final_team:
            returnable_team.append(heroList[hero])
    return returnable_team


def init():
    module_dir = os.path.dirname(__file__)
    scraped = pd.read_csv(os.path.join(module_dir, 'hero_data.csv'), header=None).as_matrix()
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
        winRate.append((0, i))
    pickedHeroes = enemyTeam + ourTeam
    bestHeroes = picker(numHeroes, enemyTeam, pickedHeroes, scraped, winRate)
    return bestHeroes

def get_best_heroes(enemyTeam, ourTeam):
    try:
        enemyTeam, ourTeam = mapHeroes(enemyTeam, ourTeam)
        bestHeroes = main(enemyTeam, ourTeam)
        bestHeroes = reverse_map_heroes(bestHeroes)
        return bestHeroes
    except:
        return None
