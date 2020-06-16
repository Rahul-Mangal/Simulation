"""
Name:     Rahul Mangal
Email id: rahul.mangal2017@vitstudent.ac.in
Task:     Working with Database and CSV file
"""


"""
@Import:
Firebase - Adds data to the firebase which is a google provided cloud service database.
CSV      - In order to read the data from CSV files.
"""
from firebase import firebase
import csv


def run_and_add_to_database():
    global j
    """
    This function is responsible for iterating throught the CSV file and getting the data from the rows and appending the
    data in the firebase row as per the column name specified in the table headers.
    
    Once, table headers are read, they are cleaned to satisfy the Google Firebase requirements of a key.
    
    This function dynamically works and modifies the database accordingly ie. if row/column is added or removed,
    the specific changes can be seen in the database.
    
    How database shifts work:
            modification of database -> 1. Checks, if row exist -> Yes - Modify with the latest data.
                                                                -> No  - Add a new row.
    """
    for line in reader_object:
        
        """
        Iterates within the reader_object created using the CSV library and gets each row within the csv file.
        """
        
        if(j == 0):
            j += 1
        elif(j == 1):
            table_headers        = line
            for i in range(len(table_headers)):
                """
                Clearing the table_headers to satisfy the requirements of the Firebase database 
                i.e. No Special Characters allowed.
                """
                table_headers[i] = str(table_headers[i]).replace("$", "Dollar")
                table_headers[i] = str(table_headers[i]).replace("/", "-")
                table_headers[i] = str(table_headers[i]).replace(".", " ")
            j+=1
            
        elif(j < 4):
            
            """
            Creates an dictionary with each iteration holding the values of each row 
            as seperate value with key as table header value.
            
            Once the dictionary is created, it is added to the Firebase with the specified data and location path.
            """
            
            d={}
            for i in range(len(line)):
                
                if (len(line[i])>0):
                    value              = str(line[i])
                    
                    """
                    Clearing the values to satisfy the requirements of the Firebase database 
                    i.e. No Special Characters allowed.
                    """
                    value               = value.replace("$", "Dollar")
                    value               = value.replace("/", "-")
                    value               = value.replace(".", " ")
                    d[table_headers[i]] = value

                else:
                    d[table_headers[i]] = "None"
                    value               = "None"

            firebase.put(db_name, "row"+str(j), data=d)        
            j += 1
            
        else:
            break
            
if __name__ == "__main__":
    """
        Opening CSV file to be read.
    """
    f                   = open("simulation.csv")


    """
    @params:
          reader_object - Reads from CSV file using reader function of the CSV
          firebase      - Creates firebase object by creating the Firebase Application on the specified database location.
          j             - Counter variable to keep track of the row running.
          db_name       - Name of the database
    """
    reader_object       = csv.reader(f)
    j                   = 0
    firebase            = firebase.FirebaseApplication("https://test-dc277.firebaseio.com/", None)
    db_name             = "/Simulation_CY_Test"
    
    run_and_add_to_database()