#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 09:40:23 2018

@author: msh
"""
from numpy import asarray as ar
from numpy import power
from numpy import log10
from numpy import log

class Etc():
    """Just to create a print_if function"""
    def __init__(self, verb=True):
        self.verb = verb
        
    def print_if(self, text):
        """Prints given text if verb value is True"""
        if self.verb:
            print(text)

class Minor():
    """Minor operations"""
    def __init__(self, verb=True):
        self.verb = verb
        self.etc = Etc(verb=self.verb)
        
    def sum(self, val1, val2):
        """Calculates sum of two values abd their errors"""
        try:
            ret = val1[0] + val2[0]
        except Exception as e:
            self.etc.print_if(e)
            ret = None
        try:
            eret = power(power(val1[1], 2) + power(val2[1], 2), 0.5)
        except Exception as e:
            self.etc.print_if(e)
            eret = None
            
        return(ar([ret, abs(eret)]))
        
    def ar_sum_inner(self, in_arr):
        """Calculates sum of all values and their error given in an array
        Calls sum method to do so"""
        the_sum = in_arr[0]
        for i in in_arr[1:]:
            the_sum = self.sum(the_sum, i)
    
        return(ar(the_sum))
        
    def ar_sum(self, in_arr, num):
        """Calculates sum of all values and their errors for 
        a given array with a number
        Calls sum method to do so"""
        the_sums = []
        for i in in_arr:
            the_sums.append(ar(self.sum(i, num)))
    
        return(ar(the_sums))
            
    def subtact(self, val1, val2):
        """Calculates subtraction of given two values and their errors"""
        try:
            ret = self.sum(val1, [-1 * val2[0], val2[1]])
            return ar(ret)
        except Exception as e:
            self.etc.print_if(e)
            return ar([None, None])
        
    def multiply(self, val1, val2):
        """Calculates multipication of two value and their errors"""
        try:
            ret = val1[0] * val2[0]
        except Exception as e:
            self.etc.print_if(e)
            ret = None
        try:
            eret = ret * power(power(val1[1] / val1[0], 2) +
                               power(val2[1] / val2[0], 2), 0.5)
        except Exception as e:
            self.etc.print_if(e)
            eret = None
        
        return(ar([ret, abs(eret)]))
        
    def ar_multiply_inner(self, in_arr):
        """Calculates multipication of all values and 
        their error given in an array
        Calls multiply method to do so"""
        the_mul = in_arr[0]
        for i in in_arr[1:]:
            the_mul = self.multiply(the_mul, i)
    
        return(ar(the_mul))
        
    def ar_multiply(self, in_arr, num):
        """Calculates multipication of all values and their errors for 
        a given array with a number
        Calls multiply method to do so"""
        the_muls = []
        for i in in_arr:
            the_muls.append(ar(self.multiply(i, num)))
    
        return(ar(the_muls))
        
    def divide(self, val1, val2):
        """Calculates division of two value and their errors
        Calls multiply method to do so"""
        try:
            ret = self.multiply(val1, [1/val2[0], val2[1]])
            return(ret)
        except Exception as e:
            self.etc.print_if(e)
            return([None, None])
            
    def power(self, bs, pw):
        """Calculates power of a value to a constant and its errors"""
        try:
            ret = power(bs[0], pw)
            eret = ret * pw * (bs[1] / bs[0])
        except:
            ret = None
            eret = None
    
        return(ar([ret, abs(eret)]))
        
    def log10(self, val):
        """Calculates logarithm of a value and its errors"""
        try:
            ret = log10(val[0])
            eret = 0.434 * (val[1] / val[0])
        except Exception as e:
            self.etc.print_if(e)
            ret = None
            eret = None
        
        return(ar([ret, abs(eret)]))
        
    def log(self, val):
        """Calculates natural logarithm of a value and its errors"""
        try:
            ret = log(val[0])
            eret = val[1] / val[0]
        except Exception as e:
            self.etc.print_if(e)
            ret = None
            eret = None
            
        return(ar([ret, abs(eret)]))
        
class Major():
    """Major operations"""
    def __init__(self, verb=True):
        self.verb = verb
        self.etc = Etc(verb=self.verb)
        self.minor = Minor(verb=self.verb)
        
    def mean(self, in_arr):
        """Calculates mean of given values and their errors"""
        try:
            sums = self.minor.ar_sum_inner(in_arr)
            ret = self.minor.multiply(sums, [1/len(in_arr), 0])
        except Exception as e:
            self.etc.print_if(e)
            ret = [None, None]
            
        return(ret)
        
    def stdv(self, in_arr):
        """Calculates standard deviation of given values and their errors"""
        try:
            mean = self.mean(in_arr)
            the_subs = []
            for i in in_arr:
                the_subs.append(self.minor.power(
                        self.minor.sum(i, -1 * mean), 2))
            
            the_subs = ar(the_subs)
            sq_sum = self.minor.ar_sum_inner(the_subs)
            sq_sum_o_num = self.minor.multiply(sq_sum, [1/len(the_subs), 0])
            ret = self.minor.power(sq_sum_o_num, 0.5)
        except Exception as e:
            self.etc.print_if(e)
            ret = ar([None, None])
            
        return(ret)
        
class Constant():
    """Constatns"""
    def __init__(self, verb=True):
        self.verb = verb
        
    def pi(self):
        """Returns Pi's value with 10^-9 error"""
        try:
            ret = 3.14159265
            eret = 10**-9
        except Exception as e:
            self.etc.print_if(e)
            ret= None
            eret = None
        
        return(ar([ret, eret]))
        
    def e(self):
        """Returns Euler's number's value with 10^-9 error"""
        try:
            ret = 2.71828182
            eret = 10**-9
        except Exception as e:
            self.etc.print_if(e)
            ret= None
            eret = None
        
        return(ar([ret, eret]))
    