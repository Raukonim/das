# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 15:12:51 2015

@author: a.fajula
"""

from pylab import*
import csv
from datetime import datetime, timedelta
#from astropy.io import ascii
#from astropy.table import Table


class esdeveniment(object):
    
    def __init__(self, event):
        try:
            self.code=event[0]
            self.date=datetime.strptime(event[1],'%d/%m/%Y')
            self.time=datetime.strptime(event[2],'%H:%M:%S.%f')
            self.date=self.date.replace(hour=self.time.hour, 
                                        minute=self.time.minute, second=self.time.second, 
                                        microsecond=self.time.microsecond)
            self.lat=float(event[3])
            self.lon=float(event[4])
            self.prof=int(event[5])
            self.mag=float(event[6])
        except ValueError:
            pass
    
    def __repr__(self):
        return '%s  %s  %s  %s  %s  %s' % (
            self.code, self.date, self.lat, self.lon, self.prof, self.mag)

class esdeveniment_automatic(esdeveniment):
    
    def __init__(self,event):
        try:
            esdeveniment.__init__(self,event)
            self.rms=float(event[7])
            self.mindist=float(event[8])
            self.gap=float(event[9])
            self.numfases_loc=float(event[10])
            self.nummags=float(event[11])
            self.desvest=float(event[12])
            self.codibd=event[13]
            self.numfases_lec=float(event[14])
            self.eix_max=float(event[15])
            self.azm_max=float(event[16])
            self.inc_max=float(event[16])
            self.eix_mig=float(event[18])
            self.azm_mig=float(event[19])
            self.inc_mig=float(event[20])
            self.eix_min=float(event[21])
            self.azm_min=float(event[22])
            self.inc_min=float(event[23])
        except ValueError:
            pass
        
        '''def __repr__(self):
            return '%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s' % (
                self.code, self.date, self.lat, self.lon, self.prof, self.mag,                
                self.rms, self.mindist , self.gap, self.numfases, self.nummags,
                self.desvest, self.codibd, self.numfases_lec, self.eix_max,
                self.azm_max, self.inc_max, self.eix_mig, self.azm_mig,
                self.inc_mig, self.eix_min, self.azm_min, inc_min)'''

            
manuallist=[]
with open('manual.csv') as csvfile:
    eventreader = csv.reader(csvfile)
    manuallist=[esdeveniment(row) for row in eventreader]

autolist=[]
with open('automatic.csv') as csvfile:
    eventreader = csv.reader(csvfile)
    autolist=[esdeveniment_automatic(row) for row in eventreader]

selectedmanual=[]
selectedauto=[]
i=0
deltat=timedelta(seconds=20)
for manual in manuallist:
    for auto in autolist:
        #print manual.date
        #print auto.date
        if abs(manual.date-auto.date) <= deltat:
            selectedmanual.append(manual)
            selectedauto.append(auto)
            i+=1
print i