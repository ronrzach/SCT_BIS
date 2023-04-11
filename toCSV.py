import csv

def spa_to_csv(folder, out_file, filename = "D:\CAREER\SCT HL7 Project\H11231513_SNB241927.spa"):
    out_path = folder+"\\"+out_file.strip()
    spa = open(filename, "r")
    # print(spa.read())
    l = len(spa.readline())
    cont = spa.readlines()
    dataList = []
    idx = 0

    # To find index of "AVGBIS"

    for i in range(l):
        if i == 1:
            continue
        elif i == 0:
            dataList = cont[i].split("|")
            for j in range(len(dataList)):
                if dataList[j].strip() == "AVGBIS":
                    idx = j;
                    break
            else:
                continue
            break
        else:
            continue


    # To transfer values to CSV file

    with open(out_path, "w", newline='') as csvf:
        csvw = csv.writer(csvf)
        for i in range(l):
            dataList = cont[i].split("|")
            csvrow = []
            csvrow.append(dataList[0].strip())
            csvrow.append(dataList[idx].strip())
            csvw.writerow(csvrow)
    csvf.close()
    return out_path



