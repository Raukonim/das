# -*- coding: utf-8 -*-
"""
Created on Wed Dec 09 12:49:23 2015

@author: a.fajula
"""

from __future__ import division
from pylab import*

interactive(True)
close('all')


def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        text(rect.get_x() + rect.get_width()/2., 1+height,
                '%d' % int(height),
                ha='center', va='bottom')

def histograma(llista1, llista2, rangs):
    
    magnituds1=[row for row in llista1 if row!=nan]
    magnituds2=[row for row in llista2 if row!=nan]
    histogram1, edges1=histogram(magnituds1, bins=rangs)
    histogram2, edges2=histogram(magnituds2, bins=rangs)
    
    n_groups=rangs.size-1
    tics=[]
    for i in range(n_groups):
        tics.append('['+str(rangs[i])+','+str(rangs[i+1])+')')
    index=arange(n_groups)
    bar_width=0.35
    opacity=0.4
    interactive(True)
    fig, ax=subplots()
    title('Nombre de sismes i % deteccio (LOCAL)')
    rects1=ax.bar(index,histogram1, bar_width, alpha=opacity,color='b',label='Manual' )
    rects2=ax.bar(index+bar_width,histogram2, bar_width, alpha=opacity,color='r',label='Automatic' )
    ax.set_xlabel('Valor del rang de Magnitud Manual (min/max no inclos')
    ax.set_ylabel('Freq')
    
    ax.legend()
    autolabel(rects1)
    autolabel(rects2)
    
    xticks(index+bar_width, tics[:])
    
    ax2 = ax.twinx()
    a1=array(histogram1[:],dtype=int)
    a2=array(histogram2[:],dtype=int)
    b=a1-a2
    with errstate(divide='ignore', invalid='ignore'):
        x=100*(1-(b/a1))
        x[x == inf]=0
        x=nan_to_num(x)
    
    ax2.plot(index+bar_width,x)
    for xy in zip(index,x):                                                # <--
        ax2.annotate('%s' % int(xy[1])+'%', xy=xy, xytext=(xy[0]+bar_width,xy[1]+0.5), textcoords='data') # <--
    ax2.set_ylim(0,120)
    show()
    
