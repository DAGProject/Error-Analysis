#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 09:39:22 2018

@author: msh
"""

from MyErr import err
from numpy import array as ar

minor = err.Minor(verb=True)
major = err.Major(verb=True)
const = err.Constant(verb=True)

a = ar([[30, 0.01],[5, 0.05], [10, 0.8], [25, 0.1]])
b = ar([2, 0.07])
c = ar([5, 0.17])
num = 2

#Sum
print("Sum of two numbers:")
print(minor.sum(b, c))

print("Sum of whole array:")
print(minor.ar_sum_inner(a))

print("Sum of whole array with a number:")
print(minor.ar_sum(a, b))

#Subtraction
print("Difference between two numbers:")
print(minor.subtact(b, c))

#Multipication
print("Multipication of two numbers:")
print(minor.multiply(b, c))

print("Multipication of whole array:")
print(minor.ar_multiply_inner(a))

print("Multipication of whole array with a number:")
print(minor.ar_multiply(a, c))

#Division
print("Division of two numbers:")
print(minor.divide(b, c))

#Power
print("Power of a number with a constant:")
print(minor.power(b, num))

#Logarithm
print("Logarithm of a number:")
print(minor.log10(b))

print("Natural logarithm of a number:")
print(minor.log(c))

#Average
print("Average of an array:")
print(major.mean(a))

#STDEV
print("Stabdard deviation of an array:")
print(major.stdv(a))

#Constatns
print("Pi:")
print(const.pi())
print("Euler's number:")
print(const.e())