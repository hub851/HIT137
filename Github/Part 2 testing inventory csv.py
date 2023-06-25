from tkinter import *
import csv
import datetime

def enter_button():
    now = datetime.datetime.now()
    SKU = e1.get()
    Description = e2.get()
    BIN = e3.get()
    Location = e4.get()
    QTY = e5.get()
    with open('File.csv', 'a') as f:
        w = csv.writer(f,dialect='excel-tab')
        w.writerow([now.strftime("%Y-%m-%d %H:%M"), SKU, Description, BIN, Location, QTY]) #need to separate this by cols
    #for row in w:
        #output.append(row.split(','))


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
myButton=Button(window,text='Enter',command=enter_button)
e1.grid(row=0,column=1)
myButton.grid(row=5,column=0)

mainloop()
