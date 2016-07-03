#!/usr/bin/env python
#
# brief: import USDA CSV data and convert to python dict
# author: bto
# date: Jun 2013
#
# description:
#  This conversion program allows future versions of USDA data to be used.
#  To convert, run the following from the command line:
#  
#  $ python import_foods.py < ABBREV.csv > usda.py
#  
#  The 'usda.py' output file can then be imported into the soylent calculator.

import sys
from string import atof, strip, lower

# -------------------------------------------------------------
# conversions

def kcal2j(kcal):
    return 4184*kcal

def iu2g(mineral, iu):
    factor = {
        'vitamin a': 0.3e-6,
        'vitamin c': 50e-6,
        'vitamin d': 0.025e-6,
        'vitamin e': 0.667e-3
        }
    if mineral in factor.keys():
        return factor[mineral]*iu
    else:
        print('\'%s\' is not in conversion list' % mineral)
        sys.exit()

# -------------------------------------------------------------
# nutrient selection, because some aren't in the RDI

nutrient = ['protein', 'lipids', 'ash', 'carbohydrate', 'fiber', 'sugar', 'calcium', 'iron', 'magnesium', 'phosphorus', 'potassium', 'sodium', 'zinc', 'copper', 'manganese', 'selenium', 'vitamin c', 'thiamin', 'riboflavin', 'niacin', 'panthothenic', 'vitamin b6', 'folate', 'folic acid', 'folate', 'folate dfe', 'choline', 'vitamin b12', 'vitamin a', 'vitamin a RAE', 'retinol', 'alpha carotine', 'beta carotine', 'beta crypt', 'lycopene', 'lut+zea', 'vitamin e', 'vitamin d', 'vitamin d ug', 'vitamin k', 'fat sat', 'fat mono', 'fat poly', 'cholesterol']
units = [1,1,1,1,1,1,1e-3,1e-3,1e-3,1e-3,1e-3,1e-3,1e-3,1e-3,1e-3,1e-6,1e-3,1e-3,1e-3,1e-3,1e-3,1e-3,1e-6,1e-6,1e-6,1e-6,1e-3,1e-6,'IU','RAE',1e-6,1e-6,1e-6,1e-6,1e-6,1e-6,1e-3,1e-6,'UI',1e-6,1,1,1,1e-3]
use = [1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,0,0,1,1,1,0,0,0,1,0,0,0,1,1,0,1,1,1,1,1]

# -------------------------------------------------------------

def create_name(name):
    name = name.replace(', ','_')
    name = name.replace(' ','_')
    name = name.replace(',','_')
    name = name.replace('/','')
    name = name.replace('&','and')
    name = name.replace('-','_')
    name = name.replace('\'','')
    name = name.replace('(','')
    name = name.replace(')','')
    name = name.replace('%','pc')

    return name

def main():
    for line in sys.stdin:
        if line[0] == '#': continue
        data = line.split('^')
        
        # handle empty cells
        for i in range(len(data)):
            if data[i] == '': data[i] = '0'

        desc = lower(data[1].strip().strip('\"'))
        name = create_name(desc)
        water = atof(data[2])
        energy = kcal2j(atof(data[3]))
        mass = []

        for i in range(len(nutrient)):
            # don't use all values
            if not use[i]: 
                mass.append(0)
                continue
            
            # convert UI values to g
            if type(units[i]) == str:
                mass.append(iu2g(nutrient[i], atof(data[4+i])))
            else:
                mass.append(atof(data[4+i])*units[i])
       
        # ignore some foods...
        if 'baby' in name: continue
        if 'shrimp' in name: continue
        if 'gravy' in name: continue
        if 'cereals' in name: continue

        # print dictionary
        print('%s = food("%s", %g, %g, {' % (name, desc, sum(mass), energy)),
        for i in range(len(nutrient)):
            # don't use all values
            if not use[i]: continue
            
            print('\'%s\': %g,' % (nutrient[i], mass[i])),
        print('})')

if __name__ == '__main__':
    main()
