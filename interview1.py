#!/usr/bin/python3

for row in range(0, 5):
    for col in range(0, row):
        print(row, end = "")
        row = row - 1
    print(" ")
