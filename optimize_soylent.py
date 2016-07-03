#! /usr/bin/env python
#
# brief: soylent recipe optimizer
# author: bto
# date: Jun 2013
#
# description:
# 
# This would benefit from some kind of bounded search method, whereby min/max of each ingredient were used

from scipy.optimize import *

from soylent import *

# -------------------------------------------------------------
# nutrient list

nutrient_list = ['carbohydrate', 'protein', 'fat', 'fiber', 'potassium', 'chloride', 'sodium', 'sulphur', 'calcium', 'phosphorus', 'choline', 'magnesium', 'vitamin c', 'niacin', 'vitamin e', 'iron', 'zinc', 'vitamin b5', 'vitamin b6', 'riboflavin', 'thiamin', 'manganese', 'copper', 'vitamin a', 'selenium', 'folate', 'iodine', 'vitamin k', 'vitamin d', 'vitamin b12']

#def soylent_fmin(x, wheat_flour, oat_flour, bakers_yeast, coconut_palm_sugar, malt_extract, dates, egg, canola_oil, soy_lecithin, sunflower_seeds, peanuts, brazil_nuts, chia_seeds, wheatgerm, spearmint, iodised_salt):
#    args = (wheat_flour, oat_flour, bakers_yeast, coconut_palm_sugar, malt_extract, dates, egg, canola_oil, soy_lecithin, sunflower_seeds, peanuts, brazil_nuts, chia_seeds, wheatgerm, spearmint, iodised_salt)

def soylent_fmin(x, *args):
    for i in range(len(args)):
        args[i].serving_size(x[i])
    
    soylent = args[0]
    for i in range(1,len(args)):
        soylent = soylent + args[i]
    #print_rdi(soylent)

    y = []
    for key in nutrient_list:
        y.append(soylent.content[key]/rdi[key] - 1.0)
        #print key, y[-1] 
    
    yy = 0
    for i in range(len(y)):
        yy += y[i]**2
    yy += (soylent.energy/rde - 1.0)**2
    
    y_stddev = sqrt(yy)

    # penalise negative quantities
    for xi in x:
        if xi < 0:
            y_stddev += -xi*10
    
    # penalise not enough carbs
    #if y[0] < 0.0:
    #    y_stddev += (-y[0])
    
    # penalise too much sugar
    if x[2] > x[1]:
        y_stddev += (x[2]/x[1]-1.0)
    
    return y_stddev

def optimize_soylent(x0, args):
    return fmin(soylent_fmin, x0, args=args, retall=True, maxfun=10e3, maxiter=10e3)


def main():
    x0 = [100.0, 30.0, 60.0, 60.0, 60.0, 40.0, 10.0, 4.0] 
    args = (oat_flour, natures_way_protein_vanilla, sustagen, malt_extract, egg, canola_oil, soy_lecithin, iodised_salt)
    
    out = optimize_soylent(x0, args)
    
    # print all x arrays searched

    #for i in out[1]:
    #    for j in i:
    #        print j,
    #    print
    
    x_opt = out[1][-1]
    s_opt = user_defined_soylent(x_opt, args)
    print_recipe(x_opt, args)
    print_rdi(s_opt)
    
if __name__ == '__main__':
    main()  
