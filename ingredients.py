#!/usr/bin/env python
#
# brief: hand written ingredients to supplemnt USDA data
# author: bto
# date: Jun 2013
#
# description:
# 
# This file is a hand-crafted list of local ingredients whose nutritional data has been verified.
# It is used to supplement (or replace) USDA data.
# There is often conflicting information when it comes to the nutritional content of ingredients.
# Remember: your soylent is only as good as the nutritional data!
# Consider creating such a list for the ingredients you plan on using.

from food_class import *

# -------------------------------------------------------------
# ingredients

# source: http://nutritiondata.self.com/facts/breakfast-cereals/1597/2
content = {'carbohydrate':55.9, 'protein':10.6, 'fat':5.3, 'fat sat':0.9, 'fiber':8.2, 'calcium':42.1e-3, 'iron':3.4e-3, 'magnesium':112e-3, 'phosphorus':332e-3, 'potassium':293e-3, 'sodium':4.9e-3, 'zinc':2.9e-3, 'copper':0.3e-3, 'manganese':2.9e-3, 'selenium':23.4e-6, 'vitamin e':0.3e-3, 'vitamin k':1.6e-6, 'thiamin':0.4e-3, 'riboflavin':0.1e-3, 'niacin':0.9e-3, 'vitamin b6':0.1e-3, 'folate':25.9e-6, 'vitamin b5':0.9e-3, 'choline':32.7e-3}
oats = food("rolled oats", 81, 1285e3, content)

# source: USDA
content = {'carbohydrate':73.0, 'protein':14.0, 'fiber':12.0, 'fat':2.0, 'sodium':6e-3}
wheat_flour = food('wheat flour', 100.0, kcal2j(339), content)

# source: USDA
#content = {'protein': 9.61, 'carbohydrate': 74.48, 'fiber': 13.1, 'calcium': 0.033, 'iron': 0.00371, 'magnesium': 0.117, 'phosphorus': 0.323, 'potassium': 0.394, 'sodium': 0.003, 'zinc': 0.00296, 'copper': 0.000475, 'manganese': 0.003399, 'selenium': 1.27e-05, 'thiamin': 0.000297, 'riboflavin': 0.000188, 'niacin': 0.005347, 'vitamin b6': 0.000191, 'folate': 2.8e-05, 'choline': 0.0312, 'vitamin a': 2.7e-06, 'vitamin e': 0.00053, 'vitamin k': 1.9e-06, 'fat sat': 0.43, 'fat mono': 0.283, 'fat poly': 1.167}
content = {'protein': 10.33, 'carbohydrate': 76.31, 'fiber': 2.7, 'calcium': 0.015, 'iron': 0.00117, 'magnesium': 0.022, 'phosphorus': 0.108, 'potassium': 0.107, 'sodium': 0.002, 'zinc': 0.0007, 'copper': 0.000144, 'manganese': 0.000682, 'selenium': 3.39e-05, 'thiamin': 0.00012, 'riboflavin': 4e-05, 'niacin': 0.00125, 'vitamin b6': 4.4e-05, 'folate': 2.6e-05, 'choline': 0.0104, 'vitamin e': 6e-05, 'vitamin k': 3e-07, 'fat sat': 0.155, 'fat mono': 0.087, 'fat poly': 0.413}
wheat_flour = food("wheat flour, white", 91.5137, 1.52298e+06, content)

# source: label
#content = {'protein': 12.4, 'carbohydrate': 58.1, 'fat':8.5, 'fat sat':1.6, 'sodium':0.0026, 'fiber':10.2, 'thiamin':1.1e-3, 'iron':5.1e-3, 'magnesium':221e-3, 'phosphorus':690e-3, 'manganese':5.3e-3, 'selenium':42.5e-6, 'zinc':2.9e-3, 'copper':0.4e-3, 'potassium':532e-3}
content = {'carbohydrate':54.8, 'protein':12.8, 'fat':9.3, 'fat sat':3.0, 'sodium':19e-3, 'fiber':12.1}
oat_flour = food("oat flour", 100.0, 1590.0e3, content)

