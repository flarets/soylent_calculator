#!/usr/bin/env python
#
# brief: defines the food class, and some useful functions, for use in soylent calculator
# author: bto
# date: Jun 2013

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

class food(object):
    def __init__(self, n = '', m = 1, e = 0.0, c = {}):
        self.name = n # label
        self.mass = m # serving size, g
        self.energy = e # energy, J
        self.content = {
            'carbohydrate':0.0,
            'protein':0.0,
            'fat':0.0,
            'fat sat':0.0,
            'fat mono':0.0,
            'fat poly':0.0,
            'fat omega3':0.0,
            'fat omega6':0.0,
            'sodium':0.0,
            'potassium':0.0,
            'chloride':0.0,
            'fiber':0.0,
            'calcium':0.0,
            'iron':0.0,
            'phosphorus':0.0,
            'iodine':0.0,
            'magnesium':0.0,
            'zinc':0.0,
            'selenium':0.0,
            'copper':0.0,
            'manganese':0.0,
            'chromium':0.0,
            'molybdenum':0.0,
            'vitamin a':0.0,
            'vitamin b6':0.0,
            'vitamin b12':0.0,
            'vitamin c':0.0,
            'vitamin d':0.0,
            'vitamin e':0.0,
            'vitamin k':0.0,
            'thiamin':0.0,
            'riboflavin':0.0,
            'niacin':0.0,
            'folate':0.0,
            'biotin':0.0,
            'choline':0.0,
            'vitamin b5':0.0,
            'sulphur':0.0,
            'cholesterol':0.0
        }
        for key,value in c.iteritems():
            if key in self.content.keys():
                # content per gram
                self.content[key] = value
            else:
                print('%s not in content list' % key)

    def serving_size(self, m):
        for key in self.content.keys():
            self.content[key] *= m/self.mass
        self.energy *= m/self.mass
        self.mass = m

    def __add__(self, other):
        n = 'mixture'
        m = self.mass + other.mass
        e = self.energy + other.energy
        c = {}
        for key in self.content.keys():
            c[key] = self.content[key] + other.content[key]
        return food(n,m,e,c)

    def __str__(self):
        s =  ('%s\n' % (self.name))
        s += ('  mass = %gg\n' % (self.mass))
        s += ('  energy = %gkJ\n' % (self.energy/1e3))
        s += ('  content per serve: ')
        sorted_content = sorted(self.content.iteritems(), key=operator.itemgetter(1), reverse=True)
        for key,value in sorted_content:
            if key not in self.content.keys(): continue
            if value != 0.0:
                s += ('%s = %gg, ' % (key,value))
        return s

