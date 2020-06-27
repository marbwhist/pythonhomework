import os
import csv
import numpy as np
import string



PyBank_csv = os.path.join("PyBank.csv")



months=len(open(PyBank_csv.readlines())
print(months)


with open(PyBank_csv) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    
