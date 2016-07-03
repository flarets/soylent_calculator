# Whole food soylent

A Soylent calculator written in Python.

To get started, simply write

    $ python soylent.py

from the command line. 
Once you have used this program to get close to a suitable recipe, you can use the optimizer to adjust the amounts by writing

    $ python optimize_soylent.py

from the command line. 
This program uses the SciPy `fmin()` function to minimize the standard deviation of the nutritional value of the recipe to the RDI.
One such recipe is described [here][2].
This is a whole-food, lactose-free soylent slice that approximately meets Rob Rinehart's RDI for an adult male.
Using whole foods instead of powders or pills reduces the overall cost.
Remember your recipe is only as good as your nutritional information.
It is best to verify (or substitute) nutritional information from the USDA database with that from the label.

## DIY RDI
If you substitute your own RDI, the following information may be useful:

*carbohydrate*
 - not all carbohydrates are created equal: a mixture of GI levels will provide more consistent energy between meals

*protein*
 - 0.8g of protein per kg of body weight

*fat*
 - Omega-6 and Omega-3 fatty acids should be in a ratio 3:1
 - avoid excess arachodonic acid

*fibre*
 - 14g per 1000 kcal

## Optional extras

*muscle*
 - 5g creatine w/ 70g maltodextrin before exercise

*nootropic*
 - 2mg piracetam w/ 500mg choline before work OR 1 cup coffee

## References
 - [hackerschool soylent][3]
 - [USDA data][5]
 - [Rob Rinehart][6]
 - [Official Soylent][4]

[2]: https://bto.io/index.php?page=projects&article=whole-food_soylent
[3]: https://github.com/zda/soylent
[4]: http://soylent.me
[5]: https://ndb.nal.usda.gov/ndb/search/list
[6]: https://github.com/engibeer