# source: USDA
content = {'protein': 6.93, 'carbohydrate': 76.85, 'fiber': 7.3, 'calcium': 0.007, 'iron': 0.00238, 'magnesium': 0.093, 'phosphorus': 0.272, 'potassium': 0.315, 'sodium': 0.005, 'zinc': 0.00173, 'copper': 0.00023, 'manganese': 0.00046, 'selenium': 1.54e-05, 'thiamin': 0.000246, 'riboflavin': 8e-05, 'niacin': 0.0019, 'vitamin b6': 0.00037, 'folate': 2.5e-05, 'choline': 0.0216, 'vitamin a': 6.42e-05, 'vitamin e': 0.00042, 'vitamin k': 3e-07, 'fat sat': 0.543, 'fat mono': 1.018, 'fat poly': 1.759}
corn_flour = food("corn flour, whole-grain", 99.6216, 1.51042e+06, content)

# source: bulknutrients.com.au
content = {'carbohydrate':95, 'sodium': 0.05}
maltodextrin = food("maltodextrin", 100.0, 1600.0, content)

# source: bulknutrients.com.au
content = {'carbohydrate': 0.9, 'protein':91.4, 'fat':1.0, 'fat sat':0.7, 'sodium':0.185}
whey_protein_isolate = food('whey protein isolate, unflavoured', 100.0, 1606, content)

# source: label
content = {'carbohydrate':14.3, 'protein':74.4, 'fat':2.8, 'fat sat':1.0, 'sodium':0.696}
natures_way_protein_vanilla = food('natures way protein, vanilla', 100.0, 1610.0, content)

# source: label
content = {'carbohydrate':75.0, 'protein':5.0, 'sodium':40e-3, 'potassium':320e-3, 'thiamin':0.4e-3, 'riboflavin':0.2e-3, 'niacin':6.2e-3, 'vitamin b6':1.7e-3, 'vitamin b12':7e-6}
malt_extract = food("malt extract, saunders", 100.0, 1340e3, content)

# source: USDA and http://coconutpalmsugar.com/Nutritional_Information.html
content = {'carbohydrate':98.0, 'potassium':1030.0e-3, 'chloride':470.0e-3, 'calcium':8.0e-3, 'iron':2.0e-3, 'phosphorus':79.0e-3, 'magnesium':29.0e-3, 'zinc':2.0e-3, 'copper':0.23e-3, 'sulphur':26.0e-3, 'manganese':0.1e-3, 'vitamin c':23.4e-3, 'thiamin':0.41e-3}
coconut_palm_sugar = food("coconut palm sugar", 100.0, 813.3e3, content)

content = {}
raw_sugar = food("raw sugar", 100.0, content)

# source: label
content = {'fat':1.0, 'fiber':3.0, 'protein':17.0, 'vitamin a':iu2g('vitamin a',200), 'vitamin d':iu2g('vitamin d', 400), 'vitamin e':iu2g('vitamin e', 5), 'vitamin k':5e-6}
raw_protein = food('raw protein, unflavoured', 22.0, kcal2j(80), content) 

# source: USDA, vitamin b5 from http://www.healthaliciousness.com/articles/foods-high-in-pantothenic-acid-vitamin-B5.php
content = {'protein': 12.56, 'carbohydrate': 0.72, 'calcium': 0.056, 'iron': 1.75e-3, 'magnesium': 0.012, 'phosphorus': 0.198, 'potassium': 0.138, 'sodium': 0.142, 'zinc': 0.00129, 'copper': 7.2e-05, 'manganese': 2.8e-05, 'selenium': 3.07e-05, 'thiamin': 4e-05, 'riboflavin': 0.000457, 'niacin': 7.5e-05, 'vitamin b6': 0.00017, 'folate': 4.7e-05, 'choline': 0.2938, 'vitamin b12': 8.9e-07, 'vitamin a': 0.000162, 'vitamin e': 0.00105, 'vitamin d': 2e-06, 'vitamin k': 3e-07, 'fat sat': 3.126, 'fat mono': 3.658, 'fat poly': 1.911, 'cholesterol': 0.372, 'sulphur': 180e-3, 'vitamin b5': 1.53e-3}
egg = food('egg, whole, raw', 33.072, 598.312e3, content)

