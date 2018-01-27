import csv
import pandas as pd
import numpy as np

#Loads all datafiles into dataframes of the same name.  Not sure the with open statements are necessary.
filenames = ['colors.csv', 'inventories.csv', 'inventory_parts.csv', 'inventory_sets.csv', 'part_categories.csv', 'parts.csv', 'sets.csv', 'themes.csv']

with open(filenames[0]) as datafile:
    colors = pd.read_csv(datafile)
with open(filenames[1]) as datafile:
    inventories = pd.read_csv(datafile)
with open(filenames[2]) as datafile:
    inventory_parts = pd.read_csv(datafile)
with open(filenames[3]) as datafile:
    inventory_sets = pd.read_csv(datafile)
with open(filenames[4]) as datafile:
    part_categories = pd.read_csv(datafile)
with open(filenames[5]) as datafile:
    parts = pd.read_csv(datafile)
with open(filenames[6]) as datafile:
    sets = pd.read_csv(datafile)
with open(filenames[7]) as datafile:
    themes = pd.read_csv(datafile)
