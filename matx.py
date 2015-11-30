# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 13:54:59 2015

@author: a.fajula
"""

from __future__ import division, print_function
from pylab import*
from datetime import datetime, time
import time as tm

start_time = tm.time()

interactive(True)
close('all')


class esdeveniment(object):
    
    def __init__ (self, event):
        self.codi=event[0]
        #data=date.strftime(event[1],'%d/%m/%Y')
        #temps=time.strftime(event[2],'%H:%M:%S.%f')
        date=datetime.strptime(event[1],'%d/%m/%Y')
        temps1=event[2]
        h=int(str(temps1[0])+str(temps1[1]))
        m=int(str(temps1[3])+str(temps1[4]))
        s=int(str(temps1[6])+str(temps1[7]))
        ms=int(str(temps1[9])+str(temps1[10]))*10000
        temps=time(h, m, s, ms)
        self.data=datetime.combine(date, temps)
        
        
class esdeveniment_manual(esdeveniment):
    
    def __init__(self,event):
        try:
            esdeveniment.__init__(self, event)
            self.compara=str(self.data.month)+str(self.codi[-3:])
        except ValueError:
            pass
    
    def __repr__(self):
        return '%s  %s %s' % (
            self.codi, self.data, self.compara)
            
class esdeveniment_automatic(esdeveniment):
    
    def __init__(self,event):
        try:
            esdeveniment.__init__(self, event)
            self.codibd=event[3]
            self.compara=str(self.data.month)+str(self.codibd[-3:])
        except ValueError:
            pass
    
    def __repr__(self):
        return '%s  %s %s %s' % (
            self.codi, self.data, self.codibd, self.compara)


manual=esdeveniment_manual(['l1510441', '31/10/2015', '20:18:01.10'])
automatic=esdeveniment_automatic(['13770', '31/10/2015', '20:18:02.80', '52441'])



time=tm.time()-start_time
print ("runing time ="+str(time))