# source: vitasoy website
content = {'carbohydrate':6.0, 'protein':3.2, 'fat':3.0, 'fat sat':0.6, 'fat mono':0.7, 'fat poly':1.7, 'sodium':43e-3, 'fiber':1e-3, 'calcium':160e-3, 'phosphorus':108e-3, 'magnesium':20e-3, 'vitamin a':54e-6, 'vitamin b12':0.4e-6, 'vitamin d':2e-6}
vitasoy_calci_plus = food('vitasoy calci-plus', 100.0, 270e3, content)

# source: label
content = {'carbohydrate':1.0, 'protein':25.0, 'fat':1.5, 'calcium':940e-3, 'iron':11e-3, 'phosphorus':650e-3, 'iodine':52e-6, 'magnesium':120e-3, 'zinc':6.3e-3, 'selenium':20e-6, 'copper':0.7e-3, 'manganese':1.3e-3, 'chromium':30e-6, 'vitamin a':iu2g('vitamin a',1750), 'vitamin b6':0.7e-3, 'vitamin b12':2.1e-6, 'vitamin c':21e-3, 'vitamin d':iu2g('vitamin d',140), 'vitamin e':iu2g('vitamin e',10), 'vitamin k':22e-6, 'thiamin':0.52e-3, 'riboflavin':0.55e-3, 'niacin':7e-3, 'folate':140e-6, 'biotin':100e-6, 'vitamin b5':3.5e-3}
trader_darwins_protein = food("trader darwin's protein", 33.0, kcal2j(120), content)

# source: label
content = {'fat':49.1, 'fat sat':3.75, 'fat mono':31.6, 'fat poly':13.75, 'fat omega3':4.5, 'fat omega6':9.25}
canola_oil = food('canola oil', 50.0, kcal2j(442), content)

# source: label, guess for choline (originally 0.75).
content = {'fat':3.25, 'fat poly':3.25, 'fat omega3':0.35, 'fat omega6':2.9, 'calcium':0.02, 'phosphorus':0.3, 'choline':0.2}
soy_lecithin = food("soy lecithin", 10.0, kcal2j(25), content) 

# source: label
content = {'protein': 24.5, 'carbohydrate': 66.2, 'fiber': 0.0, 'calcium': 0.667, 'iron': 134.0e-3, 'magnesium': 0.134, 'phosphorus': 0.741, 'potassium': 1.08, 'sodium': 0.25, 'zinc': 0.005, 'vitamin c': 26.7e-3, 'thiamin': 642e-6, 'riboflavin': 992e-6, 'niacin': 5.9e-3, 'vitamin b6': 667e-6, 'folate': 117e-6, 'vitamin b12': 1.17e-6, 'vitamin a': 312e-6, 'vitamin e': 6.67e-3, 'vitamin d': 4.1e-6, 'fat sat': 0.4, 'iodine': 62.5e-6}
sustagen = food("sustagen sport vanilla", 100.0, 1570.0, content)

# source: label
content = {'potassium':5.5e-3, 'calcium':10e-3, 'iron':1.9e-3, 'phosphorus':2.5e-3, 'iodine':50e-6, 'magnesium':30e-3, 'zinc':2.5e-3, 'selenium':25e-6, 'copper':20e-6, 'manganese':1e-3, 'chromium':5e-6, 'molybdenum':25e-6, 'vitamin a':151.5e-6, 'vitamin b6':2e-3, 'vitamin b12':4e-6, 'vitamin c':25e-3, 'vitamin d':7.5e-6, 'vitamin e':3e-3, 'vitamin k':18e-6, 'riboflavin':2.5e-3, 'folate':100e-6, 'biotin':50e-6, 'vitamin b5':9e-3}
multi_vitamin = food("bioglan multi-vitamin", 1, 0, content)

