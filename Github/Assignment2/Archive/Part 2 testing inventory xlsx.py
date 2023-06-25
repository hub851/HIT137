from tkinter import *
import xlsxwriter
import datetime



def enter_button():
    now = datetime.datetime.now()
    SKU = e1.get()
    Description = e2.get()
    BIN = e3.get()
    Location = e4.get()
    QTY = e5.get()
    #with open('File.xlsx', 'a') as f: #this needs to be fixed to work with excel

workbook = xlsxwriter.Workbook('File.xlsx')
worksheet = workbook.add_worksheet()
row=0
column=0
for type, input in (enter_button): #needs to execute from enter button
    worksheet.write(row, col, type)
    worksheet.write(row, col + 1, input)
    row += 1

        #w = xlsx.writer(f,dialect='excel-tab')
        #w.writerow([now.strftime("%Y-%m-%d %H:%M"), SKU, Description, BIN, Location, QTY])

window=Tk()
window.title("Inventory Input")
window.geometry('300x170')

Label(window, text='SKU').grid(row=0)
e1 = Entry(window)
e1.grid(column=1, row=0, columnspan=4) #want to expand the column span columnspan func not working

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
myButton.grid(row=5,column=0)

mainloop()
