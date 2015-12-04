# -*- coding: utf-8 -*-
"""
Created on Fri Dec 04 15:01:15 2015

@author: a.fajula
"""

from __future__ import division
from pylab import*
import time as tm
import csv
import sismes as sis


start_time = tm.time()

interactive(True)
close('all')

dt_manual=dtype([('codi', str),('data',str), ('TU',str),('latitud',str), 
                 ('longitud',str), ('prof',int), ('magnitud', float)])

manual_file=open('manual.csv', 'rb')
manual_reader=csv.reader(manual_file, delimiter=',')
manual_list=[]
for row in manual_reader:
    manual_list.append(sis.esdeveniment_manual(asarray(row)))

automatic_file=open('automatic.csv', 'rb')
automatic_reader=csv.reader(automatic_file, delimiter=',')
automatic_list=[]
for row in automatic_reader:
    automatic_list.append(sis.esdeveniment_automatic(asarray(row)))


time=tm.time()-start_time
print ("runing time ="+str(time))