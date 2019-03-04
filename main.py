#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 09:39:22 2018

@author: msh
"""

from MyErr import err
from numpy import array as ar

trigo = err.Trigo(verb=True)
minor = err.Minor(verb=True)
major = err.Major(verb=True)
const = err.Constant(verb=True)

a = ar([[30, 0.01],[5, 0.05], [10, 0.8], [25, 0.1]])
b = ar([2, 0.07])
c = ar([5, 0.17])
num = 2
deg = [30, 0.2]
rad = trigo.deg2rad([60, 0.2])

print("\n****VALUES****\n")
print("a = {}".format(a))
print("b = {}".format(b))
print("c = {}".format(c))
print("num = {}".format(num))
print("deg = {}".format(deg))
print("rad = {}".format(rad))

print("\n****TRIGONOMETRY****\n")

print("\n***SIN***")
print("sin(rad) = {}".format(trigo.sin(rad)))

print("\n***COS***")
print("cos(deg) = {}".format(trigo.cos(deg, degree=True)))

print("\n***TAN***")
print("tan(rad) = {}".format(trigo.tan(deg, degree=False)))

print("\n***COTAN***")
print("cot(deg) = {}".format(trigo.cot(deg, degree=True)))

print("\n***RAD to DEG***")
print("rad2deg(rad) = {}".format(trigo.rad2deg(rad)))

print("\n***DEG to RAD***")
print("deg2rad(deg) = {}".format(trigo.deg2rad(deg)))



print("\n****CALCULATIONS****\n")
print("\n***SUM***")
print("b + c = {}".format(minor.sum(b, c)))
print("sum(a) = {}".format(minor.ar_sum_inner(a)))
print("a + c = {}".format(minor.ar_sum(a, c)))

print("\n***MULTIPICATION***")
print("b * c = {}".format(minor.multiply(b, c)))
print("a * c = {}".format(minor.ar_multiply(a, c)))



print("\n***POWER***")
print("b^num = {}".format(minor.power(b, num)))


print("\n***LOGARITHM***")
print("log(b) = {}".format(minor.log10(b)))
print("ln(c) = {}".format(minor.log(c)))

print("\n***MEAN***")
print("mean(a) = {}".format(major.mean(a)))

print("\n***STDV***")
print("stdv(a) = {}".format(major.stdv(a)))

print("\n****CONSTANTS****\n")

print("\n***PI***")
print("pi() = {}".format(const.pi()))


print("\n***Euler's number***")
print("e() = {}".format(const.e()))

print("\n***180***")
print("one80() = {}".format(const.one80()))


