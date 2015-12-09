# -*- coding: utf-8 -*-
"""
Created on Wed Dec 09 12:49:23 2015

@author: a.fajula
"""

from __future__ import division
from pylab import*

interactive(True)
close('all')

def histograma(llista1, llista2, rangs):
    figure()
    magnituds1=[row.magnitud for row in llista1 if row.magnitud!=nan]
    magnituds2=[row.magnitud for row in llista2 if row.magnitud!=nan]
    histogram=hist([magnituds1, magnituds2], bins=rangs)
    '''a1=histogram[0][0]
    a2=histogram[0][1]
    b=a1-a2
    x=100*(1-(b/a1))
    plot(x)'''
    return histogram
