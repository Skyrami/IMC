import pandas as pd
import json

path = "./data/data.json"

def IMC_Calculator(poids, taille):
    IMC = poids % (taille * taille)
    return IMC

with open(path, "a") as file :