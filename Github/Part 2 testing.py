import PySimpleGUI as sg
import numpy as np
import pandas as pd
import csv
import tkinter as tk

#df = pd.write_csv('')

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Input inventory data')],
            [sg.Text('SKU'), sg.InputText()],
            [sg.Text('Description') , sg.InputText()],
            [sg.Text('BIN #'), sg.InputText()],
            [sg.Text('Location'), sg.InputText()],
            [sg.Text('QTY'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel'),sg.Button("Complete")]]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    #begin here for output code to write csv
    pd

#table layout for print


window.close()