# source: USDA
content = { 'protein': 40.44, 'carbohydrate': 41.22, 'fiber': 26.9, 'calcium': 0.03, 'iron': 0.00217, 'magnesium': 0.054, 'phosphorus': 0.637, 'potassium': 0.955, 'sodium': 0.051, 'zinc': 0.00794, 'copper': 0.000436, 'manganese': 0.000312, 'selenium': 7.9e-06, 'vitamin c': 0.0003, 'thiamin': 0.01099, 'riboflavin': 0.004, 'niacin': 0.0402, 'vitamin b6': 0.0015, 'folate': 0.00234, 'choline': 0.032, 'vitamin b12': 7e-08, 'vitamin k': 4e-07, 'fat sat': 1.001, 'fat mono': 4.309, 'fat poly': 0.017 }
bakers_yeast = food("bakers yeast", 123.326, 1.3598e+06, content)

# source: label
content = {'carbohydrate':15, 'protein': 10.0, 'fat':2.5, 'fat sat': 1, 'fiber': 8, 'cholesterol': 25e-3, 'calcium': 0.2, 'chloride': 0.15, 'chromium': 120e-6, 'copper': 2e-3, 'iodine': 150e-6, 'magnesium':50e-3, 'manganese':2e-3, 'molybdenum': 75e-6, 'potassium':0.25, 'selenium': 200e-6, 'zinc':25e-3, 'vitamin a':iu2g('vitamin a', 5000), 'vitamin b6': 50e-3, 'vitamin b12': 50e-6, 'vitamin c': 300e-3, 'vitamin d':iu2g('vitamin d', 600), 'vitamin e':iu2g('vitamin e', 30), 'vitamin k': 80e-6, 'thiamin': 50e-3, 'riboflavin': 50e-3, 'niacin': 50e-3, 'folate': 600e-6, 'vitamin b5':50e-3, 'biotin':300e-6, 'choline':10e-3}
gnc_mega_men = food('gnc mega men sport, vanilla bean', 23, kcal2j(130), content)

content = {'potassium': 270e-3}
potassium_gluconate = food("potassium gluconate", 1.74, 0.0, content)

content = {'protein': 2.18, 'carbohydrate': 63.88, 'fiber': 7.1, 'calcium': 0.043, 'iron': 0.00093, 'magnesium': 0.041, 'phosphorus': 0.069, 'potassium': 0.732, 'sodium': 0.002, 'zinc': 0.00044, 'copper': 0.000281, 'manganese': 0.000299, 'selenium': 3e-07, 'vitamin c': 0.0006, 'thiamin': 5.1e-05, 'riboflavin': 0.000186, 'niacin': 0.001882, 'vitamin b6': 0.000205, 'folate': 4e-06, 'choline': 0.0101, 'vitamin a': 0.0002343, 'vitamin e': 0.00043, 'vitamin k': 5.95e-05, 'fat sat': 0.088, 'fat mono': 0.053, 'fat poly': 0.062}
prunes = food("prunes", 112.776, 1.00416e+06, content)

# source: http://nz.freshlife.com.au/nutritionfacts.cfm
content = {'carbohydrate':2.4, 'protein':14.4, 'fat':68.5, 'fat sat':14.8, 'fat mono':21.8, 'fat poly':29.0, 'sodium':2.0e-3, 'potassium':0.6265, 'fiber':8.5, 'calcium':160.0e-3, 'iron':2.4e-3, 'iodine':0.0, 'magnesium':0.035e-3, 'zinc':4.1e-3, 'selenium':1917.0e-6, 'copper':1.74e-3, 'manganese':1.22e-3, 'vitamin b6':0.101e-3, 'vitamin e':5.7e-3, 'thiamin':0.62e-3, 'niacin':0.295e-3, 'folate':22.0e-9, 'vitamin b5':0.184e-3} 
brazil_nuts = food("brazil nuts, dried", 100.0, 2890.0, content)

