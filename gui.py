# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 12:00:55 2015

@author: a.fajula
"""

from __future__ import division
from pylab import*
from Tkinter import*
import ttk

interactive(True)
close('all')


class MyGUI():
    
    def __init__(self, parent):
        
        self.myParent = parent
        #self.myParent.geometry("600x400")
        
        ### Our topmost frame is called myContainer1
        self.myContainer1 = Frame(parent, bg='tan') ###
        self.myContainer1.pack()
        
        #------ constants for controlling layout ------
        button_width = 6
        
        button_padx = '2m'
        button_pady = '1m'
        
        buttons_frame_padx = '3m'
        buttons_frame_pady = '2m'
        buttons_frame_ipadx = '3m'
        buttons_frame_ipady = '1m'
        
        background_color='tan'
        
        introduccio='Introdueix els valors desitjats per realitzar la consulta.\n\
        Els valors límit que ens poden introduir son:\n\
        data: 17/04/2005, magnitud:-3 i 6'
        # -------------- end constants ----------------
        
        # top frame
        self.top_frame = Frame(self.myContainer1,
                               height=350,
                               width=600,
                               bg=background_color)
        self.top_frame.pack(
            side=TOP,
            fill=BOTH,
            expand=YES,
            ipadx=buttons_frame_ipadx,
            ipady=buttons_frame_ipady,
            padx=buttons_frame_padx,
            pady=buttons_frame_pady
            )
            
        # mid frame
        self.mid_frame = Frame(self.myContainer1,
                               height=350,
                               width=600,
                               bg=background_color)
        self.mid_frame.pack(
            side=TOP,
            fill=BOTH,
            expand=YES,
            ipadx=buttons_frame_ipadx,
            ipady=buttons_frame_ipady,
            )
        #bottom frame
        
        self.bottom_frame = Frame(self.myContainer1,
                                  height=50,
                                  width=600,
                                  bg=background_color)
        self.bottom_frame.pack(
            side=TOP,
            fill=X,
            expand=YES
            )
            
        # buttons frame
        self.buttons_frame = Frame(self.bottom_frame,
                                  bg=background_color)
        self.buttons_frame.pack(
            side=RIGHT,
            fill=Y
            )
        
        #------------------   TEXT   ------------------------------------
        
        self.text=Label(self.top_frame, text=introduccio)
        self.text.configure(bg=background_color)
        self.text.pack(side=TOP, fill=X, anchor=CENTER)
        
        self.text_entries1 = Label(self.mid_frame)
        self.text_entries1.configure(text='Data minima',bg=background_color)
        self.text_entries1.grid(row=0, column=0, sticky=NW)
        #self.text_entries1.pack(side=LEFT)
        
        self.text_entries2 = Label(self.mid_frame)
        self.text_entries2.configure(text='Data maxima',bg=background_color)
        self.text_entries2.grid(row=1, column=0, sticky=SW)
        #self.text_entries2.pack(side=LEFT)
        
        self.text_entries3 = Label(self.mid_frame)
        self.text_entries3.configure(text='Magnitud minima',bg=background_color)
        self.text_entries3.grid(row=0, column=4, sticky=NE)
        #self.text_entries3.pack(side=LEFT)
        
        self.text_entries4 = Label(self.mid_frame)
        self.text_entries4.configure(text='Magnitud maxima',bg=background_color)
        self.text_entries4.grid(row=1, column=4, sticky=SE)
        #self.text_entries4.pack(side=LEFT)
        
        #------------------  ENTRIES  ------------------------------------
        
        self.entryVariable1 = StringVar()
        self.entry1 = Entry(self.mid_frame,textvariable=self.entryVariable1)
        #self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable1.set(u"2015")
        self.entry1.grid(row=0, column=1, sticky=W)
        #self.entry1.pack(side=LEFT)
        
        self.entryVariable2 = StringVar()
        self.entry2 = Entry(self.mid_frame,textvariable=self.entryVariable2)
        #self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable2.set(u"01")
        self.entry2.grid(row=0, column=2, sticky=W)
        #self.entry2.pack(side=LEFT)
        
        self.entryVariable3 = StringVar()
        self.entry3 = Entry(self.mid_frame,textvariable=self.entryVariable3)
        #self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable3.set(u"01")
        self.entry3.grid(row=0, column=3, sticky=W)
        #self.entry3.pack(side=LEFT)
        
        self.entryVariable4 = StringVar()
        self.entry4 = Entry(self.mid_frame,textvariable=self.entryVariable4)
        #self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable4.set(u"2015")
        self.entry4.grid(row=1, column=1, sticky=W)
        #self.entry4.pack(side=LEFT)
        
        self.entryVariable5 = StringVar()
        self.entry5 = Entry(self.mid_frame,textvariable=self.entryVariable5)
        #self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable5.set(u"12")
        self.entry5.grid(row=1, column=2, sticky=W)
        #self.entry5.pack(side=LEFT)
        
        self.entryVariable6 = StringVar()
        self.entry6 = Entry(self.mid_frame,textvariable=self.entryVariable6)
        #self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable6.set(u"31")
        self.entry6.grid(row=1, column=3, sticky=W)
        #self.entry6.pack(side=LEFT)
        
        self.entryVariable7 = StringVar()
        self.entry7 = Entry(self.mid_frame,textvariable=self.entryVariable7)
        #self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable7.set(u"-3")
        self.entry7.grid(row=0, column=5, sticky=E)
        #self.entry7.pack(side=LEFT)
        
        self.entryVariable8 = StringVar()
        self.entry8 = Entry(self.mid_frame,textvariable=self.entryVariable8)
        #self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable8.set(u"6")
        self.entry8.grid(row=1, column=5, sticky=E)
        #self.entry8.pack(side=LEFT)
        #------------------ BUTTON #1 ------------------------------------
        button_name='OK'
        # command binding
        self.button1 = Button(self.buttons_frame,
                              command=lambda
                              arg1=button_name, arg2=1, arg3='good Stuff!':
                              self.buttonHandler(arg1, arg2, arg3)
                              )
        # event binding -- passing the event as an argument
        self.button1.bind('<Return>',
                          lambda
                          event, arg1 = button_name, arg2 =1, arg3 ='Good Stuff!':
                          self.buttonHandler_a(event, arg1, arg2, arg3)
                          )
        self.button1.configure(text=button_name)
        self.button1.configure(
            width=button_width,
            padx=button_padx,
            pady=button_pady
            )
        self.button1.pack(side=LEFT, padx=button_padx, pady=button_pady)
        self.button1.focus_force()
        #self.button1.bind('<Button-1>', self.button1Click)
        
        #------------------ BUTTON #2 ------------------------------------
        button_name='Cancel'
        
        # command binding
        self.button2 = Button(self.buttons_frame,
                              command=lambda
                              arg1=button_name, arg2=2, arg3="Bad  stuff!":
                              self.buttonHandler(arg1, arg2, arg3)
                              )
        # event binding -- without passing the event as an argument
        self.button2.bind('<Return>', 
                          lambda
                          event, arg1=button_name, arg2=2, arg3="Bad  stuff!" :
                          self.buttonHandler_a(event, arg1, arg2, arg3)
                          )
        self.button2.configure(text=button_name)
        self.button2.configure(
            width=button_width,  ### (1)
            padx=button_padx,    ### (2)
            pady=button_pady     ### (2)
            )
        self.button2.pack(side=LEFT, padx=button_padx, pady=button_pady)
    
    def buttonHandler(self, argument1, argument2, argument3):
        '''print "    buttonHandler routine received arguments:" \
            , argument1.ljust(8), argument2, argument3'''
        if argument2==2:
            self.entries='exit'
            self.myParent.destroy()
        else:
            print '\t'+self.entryVariable1.get()+'\t'+self.entryVariable2.get()+'\t'+self.entryVariable3.get()+'\n'
            print '\t'+self.entryVariable4.get()+'\t'+self.entryVariable5.get()+'\t'+self.entryVariable6.get()+'\n'
            print '\t'+self.entryVariable7.get()+'\t'+self.entryVariable8.get()+'\n'
            
            self.entries=[
                int(self.entryVariable1.get()),
                int(self.entryVariable2.get()),
                int(self.entryVariable3.get()),
                int(self.entryVariable4.get()),
                int(self.entryVariable5.get()),
                int(self.entryVariable6.get()),
                int(self.entryVariable7.get()),
                int(self.entryVariable8.get())
                ]
            self.myParent.destroy()
    
    def buttonHandler_a(self, event, arg1, arg2, arg3):
        '''print "buttonHandler_a received event", event'''
        self.buttonHandler(arg1, arg2, arg3)
