# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 13:54:59 2015

@author: a.fajula
"""

from __future__ import division, print_function
from pylab import*
from datetime import datetime, time


class esdeveniment(object):
    
    def __init__ (self, event):
        self.codi=event[0]
        if event[1]=='nan':
            self.data='nan'
        else:
            date=datetime.strptime(event[1],'%d/%m/%Y')
            temps1=str(event[2])[:5]
            h=int(str(temps1[0:2]))
            m=int(str(temps1[3:5]))
            temps2=str(event[2])[6:]
            s=int(float(temps2))
            ms=int("{0:.2f}".format(float(temps2))[3:])*10000
            temps=time(h, m, s, ms)
            self.data=datetime.combine(date, temps)
        if isnan(float(event[5])):
            self.prof=float(event[5])
        else:
            self.prof=event[5]
        self.magnitud=float(event[6])
        
class esdeveniment_manual(esdeveniment):
    
    def __init__(self,event):
        try:
            esdeveniment.__init__(self, event)
            self.latitud=float(event[3])
            self.longitud=float(event[4])
            self.comarca=event[7]
            self.compara=str(self.codi)[1:]
        except ValueError:
            pass
    
    def __repr__(self):
        return '%s  %s %s %s %s %s %s' % (
            self.codi, str(self.data)[:-4], str(self.latitud), str(self.longitud), 
            str(self.prof), str(self.magnitud), self.comarca)
            
class esdeveniment_automatic(esdeveniment):
    
    def __init__(self,event):
        try:
            esdeveniment.__init__(self, event)
            if isnan(float(event[0])):
                self.codi=float(event[0])
            else:
                self.codi=event[0]
            self.latitud=float(event[3])
            self.longitud=float(event[4])
            self.rms=float(event[7])
            if event[8]=='nan':
                self.mindist=float(event[8])
            else:
                self.mindist=int(event[8])
            if isnan(float(event[9])):
                self.gap=float(event[9])
            else:
                self.gap=int(event[9])
            if isnan(float(event[10])):
                self.numfases_loc=float(event[10])
            else:
                self.numfases_loc=int(event[10])
            if isnan(float(event[11])):
                self.nummags=float(event[11])
            else:
                self.nummags=int(event[11])
            self.desvest=float(event[12])
            if isnan(float(event[13])):
                self.codibd=float(event[13])
            else:
                self.codibd=event[13]
            if isnan(float(event[14])):
                self.numfases_lec=float(event[14])
            else:
                self.numfases_lec=int(event[14])
            self.eix_max=float(event[15])
            if isnan(float(event[16])):
                self.azm_max=float(event[16])
            else:
                self.azm_max=int(event[16])
            if isnan(float(event[17])):
                self.inc_max=float(event[17])
            else:
                self.inc_max=int(event[17])
            self.eix_mig=float(event[18])
            if isnan(float(event[19])):
                self.azm_mig=float(event[19])
            else:
                self.azm_mig=int(event[19])
            if isnan(float(event[20])):
                self.inc_mig=float(event[20])
            else:
                self.inc_mig=int(event[20])
            self.eix_min=float(event[21])
            if isnan(float(event[22])):
                self.azm_min=float(event[22])
            else:
                self.azm_min=int(event[22])
            if isnan(float(event[23])):
                self.inc_min=float(event[23])
            else:
                self.inc_min=int(event[23])
            if self.data=='nan':
                self.data=nan
                self.compara=nan
            else:
                self.compara=str(self.data.year)[2:]+str(self.data.month)+str(self.codibd)[2:]
        except ValueError:
            pass
    
    def __repr__(self):
        return '%s %s %s %s  %s %s %s %s  %s %s %s %s  %s %s %s %s  %s %s %s %s  %s %s %s' % (
            self.codi, str(self.data)[:-4], str(self.latitud), str(self.longitud), 
            str(self.prof), str(self.magnitud), str(self.rms), str(self.mindist),
            str(self.gap), str(self.numfases_loc), str(self.nummags), 
            str(self.desvest), str(self.codibd), str(self.numfases_lec), 
            str(self.eix_max), str(self.azm_max), str(self.inc_max), 
            str(self.eix_mig), str(self.azm_mig), str(self.inc_mig), 
            str(self.eix_min), str(self.azm_min), str(self.inc_min))
