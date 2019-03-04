# Error-Analysis
### This Module contains methods to calculates basic mathematical functions with error

Functions:
- sum
- subtract
- multiply
- divide
- mean
- stdv (STDV is an error itself. However in some cases, such as DIMM Calculations, changes in location driven from STDV of x, y coordinates and x and y coordinates has uncertainties and this error must be caaried after STDV calculation. http://www.astro.auth.gr/~seeing-gr/seeing_gr_files/theory/node13.html)
- sin, cos, tan, cot, sec, cos (arcsin, arccos etc coming soon) and array vcersions
- rad2deg, deg2rad and array vcersions

for usage look at:
[main.py](https://github.com/mshemuni/Error-Analysis/blob/master/main.py).


# Sources:
http://science.widener.edu/svb/stats/error.html

http://lectureonline.cl.msu.edu/~mmp/labs/error/e2.htm

https://math.stackexchange.com/questions/1045076/calculate-uncertainty-of-sine-function-result

Please note that this module is written in Python3 and will not directly work with python2 (You need to modify the code).
And do not hasitate to ask if you want to some other functions to be added.
