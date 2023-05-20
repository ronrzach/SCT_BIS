# import csv
from toCSV import spa_to_csv
from bis_visualize import plot_bis
from bis_visualize import bisVal_csv
# import matplotlib
# from matplotlib import pyplot as plt
# import numpy as np

import os

# print("Enter date in DD/MM/YYYY format and time in HH:MM:SS format \n")
# sDate = input("Enter start date: ")
# sTime = input("Enter start time: ")
# eDate = input("Enter end date: ")
# eTime = input("Enter end time: ")
# bis_thresh = float(input("Enter BIS threshold value: "))
# time_thresh = float(input("Enter Time threshold value: "))


# spa_file = input("Enter SPA file name, if available otherwise enter \"NA\": ")
# csv_file = input("Enter CSV file name, if available otherwise enter \"NA\": ")

# spa_file = ""
# csv_file = ""

sDate = "04/27/2018"
sTime = "12:36:00"
eDate = "04/28/2018"
eTime = "15:05:00"
bis_thresh = float(50)
time_thresh = float(5)

curr_folder = os.getcwd()




csv_file = curr_folder+"\\"+"tri_event_sample.csv"

def bisviz(sDate,sTime,eDate,eTime,bis_thresh, time_thresh,csv_file):
    event, x_arr, y_arr, e_start, e_end,time_array = bisVal_csv(sDate, sTime, eDate, eTime, bis_thresh, time_thresh, csv_file)
    plot_bis(event, x_arr, y_arr, e_start, e_end, bis_thresh, time_thresh,time_array)

    print("CSV: ", csv_file)\

bisviz(sDate,sTime,eDate,eTime,bis_thresh, time_thresh,csv_file)