# source: USDA
content = {'protein': 18.29, 'carbohydrate': 28.88, 'fiber': 27.3, 'calcium': 0.255, 'iron': 0.00573, 'magnesium': 0.392, 'phosphorus': 0.642, 'potassium': 0.813, 'sodium': 0.03, 'zinc': 0.00434, 'copper': 0.00122, 'manganese': 0.002482, 'selenium': 2.54e-05, 'vitamin c': 0.0006, 'thiamin': 0.001644, 'riboflavin': 0.000161, 'niacin': 0.00308, 'vitamin b6': 0.000473, 'folate': 8.7e-05, 'choline': 0.0787, 'vitamin e': 0.00031, 'vitamin k': 4.3e-06, 'fat sat': 3.663, 'fat mono': 7.527, 'fat poly': 28.73}
flax_seeds = food("flax seeds", 160.331, 2.23426e+06, content) 

content = {'protein': 16.54, 'carbohydrate': 42.12, 'fiber': 34.4, 'calcium': 0.631, 'iron': 0.00772, 'magnesium': 0.335, 'phosphorus': 0.86, 'potassium': 0.407, 'sodium': 0.016, 'zinc': 0.00458, 'copper': 0.000924, 'manganese': 0.002723, 'selenium': 5.52e-05, 'vitamin c': 0.0016, 'thiamin': 0.00062, 'riboflavin': 0.00017, 'niacin': 0.00883, 'folate': 4.9e-05, 'vitamin a': 1.62e-05, 'vitamin e': 0.0005, 'fat sat': 3.33, 'fat mono': 2.309, 'fat poly': 23.665}
chia_seeds = food("chia seeds, dried", 155.381, 2.03342e+06, content) 

# source: http://nz.freshlife.com.au/nutritionfacts.cfm
content = {'protein': 20.78, 'carbohydrate': 20.0, 'fiber': 8.6, 'calcium': 0.078, 'iron': 5.25e-3, 'magnesium': 0.325, 'phosphorus': 0.66, 'potassium': 0.645, 'sodium': 0.009, 'zinc': 0.005, 'copper': 0.0018, 'manganese': 0.00195, 'selenium': 5.3e-05, 'vitamin c': 0.0014, 'thiamin': 0.00148, 'riboflavin': 0.000355, 'niacin': 0.008335, 'vitamin b6': 0.001345, 'folate': 0.000227, 'choline': 0.0551, 'vitamin b12': 0.0, 'vitamin a': 1.5e-05, 'vitamin e': 0.03517, 'vitamin d': 0.0, 'vitamin k': 0.0, 'fat sat': 4.455, 'fat mono': 18.528, 'fat poly': 23.137}
sunflower_seeds = food("sunflower seeds, dried", 151.415, 2.44346e+06, content)

# source: http://nz.freshlife.com.au/nutritionfacts.cfm
content = {'protein': 15.03, 'carbohydrate': 17.6, 'fiber': 9.4, 'calcium': 0.123, 'iron': 4.38e-3, 'magnesium': 0.173, 'phosphorus': 0.31, 'potassium': 0.755, 'sodium': 0.0, 'zinc': 0.0025, 'copper': 0.00175, 'manganese': 0.00555, 'selenium': 4.1e-06, 'vitamin c': 0.0038, 'thiamin': 0.000338, 'riboflavin': 0.000123, 'niacin': 0.00205, 'vitamin b6': 0.00062, 'folate': 8.8e-05, 'choline': 0.0, 'vitamin b12': 0.0, 'vitamin a': 1.83e-05, 'vitamin e': 0.01528, 'vitamin d': 0.0, 'vitamin k': 0.0, 'fat sat': 4.511, 'fat mono': 46.608, 'fat poly': 8.463}
hazelnuts = food("hazelnuts, roasted", 170.3, 2.70286e+06, content)

# source: label, micronutrients as for roasted peanuts
content = {'carbohydrate': 9.0, 'protein': 24.7, 'fat': 47.1, 'fat sat': 7.0, 'fiber': 8.2, 'sodium': 1.0e-3, 'potassium': 540e-3, 'niacin': 8.692e-3, 'copper': 431.3e-6, 'zinc': 2.127e-3, 'biotin': 462.7e-6, 'choline': 35.54e-3, 'vitamin e': 4.45e-3, 'selenium': 4.82e-6, 'thiamin': 281.5e-6, 'manganese': 1.339e-3, 'folate': 93.19e-6, 'calcium': 34.71e-3, 'riboflavin': 62.98e-06, 'vitamin b6': 164.5e-6, 'magnesium': 113.1e-3, 'iron': 1.452e-3, 'phosphorus': 230.1e-3}
raw_peanuts = food("peanuts, raw", 100.0, 2.31e6, content)

