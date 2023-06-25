from tkinter import *
#tkinter is being used to create the GUI for this application
import csv
#the output will be in csv format for ease of use by the end user.
#I was trying to use a xlsx format, however could not identify the
#correct code to create a suitable output.
import datetime
#used to add the output for the current date and time to "timestamp" the output
#This is so that the user can identify when the inputs were entered.

def enter_button():
    now = datetime.datetime.now()
    SKU = e1.get()
    Description = e2.get()
    BIN = e3.get()
    Location = e4.get()
    QTY = e5.get()
    with open('File.csv', 'w') as f:
        w = csv.writer(f,dialect='excel-tab')
        header_columns = (['Date/Time', 'SKU', "Description", "BIN", "Location", "QTY"])
        writer = csv.DictWriter(f, header_columns, delimiter=',', quoting = csv.QUOTE_ALL)
        #w.writeheader()
        w.writerow(["Date/Time", "SKU", "Description", "BIN", "Location", "QTY"])
        w.writerow([now.strftime("%Y-%m-%d %H:%M"),
        SKU, Description, BIN, Location, QTY])
window=Tk()
window.title("Inventory Input")

Label(window, text='SKU').grid(row=0)
e1 = Entry(window)
e1.grid(column=1, row=0)
Label(window, text='Description').grid(row=1)
e2 = Entry(window)
e2.grid(column=1, row=1)
Label(window, text='BIN #').grid(row=2)
e3 = Entry(window)
e3.grid(column=1, row=2)
Label(window, text='Location').grid(row=3)
e4 = Entry(window)
e4.grid(column=1, row=3)
Label(window, text='QTY').grid(row=4)
e5 = Entry(window)
e5.grid(column=1, row=4)
enter=Button(window,text='Enter',command=enter_button)
e1.grid(row=0,column=1)
enter.grid(row=5,column=0)
def close_window ():
    window.destroy()
cancel=Button(window,text='Cancel',command=close_window)
e1.grid(row=0,column=1)
cancel.grid(row=5,column=2)
mainloop()
