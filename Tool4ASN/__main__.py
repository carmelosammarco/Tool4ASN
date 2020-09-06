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


def main(args=None):
    
    window = Tk()

    window.title("Tool4ASN-by_Carmelo_Sammarco")
    #window.geometry('500x600')

    def ASN():
        print ("Test")



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
    FTPlink = Label(window, text="FTP-URL")
    FTPlink.grid(column=0, row=3)
    FTPlk = Entry(window, width=13)
    FTPlk.grid(column=1, row=3)
    ##
    space = Label(window, text="")
    space.grid(column=1, row=4)
    ##
    Datest = Label(window, text="From(YYYY-MM-DD)")
    Datest.grid(column=0, row=6)
    Ds = Entry(window, width=13)
    Ds.grid(column=1, row=6)
    ##
    Daten = Label(window, text="To(YYYY-MM-DD)")
    Daten.grid(column=0, row=7)
    De = Entry(window, width=13)
    De.grid(column=1, row=7)
    ##
    space = Label(window, text="")
    space.grid(column=0, row=8)
    space = Label(window, text="")
    space.grid(column=1, row=8)
    ##
    boundingb = Label(window, text="Bounding-box?(YES/NO)")
    boundingb.grid(column=0, row=9)
    bb = Entry(window, width=13)
    bb.grid(column=1, row=9)
    ##
    longmin = Label(window, text="Long-min(W)")
    longmin.grid(column=0, row=10)
    lomin = Entry(window, width=8)
    lomin.grid(column=0, row=11)
    ##
    longmax = Label(window, text="Long-max(E)")
    longmax.grid(column=1, row=10)
    lomax = Entry(window, width=8)
    lomax.grid(column=1, row=11)
    ##
    latmin = Label(window, text="Lat-min(S)")
    latmin.grid(column=0, row=12)
    lamin = Entry(window, width=8)
    lamin.grid(column=0, row=13)
    ##
    latmax = Label(window, text="Lat-max(N)")
    latmax.grid(column=1, row=12)
    lamax = Entry(window, width=8)
    lamax.grid(column=1, row=13)
    ##
    space = Label(window, text="")
    space.grid(column=0, row=14)
    space = Label(window, text="")
    space.grid(column=1, row=14)
    ##
    Varex = Label(window, text="Variables?(YES/NO)")
    Varex.grid(column=0, row=15)
    Vex = Entry(window, width=13)
    Vex.grid(column=1, row=15)
    VexY = Label(window, text="Variables(var1,var2,...)")
    VexY.grid(column=0, row=16)
    Vexlist = Entry(window, width=13)
    Vexlist.grid(column=1, row=16)
    ##
    space = Label(window, text="")
    space.grid(column=0, row=17)
    space = Label(window, text="")
    space.grid(column=1, row=17)
    ##
    Depex = Label(window, text="Depths?(YES/NO | SINGLE/RANGE)")
    Depex.grid(column=0, row=18)
    Dex = Entry(window, width=13)
    Dex.grid(column=1, row=18)
    Dtype = Entry(window, width=13)
    Dtype.grid(column=2, row=18)
    ##
    Singledepth = Label(window, text="Single-depth")
    Singledepth.grid(column=0, row=19)
    sdepth = Entry(window, width=13)
    sdepth.grid(column=1, row=19)
    ##
    Rangedepth = Label(window, text="Range-depths(Min|Max)")
    Rangedepth.grid(column=0, row=20)
    Rdepthmin = Entry(window, width=13)
    Rdepthmin.grid(column=1, row=20)
    Rdepthmax = Entry(window, width=13)
    Rdepthmax.grid(column=2, row=20)
    ##
    space = Label(window, text="")
    space.grid(column=0, row=22)
    space = Label(window, text="")
    space.grid(column=1, row=22)
    ##
    
    btn1 = Button(window, text="Download", bg="red", command=ASN)
    btn1.grid(column=0, row=23)
    

    #################################################################

    window.mainloop()

