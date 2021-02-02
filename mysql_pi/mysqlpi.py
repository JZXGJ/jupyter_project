import mysql.connector
import numpy as np

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="jtwx1234",
    database="att_simu_wz"
)

control_table_name = 'telemetry_data_info'
dynamics_table_name = 'dynamics_data_info'

mycursor = mydb.cursor()

def get_column(column_name, table_name):
    mycursor.execute("SELECT " + column_name + " FROM " + table_name)
    data = np.array(mycursor.fetchall())
    return data

def get_table(table_name):
    mycursor.execute("SELECT * FROM " + table_name)
    return mycursor.fetchall()

def get_unit(column_name, table_name):
    mycursor.execute("SELECT " + column_name + " FROM " + table_name)
    unit_list = mycursor.fetchall()
    unit = unit_list[0][0]
    if unit == "null":
        unit = ""
    return data, unit

def get_column_name(table_name):
    mycursor.execute("SHOW COLUMNS FROM " + table_name)
    res = mycursor.fetchall()
    x = []
    for t in res:
        x.append(t[0])
    return x

def get_control_data_name():
    return get_column_name(control_table_name)

def get_control_data(column_name):
    return get_column(column_name, control_table_name)

def get_dynamics_data(column_name):
    return get_column(column_name, dynamics_table_name)

