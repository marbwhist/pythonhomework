
import os
import csv
import numpy as np
import string



PyBank_csv = os.path.join("PyBank.csv")




with open(PyBank_csv) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=" ")

    month=list(zip(*reader))[1]
    
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    
    
