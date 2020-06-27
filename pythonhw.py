import os
import csv
import numpy as np
import string



PyBank_csv = os.path.join("PyBank.csv")

total_months= 0
total_profits=0
monthly_changes=list()
greatest_changes={
    "increase": 0,
    "increase_month" :"",
    "decrease" : 0,
    "decrease_month": "",
}


def update_changes(change, month, greatest_changes):
    if change > greatest_changes["increase"]:
        greatest_changes["increase"]=change
        greatest_changes["increase_month"]=month

    if change < greatest_changes["decrease"]:
        greatest_changes["decrease"]=change
        greatest_changes["decrease_month"]=month




with open(PyBank_csv) as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=',')
    csv_header= next(csv_file)
    print(f"Header: {csv_header}")
    last_profit=0
    
    for row in csv_reader:
        month=row[0]
        profit=int(row[1])
        total_months += 1
        total_profits+= profit
        if last_profit:
            change=profit-last_profit
            update_changes(profit,month, greatest_changes)
            monthly_changes.append(change)         
        last_profit=profit


    

average_changes=sum(monthly_changes)/len(monthly_changes)
greatest_increase=greatest_changes["increase"]
greatest_decrease=greatest_changes["decrease"]
greatest_increase_month=greatest_changes["increase_month"]
greatest_decrease_month=greatest_changes["decrease_month"]


print(f"total_months: {total_months}")
print(f"total_profits: $ {total_profits}")
print(f"Average Change: $ {average_changes}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")