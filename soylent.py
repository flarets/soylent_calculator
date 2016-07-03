#!/usr/bin/env python
#
# brief: soylent calculator
# author: bto
# date: Jun 2013
#
# resources:
#  nutritiondata.self.com
#  ars.usda.gov
#
# Notes:
#  - Radical diet changes never seem to work. keeping a food diary and making
#    incremental changes based on overamounts/deficiencies works better
#  - It's easy to meet the macronutrient (carbs/protein/fat) requirements but more
#    difficult to meet the micronutrient (vitamins, minerals) requirements.
#  - Not all carbohydrates are created equal: a mixture of GI levels will provide
#    more consistent energy between meals
#  - A wide variety of foods will minimize the harmful components of any one
#  - The body does not store protein, you must eat it as you need it
#  - For a cheaper recipe, use foods fortified with vitamins instead of pills

import sys
import operator

from math import sqrt
from numpy import array

#from usda import *        # USDA data
from ingredients import * # custom data

# -------------------------------------------------------------
# requirements
# source: rob reinhart's values (source: robrhinehart.com)
# see also: nutritiondata.self.com

rde = 9.8e6
# this RDI already includes supplement calcium, vitamin D and vitamin C per day!
rdi = {
    'carbohydrate':220.0,
    'protein':65.0,
    'fat':65.0,
    'fiber':40.0,
    'potassium':3.5,
    'chloride':3.4,
    'sodium':2.4,
    'sulphur':0.5,
    'calcium':(1000e-3), # use supplement
    'phosphorus':1.0,
    'choline':550e-3,
    'magnesium':400e-3,
    'vitamin c':(60e-3), # use powder
    'niacin':20e-3,
    'vitamin e':20e-3,
    'iron':18e-3,
    'zinc':15e-3,
    'vitamin b5':10e-3,
    'vitamin b6':2e-3,
    'riboflavin':1.7e-3,
    'thiamin':1.5e-3,
    'manganese':2e-3,
    'copper':1e-3,
    'vitamin a':900e-6,
    'selenium':700e-6,
    'folate':400e-6,
    'biotin':300e-6,
    'iodine':150e-6,
    'chromium':120e-6,
    'vitamin k':80e-6,
    'molybdenum':75e-6,
    'vitamin d':(15e-6), # use tablet/sunshine
    'vitamin b12':6e-6,
}

def check_rdi(food):
    di = {}
    sorted_food = sorted(food.content.iteritems(), key=operator.itemgetter(1), reverse=True)
    for key,value in sorted_food:
        if key in rdi.keys():
            amount = food.content[key]/rdi[key]
            di[key] = amount
    return di

def print_rdi(food):
    plus = []
    sorted_food = sorted(food.content.iteritems(), key=operator.itemgetter(1), reverse=True)
    print("Content:")
    for key,value in sorted_food:
        if key in rdi.keys():
            amount = food.content[key]/rdi[key]*100
            if amount > 99:
                print('%13s: %3.0f%%' % (key, amount))
            else:
                print('%13s: %3.0f%% *' % (key, amount))
        else:
            plus.append(key)
    
    print
    print("  * insufficient")
    print
    print("Energy:")
    print("  %gMJ (%gMJ recommended)" % (food.energy/1e6, rde/1e6))
    
    if plus != []:
        print("\nAdditional:")
        for key in plus:
            print('%13s: %4.1fg' % (key, food.content[key]))
    print

def print_recipe(x0, args):
    print("Recipe:")
    for i in range(len(x0)):
        print("%7.1fg %s" % (x0[i], args[i].name))
    print

def print_difference(food0, food1):
    # useful for comparing quick variations
    sorted_food0 = sorted(food0.content.iteritems(), key=operator.itemgetter(1), reverse=True)
    sorted_food1 = sorted(food1.content.iteritems(), key=operator.itemgetter(1), reverse=True)
    
    energy_diff = (food1.energy - food0.energy)/rde
    if energy_diff > 10:
        print("%13s: %gMJ (%gMJ recommended)" % ('energy',energy_diff/1e6, rde/1e6))
    print

    for key,value in sorted_food0:
        if key in rdi.keys():
            amount = food1.content[key]/rdi[key]*100
            diff = (food1.content[key] - food0.content[key])/rdi[key]*100
            if diff > 5:
                print('%13s: %3.0f%% %3.0f%%' % (key, amount, diff))
            if diff < -5:
                print('%13s: %3.0f%% %3.0f%%' % (key, amount, diff))
    print

# -------------------------------------------------------------
# recipe

def user_defined_soylent(x, args):

    assert len(x) == len(args) 
    for i in range(len(args)):
        args[i].serving_size(x[i])
    
    soylent = args[0]
    for i in range(1,len(args)):
        soylent += args[i]

    return soylent
    
def main():
    # soylent procedure:
    #  1. vary macros to get energy+ratios 
    #  2. include flavour/emulsifier
    #  3. use most complete micro first
    #  4. fill in remainder of micros with specific powders

    # example 1
    x0 = [100.0, 30.0, 60.0, 60.0, 60.0, 40.0, 10.0, 4.0] 
    args = (oat_flour, natures_way_protein_vanilla, sustagen, malt_extract, egg, canola_oil, soy_lecithin, iodised_salt)

    # example 2
    #x0 = [ 100.0, 75.0, 7.0, 1.0, 60.0, 80.0, 60.0, 40.0, 10.0, 75.0, 50.0, 30.0, 30.0, 30.0, 10.0, 4.0, ]
    #x1 = [ 100.0, 75.0, 7.0, 1.0, 60.0, 80.0, 60.0, 40.0, 10.0, 75.0, 50.0, 30.0, 70.0, 30.0, 10.0, 4.0, ]
    #args = (wheat_flour, oat_flour, bakers_yeast, coconut_palm_sugar, malt_extract, dates, egg, canola_oil, soy_lecithin, sunflower_seeds, peanuts, brazil_nuts, chia_seeds, wheatgerm, spearmint, iodised_salt)
    
    """
    cost = [ 0.75, # white flour
             3.29, # quick oats
            70.00, # bakers yeast
             9.70, # coconut palm sugar
            11.00, # malt extract
             7.25, # dates
             7.00, # egg
             5.60, # canola oil
            23.40, # soy lecithin
             8.00, # sunflower seeds
             5.00, # peanuts
            23.00, # brazil nuts 
            28.00, # chia seeds
             9.10, # wheatgerm
             0.00, # spearmint
             3.90] # iodized salt

    c = array(x0)*array(cost)/1e3
    
    print("cost:\n")
    print c
    print("$%3.2f/day" % (sum(c)))

    """
    
    soylent0 = user_defined_soylent(x0, args)
    
    print_recipe(x0, args)
    print_rdi(soylent0)
    
    #soylent1 = user_defined_soylent(x1, args)
    #print_rdi(soylent1)
    #print_difference(soylent0, soylent1)

    #print "# x0 = [",
    #for xi in x0: print("%.1f," % xi),
    #print "]"
    
    return

if __name__ == '__main__':
    main()
