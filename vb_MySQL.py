# Program to write MySQL commands in shell command
import mysql.connector
import os
import time
from tabular_form import *
connection = mysql.connector.connect(host = "165.22.14.77", database = "db_Venkatesh" ,user = "Venkatesh", password = "Venkatesh");

print("Welcome to the MySQL monitor.  Commands end with ; or \\g.")
print("Your MySQL connection id is 17896")
print("Server version: 5.7.32-0ubuntu0.18.04.1 (Ubuntu)")
print("\nCopyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.")
print("\nOracle is a registered trademark of Oracle Corporation and/or its")
print("affiliates. Other names may be trademarks of their respective")
print("owners.")
print("\nType 'help;' or '\\h' for help. Type '\\c' to clear the current input statement.\n")

while True:
    query = input("mysql>")
    my_cursor = connection.cursor()

    if query.upper() == "QUIT" or query.upper() == 'EXIT':
        print("Bye")
        connection.close()
        exit()
    elif query == 'system cls':
        os.system('cls')
    else:
        try:
            start_time = time.time()
            my_cursor.execute(query.replace(";", ""))
            end_time = time.time()
        except mysql.connector.errors.ProgrammingError:
            print("You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near %s at line 1"%(query))
            continue
        if query[:6].upper() == 'SELECT'  or query[:4].upper() == 'SHOW' or query[:8].upper() == 'DESCRIBE':
            num_fields = len(my_cursor.description)
            field_names = [description[0] for description in my_cursor.description]
            field_values = my_cursor.fetchall()
            print_column_names(field_names, field_values)
            if not field_values:
                print("Empty set[" + str(round(end_time - start_time, 2)) + "]")    
            else:
                print_field_values(field_names, field_values)
            print_pipe(field_names, field_values)
            print(str(len(field_values)) + " rows in set (" + str(round(end_time - start_time, 2)) +" secs)")
        else:
            continue
connection.close()
