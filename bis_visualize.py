import csv
# import toCSV
# import matplotlib
from matplotlib import pyplot as plt
import numpy as np



# print("Enter date in DD/MM/YYYY format and time in HH:MM:SS format \n")
# sDate = input("Enter start date: ")
# sTime = input("Enter start time: ")
# eDate = input("Enter end date: ")
# eTime = input("Enter end time: ")
# bis_thresh = float(input("Enter BIS threshold value: "))
# time_thresh = float(input("Enter Time threshold value: "))


# sDate = "04/27/2018"
# sTime = "12:36:00"
# eDate = "04/28/2018"
# eTime = "15:05:00"
# bis_thresh = float(50)
# time_thresh = float(5)


def bisVal_csv(sDate, sTime, eDate, eTime, bis_thresh, time_thresh, filename ="tri_event_sample.csv"):

    x_plot_counter = 0.0
    x_arr = []
    y_arr = []
    e_start = []
    e_end = []
    time_array = []

    with open(filename, "r", newline='') as csvf:
        csvR = csv.reader(csvf)
        flag = 5 #random number for initialization - actual values are 1 and 0
        counter = 0
        event = 0



        #'row' variable is used to get each row of records from CSV file using for loop
        for row in csvR:
            # print(row)
            if row == ['Time', 'AVGBIS']:
                continue


            # Using split() function we split the date and time which are both part of row[0] and store it in array 'rDT'
            # Note that this is done for each row
            rDT = row[0].split(" ")

            #rDT[0] and rDT[1] are used to access date and time respectively
            print(rDT[0], rDT[1])


            # Code to set value of flag to 1 if rDT[0] and rDT[1] are equal to start date and start time (i.e., sDate and sTime)
            if rDT[0].strip() == sDate.strip() and rDT[1].strip() == sTime.strip():
                # print(rDT)
                flag = 1

            # Code to set value of flag to 0 if rDT[0] and rDT[1] are equal to end date and end time (i.e., eDate and eTime)
            elif rDT[0].strip() == eDate.strip() and rDT[1].strip() == eTime.strip():
                # print(rDT)
                flag = 0

            # If
            if flag == 1:

                x_plot_counter = x_plot_counter + 1
                x_arr.append(x_plot_counter)
                y_arr.append(float(row[1]))
                time_array.append(rDT[1][:-3])

                # print(float(row[1]),"\n")

                if float(row[1]) < bis_thresh:
                    if counter == 0:
                        e_start.append(x_plot_counter)
                        print("E_START: ", e_start)
                        print("E_END: ", e_end)
                    counter = counter + 1

                elif float(row[1]) >= bis_thresh and counter < time_thresh:
                    if(len(e_start) != 0 and counter < time_thresh and len(e_start) == len(e_end) + 1):
                        e_start.pop()
                        print("E_START: ", e_start)
                        print("E_END: ", e_end)
                    elif(len(e_start) == 0 and len(e_end) == 0):
                        print("E_START: ", e_start)
                        print("E_END: ", e_end)
                        continue
                    counter = 0

                elif float(row[1]) >= bis_thresh and counter >= time_thresh:
                    event = event + 1
                    if (len(e_start) == len(e_end) + 1):
                        e_end.append(x_plot_counter-1)
                        print("E_START: ", e_start)
                        print("E_END: ", e_end)
                    counter = 0



            elif flag == 0:

                x_plot_counter = x_plot_counter + 1
                x_arr.append(x_plot_counter)
                y_arr.append(float(row[1]))
                time_array.append(rDT[1][:-3])

                # print(float(row[1]),"\n")

                if float(row[1]) < bis_thresh:
                    if counter == 0:
                        e_start.append(x_plot_counter)
                        print("E_START: ", e_start)
                        print("E_END: ", e_end)
                    counter = counter + 1

                elif float(row[1]) >= bis_thresh and counter < time_thresh:
                    if (len(e_start) != 0 and counter < time_thresh and len(e_start) == len(e_end) + 1):
                        e_start.pop()
                        print("E_START: ", e_start)
                        print("E_END: ", e_end)
                    elif (len(e_start) == 0 and len(e_end) == 0):
                        print("E_START: ", e_start)
                        print("E_END: ", e_end)
                        continue
                    counter = 0

                if counter >= time_thresh:
                    event = event + 1
                    e_end.append(x_plot_counter - 1)
                    print("E_START: ", e_start)
                    print("E_END: ", e_end)
                    counter = 0

                break
    csvf.close()
    return event, x_arr, y_arr, e_start, e_end,time_array



def plot_bis(event, x_arr, y_arr, e_start, e_end, bis_thresh, time_thresh,time_array):

    print("Time array: ", time_array)
    print("No of events: ", event)
    x_arr = np.array(x_arr)
    y_arr = np.array(y_arr)
    my_xt = time_array
    fig, ax = plt.subplots(1, figsize=(50, 15))
    ax.grid()
    plt.xticks(rotation=75)
    plt.xticks(x_arr, my_xt)
    plt.plot(x_arr, y_arr)
    print(e_start)
    print(e_end)
    threshLine = np.array(list(50.0 for x in range(len(x_arr))))
    plt.plot(x_arr, threshLine, linestyle = 'dotted')



    for i in range(len(e_end)):
        plt.fill_between(x_arr, y_arr,color="red", where=(x_arr >= e_start[i]) & (x_arr <= e_end[i]))



    plt.xlabel('Timeline')
    plt.ylabel('AVGBIS')
    plt.text(1, 90, f"Event Count: {event} \nAVGBIS Threshold: {bis_thresh} \nTime Tolerance: {time_thresh}\nInitial Time: {time_array[0]}", weight='bold', size=10 ,color='white' ,bbox={'facecolor': 'black', 'alpha': 0.5, 'pad': 10})
    plt.show()

# event, x_arr, y_arr, e_start, e_end = bisVal_csv(sDate, sTime, eDate, eTime, bis_thresh, time_thresh, csv_file)
# plot_bis(event, x_arr, y_arr, e_start, e_end)