# source: http://nz.freshlife.com.au/nutritionfacts.cfm, biotin from whfoods.com
content = {'protein': 23.68, 'carbohydrate': 21.51, 'fiber': 8, 'calcium': 0.054, 'iron': 2.26e-3, 'magnesium': 0.176, 'phosphorus': 0.358, 'potassium': 0.658, 'sodium': 0.006, 'zinc': 0.00331, 'copper': 0.000671, 'manganese': 0.002083, 'selenium': 7.5e-06, 'thiamin': 0.000438, 'riboflavin': 9.8e-05, 'niacin': 0.013525, 'vitamin b6': 0.000256, 'folate': 0.000145, 'choline': 0.0553, 'vitamin e': 0.00693, 'fat sat': 6.893, 'fat mono': 24.64, 'fat poly': 15.694, 'biotin': 720e-6, 'molybdenum': 200e-6}
peanuts = food("peanuts, roasted", 155.594, 2.44764e+06, content)

# source: http://nz.freshlife.com.au/nutritionfacts.cfm, nutritiondata.self.com (vitamin k)
content = {'carbohydrate':13.7, 'protein':24.4, 'fat':45.6, 'fat sat':7.0, 'fat mono':11.2, 'fat poly':18.2, 'sodium':18.0e-3, 'potassium':0.20, 'fiber':10.2, 'calcium':43e-3, 'iron':14.97e-3, 'magnesium':0.32e-3, 'zinc':7.46e-3, 'selenium':5.6e-6, 'copper':1.387e-3, 'manganese':3.021e-3, 'vitamin a':iu2g('vitamin a', 19.0), 'vitamin k':51e-6, 'thiamin':0.21e-3, 'riboflavin':0.32e-3, 'niacin':1.745e-3, 'folate':58e-6, 'vitamin b5':0.339e-3}
pumpkin_seeds = food("pumpkin seeds, dried", 100.0, 2420.0, content)

# source: USDA
content = {'protein': 23.15, 'carbohydrate': 51.8, 'fiber': 13.2, 'calcium': 0.039, 'iron': 6.26e-3, 'magnesium': 0.239, 'phosphorus': 0.842, 'potassium': 0.892, 'sodium': 0.012, 'zinc': 0.01229, 'copper': 0.000796, 'manganese': 0.013301, 'selenium': 7.92e-05, 'thiamin': 0.001882, 'riboflavin': 0.000499, 'niacin': 0.006813, 'vitamin b6': 0.0013, 'folate': 0.000281, 'fat sat': 1.665, 'fat mono': 1.365, 'fat poly': 6.01, 'molybdenum': 100e-6, 'chromium':28e-6}
wheatgerm = food("wheatgerm", 109, 1.506e6, content)

# source: USDA, used molybdenum value for wheatgerm from everynutrient.com/molybdenum.html, chromium from http://www.healthfitonline.com/resources/articles/chromium.html
content = {'protein': 15.55, 'carbohydrate': 64.51, 'fiber': 42.8, 'calcium': 0.073, 'iron': 10.57e-3, 'magnesium': 0.611, 'phosphorus': 1.013, 'potassium': 1.182, 'sodium': 0.002, 'zinc': 0.00727, 'copper': 0.000998, 'manganese': 0.0115, 'selenium': 7.76e-05, 'thiamin': 0.000523, 'riboflavin': 0.000577, 'niacin': 0.013578, 'vitamin b6': 0.001303, 'folate': 7.9e-05, 'choline': 0.0744, 'vitamin a': 2.7e-06, 'vitamin e': 0.00149, 'vitamin k': 1.9e-06, 'fat sat': 0.63, 'fat mono': 0.637, 'fat poly': 2.212, 'molybdenum': 100e-6, 'chromium':28e-6}
wheat_bran = food("wheat bran", 134.002, 903744, content)

