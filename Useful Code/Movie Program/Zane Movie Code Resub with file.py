# Programmed by Zane Imran
#NSN : 125645168
# Code Version 13
# 6/9/16

# This code is designed for a ticket selling program which allows
# a user to enter the number of tickets for a movie and purchase them.
# It uses a GUI interface to interact with the user and is reset each time
# the program is run.

import tkinter as tk
import tkinter.messagebox
from tkinter import PhotoImage
import linecache 

FDseatsLeft = 50
GBseatsLeft = 50
JBseatsLeft = 50

class mainApp:
    def __init__(self, master): #Creates Homescreen page
        #self.master = master
        root.title("Movie Ticket Sales")
        root.geometry('320x185+800+400')

        logo = PhotoImage(file="gif4.gif")
        logoLab = tk.Label(root, image=logo)
        logoLab.image = logo
        logoLab.grid(row=3, column=3, rowspan=4)

        options = ["Ghostbusters","Jason Bourne","Finding Dory"]

        self.labTitle= tk.Label(root,bg="blue",fg="white",text="          WELCOME            ",font=("comicsans","20","italic"))
        self.labTitle.grid(row=0,columnspan=20)
        self.labelAdult = tk.Label(text="ADULT:").grid(row=1)
        self.entryAdult = tk.Spinbox(root,from_=0, to=50)
        self.entryAdult.grid(row=1, column=1)

        self.labelChild = tk.Label(text="CHILD:").grid(row=2)
        self.entryChild = tk.Spinbox(root,from_=0, to=50)
        self.entryChild.grid(row=2, column=1)

        self.labelStudent = tk.Label(text="STUDENT:").grid(row=3)
        self.entryStudent = tk.Spinbox(root,from_=0, to=50)
        self.entryStudent.grid(row=3, column=1)

        self.labelSenior = tk.Label(text="SENIOR:").grid(row=4)
        self.entrySenior = tk.Spinbox(root,from_=0, to=50)
        self.entrySenior.grid(row=4, column=1)

        self.var1 = tk.StringVar(root)
        self.var1.set("Select A Movie")
        self.dropMenu = tk.OptionMenu(root,self.var1,*options).grid(row=1,column=3)

        self.sumSheet = tk.Button(root, text="View Summary Sheet", command = self.page2).grid(row=5,column=1)

    def page2(self): #Creates Summary Seat Page
        global window
        window = tk.Tk()
        window.title("Summary")
        window.geometry('320x185+800+400')

        self.getEntry()
        self.movieName = tk.Label(window,text=e).grid(row=0,column=0)

        self.labelaa = tk.Label(window,text=" Adult Tickets :").grid(row=1,column=0, sticky = 'W')
        self.labela = tk.Label(window, text=a)
        self.labela.grid(row=1, column =1, sticky = 'W')

        self.labelbb = tk.Label(window,text=" Child Tickets :").grid(row=2,column=0, sticky = 'W')
        self.labelb = tk.Label(window, text=b)
        self.labelb.grid(row=2, column =1, sticky = 'W')

        self.labelcc = tk.Label(window,text=" Student Tickets :").grid(row=3,column=0, sticky = 'W')
        self.labelc = tk.Label(window, text=c)
        self.labelc.grid(row=3, column =1, sticky = 'W')

        self.labeldd = tk.Label(window,text=" Senior Tickets :").grid(row=4,column=0, sticky = 'W')
        self.labeld = tk.Label(window, text=d)
        self.labeld.grid(row=4, column =1, sticky = 'W')

        self.movieDisplay = tk.Label(window, text=" MOVIES AND SEATS ",bg="blue",fg="white").grid(row=1, column=3,columnspan=2)

        self.fill = tk.Label(window, text="").grid(row=0, column=2)
        self.movie1 = tk.Label(window, text=" Ghostbusters :").grid(row=2,column=3, sticky = 'W' )
        self.movie2 = tk.Label(window, text=" Jason Bourne :").grid(row=3,column=3, sticky = 'W')
        self.movie3 = tk.Label(window, text=" Finding Dory :").grid(row=4,column=3, sticky = 'W')

        self.movie1Seat = tk.Label(window, text=GBseatsLeft).grid(row=2,column=4, sticky = 'W')
        self.movie2Seat = tk.Label(window, text=JBseatsLeft).grid(row=3,column=4, sticky = 'W')
        self.movie3Seat = tk.Label(window, text=FDseatsLeft).grid(row=4,column=4, sticky = 'W')

        self.cost = tk.Label(window, text="Total Cost is :      $").grid(row=4,column=0, sticky = 'W')
        self.costLab = tk.Label(window, text=str("{:.2f}".format(totalCost))).grid(row=4,column=1, sticky = "W")

        self.checkOut = tk.Button(window, text="Confirm Purchase", command=self.checkout, activebackground = "blue").grid(row=5,column=0,columnspan=2 )
        self.goBack = tk.Button(window, text="Back",command=self.resetSeats).grid(row=5,column=2,columnspan=2)

        self.reset = tk.Button(window, text="Reset Seats", command=self.resetFile).grid(row=5, column=4)

    def close_window(self): # Closes window and clears inputs
        window.destroy()

    def resetSeats(self): # Resets number of seats if order cancelled
        if e == "Finding Dory":
            global FDseatsLeft
            FDseatsLeft = FDseatsLeft + totalSeats
        if e == "Jason Bourne":
            global JBseatsLeft
            JBseatsLeft = JBseatsLeft + totalSeats
        if e == "Ghostbusters":
            global GBseatsLeft
            GBseatsLeft = GBseatsLeft + totalSeats
        self.close_window()

    def resetSeatsError(self): # Resets number of seats without closing window
        if e == "Finding Dory":
            global FDseatsLeft
            FDseatsLeft = FDseatsLeft + totalSeats
        if e == "Jason Bourne":
            global JBseatsLeft
            JBseatsLeft = JBseatsLeft + totalSeats
        if e == "Ghostbusters":
            global GBseatsLeft
            GBseatsLeft = GBseatsLeft + totalSeats
   
    def getEntry(self): # Gets entries from Spinbox
        self.adultEntry()
        self.childEntry()
        self.studentEntry()
        self.seniorEntry()
        self.movieEntry()
        
    def adultEntry(self): #Gets adult entry
        global a
        try:
            a = int(self.entryAdult.get() or "0")
            if a<0:
                self.inputError()
        except ValueError:
            self.inputError()
            print("Error")
            a=0
    def childEntry(self): #Gets child entry
        global b
        try:
            b = int(self.entryChild.get() or "0")
            if b<0:
                self.inputError()
        except ValueError:
            self.inputError()
            print("Error")
            b=0
    def studentEntry(self):#Gets student entry
        global c
        try:
            c = int(self.entryStudent.get() or "0")
            if c<0:
                self.inputError()
        except ValueError:
            self.inputError()
            print("Error")
            c=0
    def seniorEntry(self): #Gets senior entry
        global d
        try:
            d = int(self.entrySenior.get() or "0")
            if d<0:
                self.inputError()
        except ValueError:
            self.inputError()
            print("Error")
            d=0
    def movieEntry(self): #Gets movie name
        global e
        try:
            e = self.var1.get()
        except ValueError:
            e = "Select A Movie"   
        if e == "Select A Movie":
            e = "No Movie"
        self.calculate()

    def inputError(self): # Creats Input error pop-up screen
        error = "Invalid Input"
        self.errorMessage(error)
        
    def errorMessage(self,error): # General Error Screen Funciton
        tkinter.messagebox.showinfo("Error", error)  

    def movieSeats(self): # Calculates the number of seats left for each movie
        global FDseatsLeft, JBseatsLeft, GBseatsLeft
        if e == "Finding Dory":
            FDseatsLeft = FDseatsLeft - totalSeats
            if FDseatsLeft < 0:
                self.seatError()   
        if e == "Jason Bourne":
            JBseatsLeft = JBseatsLeft - totalSeats
            if JBseatsLeft < 0:
                self.seatError()          
        if e == "Ghostbusters":
            GBseatsLeft = GBseatsLeft - totalSeats
            if GBseatsLeft < 0:
                self.seatError()           

    def seatError(self): # Error if no seats left
        error = "No Seats Left"
        self.errorMessage(error)
        self.resetSeatsError()
        
    def calculate(self): # Calculates total number of seats
        global totalSeats
        totalSeats = a + b + c + d
        self.movieSeats()
        self.getCost()

    def resetFile(self):
        global FDseatsLeft, JBseatsLeft, GBseatsLeft
        FDseatsLeft = 50
        JBseatsLeft = 50
        GBseatsLeft = 50
        self.resetSeats()
        self.writeFile()
	
    def writeFile(self):
        global FDseatsLeft, JBseatsLeft, GBseatsLeft
        summaryFile = open("summary.txt", "w+")
        summaryFile.write(str(FDseatsLeft) + '\n')
        summaryFile.write(str(JBseatsLeft) + '\n')
        summaryFile.write(str(GBseatsLeft) + '\n')
          
    def checkout(self): # Finalises user input and appends data to list
        global numberSeats, details
        if e == "No Movie":
            self.close_window()
            error = "Please Select Movie"
            self.errorMessage(error)
            return
        if totalSeats == 0:
            self.close_window()
            error = "No Seats Selected"
            self.errorMessage(error)
            return
        details = []
        details.append(e)
        details.append(totalSeats)
        details.append(totalCost)
        print("Your Order has been processed")
        print(details)
        self.writeFile()
        self.close_window()
        self.entryAdult.delete(0,tk.END)
        self.entryChild.delete(0,tk.END)
        self.entryStudent.delete(0,tk.END)
        self.entrySenior.delete(0,tk.END)

    def getCost(self): # Calculates cost of tickets
        global totalCost
        totalCost = 18*a + 12.5*b + 16*c + 12.5*d

#Read in seat left values
        
FDseatsLeft = linecache.getline("summary.txt",1)
JBseatsLeft = linecache.getline("summary.txt",2)
GBseatsLeft = linecache.getline("summary.txt",3)
FDseatsLeft = int(FDseatsLeft)
JBseatsLeft = int(JBseatsLeft)
GBseatsLeft = int(GBseatsLeft)
print("Finding Dory Initial Seats left : ", FDseatsLeft)
print("Jason Bourne Initial Seats left : ", JBseatsLeft)
print("Ghostbusters Initial Seats left : ", GBseatsLeft)

root = tk.Tk()
app = mainApp(root)
root.mainloop()

