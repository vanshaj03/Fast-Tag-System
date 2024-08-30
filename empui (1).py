import time
import cv2
from pyzbar.pyzbar import decode
import mysql.connector




mydb = mysql.connector.connect(host="localhost", user="root", password="Putznslqc4", database = "fasttag")
mycursor = mydb.cursor()

cap = cv2.VideoCapture(0)
cap.set (3,640)
cap.set(4,480)

camera = True

while camera == True:
    mydb = mysql.connector.connect(host="localhost", user="root", password="Putznslqc4", database="fasttag")
    mycursor = mydb.cursor()
    success, frame = cap.read()

    for code in decode(frame):
        mydb = mysql.connector.connect(host="localhost", user="root", password="Putznslqc4", database="fasttag")
        mycursor = mydb.cursor()
        data = str(code.data.decode('utf-8')).split(sep="%")
        print(data)

        if str(data[3]) == "car": AmountCharged = 300
        if str(data[3]) == "bike": AmountCharged = 150
        if str(data[3]) == "bus": AmountCharged = 700
        if str(data[3]) == "government": AmountCharged = 0

        if int(input("Enter Toll ID")) == 1 or int(input("Enter Toll ID")) == 2 or int(input("Enter Toll ID")) == 3 or int(input("Enter Toll ID")) == 4 or int(input("Enter Toll ID")) == 5:
            tollid = int(input("Re Enter Toll ID to Confirm"))


            mycursor.execute('insert into tollgate (vehicleno,VehicleType,OwnerNo,OwnerName,AmountCharged,TollGateID) values (%s,%s,%s,%s,%s,%s)',(str(data[1]),str(data[3]),int(data[2]),str(data[0]),int(AmountCharged),tollid))
            mydb.commit()

            mycursor.execute('insert into agencydb (vehicleno,VehicleType,AmountCharged,TollGateID) values(%s,%s,%s,%s)',(str(data[1]),str(data[3]),int(AmountCharged),tollid))
            mydb.commit()



        time.sleep(5)
    cv2.imshow('scanner',frame)
    cv2.waitKey(1)