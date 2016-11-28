from tkinter import *

root = Tk()
root.geometry('450x450+200+200')
root.title("Salary Calculator")

hourlyRate=14.75
hours=StringVar()

def calcIncome():
    global hourlyRate, labmyIncome
    hoursWorked=hours.get()
    myIncome=(float(hoursWorked)*hourlyRate)
    labmyIncome['text']=myIncome
    
    
def finish():
    root.destroy()

labTitle= Label(root,bg="green",fg="white",text="SJC Salary Calculator",font=("comicsans","20","italic"))
labTitle.pack(fill=X)

labHoursWorked=Label(root,text="Enter the hours worked this week")
labHoursWorked.pack()
hours=Entry(root,textvariable=labHoursWorked)
hours.pack()

buttonQuit=Button(root,text="Quit",command=finish)
buttonQuit.pack()

buttonCalcIncome=Button(root,text="Calculate Income",command=calcIncome)
buttonCalcIncome.pack()

labmyIncome=Label(root,text="This weeks income : ")
labmyIncome.pack()

root.mainloop()

