#!/usr/bin/env python

import csv

with open("matrix.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=",")
    for row in readCSV:
        print(row)
