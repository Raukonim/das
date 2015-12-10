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
    interactive(False)
    figure()
    magnituds1=[row for row in llista1 if row!=nan]
    magnituds2=[row for row in llista2 if row!=nan]
    histogram1=hist(magnituds1, bins=rangs)
    histogram2=hist(magnituds2, bins=rangs)
    
    n_groups=rangs.size-1
    tics=[]
    for i in range(n_groups):
        tics.append('['+str(rangs[i])+','+str(rangs[i+1])+')')
    index=arange(n_groups)
    bar_width=0.35
    opacity=0.4
    interactive(True)
    fig, ax1=subplots()
    title('Nombre de sismes i % deteccio (LOCAL)')
    bar(index,histogram1[0], bar_width, alpha=opacity,color='b',label='Manual' )
    bar(index+bar_width,histogram2[0], bar_width, alpha=opacity,color='r',label='Automatic' )
    ax1.set_xlabel('Valor del rang de Magnitud Manual (min/max no inclos')
    ax1.set_ylabel('Freq')
    
    legend()
    
    xticks(index+bar_width, tics[:])
    
    ax2 = ax1.twinx()
    a1=array(histogram1[0][:],dtype=int)
    a2=array(histogram2[0][:],dtype=int)
    b=a1-a2
    with errstate(divide='ignore', invalid='ignore'):
        x=100*(1-(b/a1))
        x[x == inf]=0
        x=nan_to_num(x)
        
    ax2.plot(x)
    show()
    
