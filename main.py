# -*- coding: utf-8 -*-
"""
Created on Fri Dec 04 15:01:15 2015

@author: a.fajula
"""

from __future__ import division
from pylab import*
import time as tm
from datetime import datetime, timedelta
import csv
import sismes as sis


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

data_min=datetime(2005,04,16)
data_max=datetime.today()
mag_min=-3
mag_max=6
print('Introdueix els valors desitjats per realitzar la consulta.')
print('Els valors per defecte son data:[16/04/2005,avui], magnitud:[-3,6]')
sel_params=raw_input('vols modificar aquests parametres?[y/N]\n')
if sel_params=='y':
    print('Si desitges modificar aquestes dades has introdueix-els seguint aquest exemple:')
    print('[2005,04,17,2015,12,31,-2,5]')
#boundary=[8]
    lectura=raw_input('introdueix els parametres desitjats:\n')
    boundary=lectura.split()
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
else:
    pass

manualxdata=consulta(manual_list, 'data', data_min, data_max)
manual_selection=consulta(manualxdata, 'magnitud', mag_min, mag_max)

time=tm.time()-start_time
print ("runing time ="+str(time))