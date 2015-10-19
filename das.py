# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 15:12:51 2015

@author: a.fajula
"""

from pylab import*
import csv
from datetime import datetime
#from astropy.io import ascii
#from astropy.table import Table


class esdeveniment:
    
    def __init__(self, event):
        self.code=event[0]
        self.date=datetime.strptime(event[1],'%d/%m/%Y')
        self.time=datetime.strptime(event[2],'%H:%M:%S.%f')
        self.date=self.date.replace(hour=self.time.hour, 
                                    minute=self.time.minute, second=self.time.second, 
                                    microsecond=self.time.microsecond)
        self.lat=float(event[3])
        self.lon=float(event[4])
        '''print self.lon
        if self.lon[-1]=='W':
            self.lon=float(event[4][:-2])*-1
        else:
            self.lon=float(event[4][:-2])'''
        self.prof=int(event[5])
        self.mag=float(event[6])



#t = Table.read('manual.csv', format='csv'''', dtype=('S8','S10','S11','f5','f5','i2','f4')''')
'''
t = ascii.read('manual.csv', delimiter=',')
esdeveniments=zeros(len(t))
for i in range(len(t)):
    esdeveniments[i]=esdeveniment_manual(t[i])'''

#a=esdeveniment(['l1510962','13/10/2015','20:11:42.10','42.55 N','1.96 E','8','2.0'])
eventlist=[]
with open('manual.csv') as csvfile:
    eventreader = csv.reader(csvfile)
    eventlist=[esdeveniment(row) for row in eventreader]
    

