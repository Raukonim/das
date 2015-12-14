# -*- coding: utf-8 -*-
"""
Created on Fri Dec 04 15:01:15 2015

@author: a.fajula
"""

#from __future__ import division
from pylab import*
from Tkinter import*
import time as tm
from datetime import datetime, timedelta
import csv
import sismes as sis
import plotter
import gui


start_time = tm.time()

interactive(True)
close('all')

def consulta(llista, element, minim, maxim):
        if element=='magnitud':
            seleccio=[row for row in llista if (row.magnitud>=minim and row.magnitud<=maxim)]
        elif element=='data':
            seleccio=[row for row in llista if (row.data>=minim and row.data<maxim+timedelta(days=1))]
        return seleccio

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

automatic_clean=[row for row in automatic_list if str(row.codi)!='nan']
automatic_hist=[]

data_min=datetime(2005,04,17)
data_max=datetime.today()
mag_min=-3
mag_max=6

#print '\n'*100
#print 'Starting...'    
root = Tk()
mygui=gui.MyGUI(root)
#print "Ready to start executing the event loop."
root.mainloop()
#print mygui.entries

boundary=mygui.entries
try:
    any_min=int(boundary[0])
    mes_min=int(boundary[1])
    dia_min=int(boundary[2])
    any_max=int(boundary[3])
    mes_max=int(boundary[4])
    dia_max=int(boundary[5])
    mag_min=float(boundary[6])
    mag_max=float(boundary[7])
    data_min=datetime(any_min,mes_min,dia_min)
    data_max=datetime(any_max,mes_max,dia_max)
except ValueError:
    print('Nombre invalid') 

manualxdata=consulta(manual_list, 'data', data_min, data_max)
manual_selection=consulta(manualxdata, 'magnitud', mag_min, mag_max)

automaticxdata=consulta(automatic_clean, 'data',data_min,data_max)
automatic_selection=consulta(automaticxdata, 'magnitud', mag_min, mag_max)

manual_mags=[row.magnitud for row in manual_selection if row.magnitud!=nan]
auto_mags=[row.magnitud for row in manual_selection if row.coincideix==True]

bins1=array([-3,0.5,1,1.5,2,2.5,3,3.5,4,4.5])
bins2=array([-3,0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1.1,1.2,1.3,1.4,1.5,1.6,1.7,
       1.8,1.9,2,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3,3.5,4,4.5,5,5.5])
bins3=array([-3,1.7,2,2.4,5.5])
plotter.histograma(manual_mags,auto_mags, bins1)
plotter.histograma(manual_mags,auto_mags, bins2)
plotter.histograma(manual_mags,auto_mags, bins3)

time=tm.time()-start_time
print ("runing time ="+str(time))