# source: USDA
content = {'protein':2.2, 'fat':1.3, 'fat sat':0.0, 'fat mono':0.9, 'fat poly':3.4, 'fat omega3':2.7, 'fat omega6':0.7, 'fiber':3.3, 'phosphorus':0.77, 'magnesium':0.047}
linseed_meal = food("linseed meal", 12, kcal2j(64), content)

# source: USDA
content = {'protein': 19.6, 'carbohydrate': 57.9, 'fiber': 33.2, 'calcium': 0.128, 'iron': 13.86e-3, 'magnesium': 0.0, 'phosphorus': 0.734, 'potassium': 1.524, 'sodium': 0.021, 'zinc': 0.00681, 'copper': 0.003788, 'manganese': 0.003837, 'selenium': 1.43e-05, 'thiamin': 7.8e-05, 'riboflavin': 0.000241, 'niacin': 0.002185, 'vitamin b6': 0.000118, 'folate': 3.2e-05, 'choline': 0.012, 'vitamin e': 0.0001, 'vitamin k': 2.5e-06, 'fat sat': 8.07, 'fat mono': 4.57, 'fat poly': 0.44}
cocoa_powder = food("cocoa,dry pdr,unswtnd", 142.179, 953952, content)

# source: USDA, fiber from label
content = { 'protein': 1.81, 'carbohydrate': 74.97, 'fiber': 15.0, 'calcium': 0.064, 'iron': 0.0009, 'magnesium': 0.054, 'phosphorus': 0.062, 'potassium': 0.696, 'sodium': 0.001, 'zinc': 0.00044, 'copper': 0.000362, 'manganese': 0.000296, 'thiamin': 5e-05, 'riboflavin': 6e-05, 'niacin': 0.00161, 'vitamin b6': 0.000249, 'folate': 1.5e-05, 'choline': 0.0099, 'vitamin a': 4.47e-05, 'vitamin k': 2.7e-06}
dates = food("dates, medjool", 150.991, 1.15897e+06, content)

# source: USDA
content = {'protein': 6.88, 'carbohydrate': 23.65, 'fiber': 16.3, 'calcium': 0.026, 'iron': 3.32e-3, 'magnesium': 0.09, 'phosphorus': 0.206, 'potassium': 0.543, 'sodium': 0.037, 'zinc': 0.00201, 'copper': 0.000796, 'manganese': 0.002745, 'selenium': 1.85e-05, 'vitamin c': 0.0015, 'thiamin': 6e-05, 'riboflavin': 0.0001, 'niacin': 0.000603, 'vitamin b6': 0.0003, 'folate': 9e-06, 'choline': 0.0221, 'vitamin e': 0.00044, 'vitamin k': 3e-07, 'fat sat': 57.218, 'fat mono': 2.745, 'fat poly': 0.706}
desiccated_coconut = food("desiccated coconut", 180.315, 2.76144e+06, content)

# source: USDA + guess for vitamin k
content = { 'protein': 3.29, 'carbohydrate': 8.41, 'fiber': 6.8, 'calcium': 0.199, 'iron': 11.87e-3, 'magnesium': 0.063, 'phosphorus': 0.06, 'potassium': 0.458, 'sodium': 0.03, 'zinc': 0.00109, 'copper': 0.00024, 'manganese': 0.001118, 'vitamin c': 0.0133, 'thiamin': 7.8e-05, 'riboflavin': 0.000175, 'niacin': 0.000948, 'vitamin b6': 0.000158, 'folate': 0.000105, 'vitamin a': 0.0012162, 'vitamin k': 150e-6, 'fat sat': 0.191, 'fat mono': 0.025, 'fat poly': 0.394}
spearmint = food("spearmint", 20.6803, 184096, content)

# source: label
content = {'chloride': 1.2, 'sodium': 0.8, 'iodine': 94e-6}
iodised_salt = food("iodised salt", 2, 0, content)

