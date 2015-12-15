# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 10:12:13 2015

@author: a.fajula
"""

from __future__ import division
from pylab import*
import csv
import sismes as sis

interactive(True)
close('all')

class LoadFiles(object):
    
    def __init__(self, file1, file2):
        
        manual_file=open(file1, 'rb')
        manual_reader=csv.reader(manual_file, delimiter=',')
        manual_list=[]
        for row in manual_reader:
            manual_list.append(sis.esdeveniment_manual(asarray(row)))
        
        automatic_file=open(file2, 'rb')
        automatic_reader=csv.reader(automatic_file, delimiter=',')
        automatic_list=[]
        for row in automatic_reader:
            automatic_list.append(sis.esdeveniment_automatic(asarray(row)))
        
        self.file2_clean=[row for row in automatic_list if str(row.codi)!='nan']
        self.file1_list=manual_list
        self.file2_list=automatic_list
        
        