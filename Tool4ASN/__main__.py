#####################################################################
#Programm author: Carmelo Sammarco
#####################################################################

#< Tool4ASN - Software to compute cross correlations with different stacking methodologies. >
#Copyright (C) <2020>  <Carmelo Sammarco - sammarcocarmelo@gmail.com>

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.
###################################################################

#########################
# IMPORT MODULES NEEDED #
#########################
import pkg_resources

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from tkinter import scrolledtext

import os
import json

def main(args=None):
    
    window = Tk()
    window.title("Tool4ASN")
    #window.geometry('500x600')

    def inputfile1():
        inputfile1.file = filedialog.askopenfilename() 

    def inputfile2():
        inputfile2.file = filedialog.askopenfilename()

    def inputdir():
        inputdir.dir = filedialog.askdirectory()





    def ASN():
        ################
        #LOGINs
        ###############
        filejason =  pkg_resources.resource_filename('Tool4ASN', 'SRC/Users_Database.json')

        Usr = StringVar()
        Pass = StringVar()

        Utente = ["Carmelo_Sammarco"]

        Database = {}
        with open (filejason, "r") as login_file:
            Database = json.load(login_file)
            for Utente in Database.keys(): 
                print(Utente)
                    
                listdic = Database.get(Utente) 
                print(listdic)

                Usr= listdic[0] 
                Pass = listdic[1]

                print (Usr)  
                print (Pass)  

        #########################



        outpath = str(os.getcwd())

        path0 = os.path.join(outpath, "Results")

        if not os.path.exists(path0):
            os.mkdir(path0) 
        
        print (inputfile1.file)
        print (inputfile2.file)



    #######################
    #GUI interface
    #######################
   
    Username = Label(window, text="Username")
    Username.grid(column=0, row=0)
    User = Entry(window, width=13)
    User.grid(column=0, row=1)
    ##
    Password = Label(window, text="Password")
    Password.grid(column=1, row=0)
    Pwd = Entry(window, width=13, show="*")
    Pwd.grid(column=1, row=1)
    ##
    space = Label(window, text="")
    space.grid(column=0, row=2)
    space = Label(window, text="")
    space.grid(column=1, row=2)
    ##
    Input1 = Button(window, text="Station-1", bg="yellow", command=inputfile1)
    Input1.grid(column=0, row=3)
    ##
    Input2 = Button(window, text="Station-2", bg="yellow", command=inputfile2)
    Input2.grid(column=1, row=3)
    ##
    space = Label(window, text="")
    space.grid(column=0, row=4)
    space = Label(window, text="")
    space.grid(column=1, row=4)
    ##
    btn1 = Button(window, text="START", bg="red", command=ASN)
    btn1.grid(column=0, row=5)
    

    #################################################################

    window.mainloop()

