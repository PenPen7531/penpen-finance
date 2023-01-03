from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter
from flask import request, render_template, redirect, session, Flask
import datetime
import matplotlib.pyplot as plt
import numpy as np


wb = load_workbook('finances.xlsx')

ws = wb.active


def append_data(type, cost):
    date=datetime.datetime.now()
    
    ws.append([str(type), str(cost), date.strftime("%B %d, %Y")])
    wb.save('finances.xlsx')

def show_data():
    wb = load_workbook('finances.xlsx')
    ws = wb.active
   
    food = 0
    videogames = 0
    computer = 0
    other = 0
    savings = 0
    data=[]
    for row in ws.values:


        row_data={}
        row_data["type"] = row[0]
        row_data["cost"] = row[1]
        row_data["date"] = row[2]
        if row[0] == 'Food':
            food += int(row[1])
        if row[0] == 'Videogames':
            videogames += int(row[1])
        if row[0] == 'Computer':
            computer += int(row[1])
        if row[0] == 'Other':
            other += int(row[1])
        if row[0] == 'Saving':
            savings += int(row[1])
        

        data.append(row_data)
    costs=[]
    mylabels=[]
    
    if food > 0:
        costs.append(food)
        mylabels.append("Food")
    
    if videogames > 0:
        costs.append(videogames)
        mylabels.append("Videogames")
    
    if computer > 0:
        costs.append(computer)
        mylabels.append("Computer")

    if other > 0:
        costs.append(other)
        mylabels.append("Other")

    if savings > 0:
        costs.append(savings)
        mylabels.append("Savings")

    plt.switch_backend('agg')
    plt.pie(costs, labels=mylabels, autopct=lambda p: '${:.2f}'.format(p * sum(costs) / 100))
    plt.legend(title = 'Costs')
    plt.savefig('static/img/piechart.png')
    return data

show_data()