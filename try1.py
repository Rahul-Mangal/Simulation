"""
Name:     Rahul Mangal
Email id: rahul.mangal2017@vitstudent.ac.in
Task:     Working with Mysql and CSV file in python

"""

"""
@Import:
mysql.connector - which connects mysql database with python.
CSV             - In order to read the data from CSV files.
"""

import mysql.connector
import csv

mydb = mysql.connector.connect(host="localhost",database="assignment",user="root",passwd="rahul2008", auth_plugin="mysql_native_password")
mycursor = mydb.cursor()

#If table already exists then drop table
mycursor.execute("DROP TABLE IF EXISTS Simulation_CY_Test")

#Create table Simulation_CY_Test 
mycursor.execute("create table Simulation_CY_Test(Time text(52))")


#Read the csv file and insert columns name into the mysql database
with open("Simulation_CY.csv", mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    count = 0
    l = []
    mycursor = mydb.cursor()
    for row in csv_reader:
        count += 1
        if(count == 2):
            #print(row)
            for i in row:
                x = i.split()
                s = "_".join(x)
                l.append(s)
                
for i in range(1,len(l)):
    mycursor.execute("alter table Simulation_CY_Test add "+ "`" + l[i] + "`" +" text(52)")
            
#Function which insert values of data
def InsertValues():
    command = "INSERT INTO Simulation_CY_Test VALUES("
    val = ""
    for i in range(len(l2)-1):
        if (len(l2[i]) > 0):
            val += " '" + l2[i] + "' ,"  
        else:
            val += " 'None',  " 
    val += " ' " + l2[-1] +"' )"

    command += val
    command += ";"
    mycursor.execute(command)
    
#Read the csv file and insert data into the mysql database
with open("Simulation_CY.csv", mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    count = 0
    l = []
    mycursor = mydb.cursor()
    for row in csv_reader:
        count += 1
        if(count > 2):
            l2 = []
            for i in row:
                l2.append(i)
            InsertValues()
    
    
    

                


      
                
        
