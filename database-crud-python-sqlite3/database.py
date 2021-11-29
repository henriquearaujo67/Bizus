'''
Name: database.py
Data: 30/11/2021
Autor: Henrique Araujo
Versão: 1.0

Objetivo: modulo com funcionalidades básicas de conexão à bds:
    - sqlite3
    - msaccess
    - sqlserver
	- DNS Connection


The SQL Server driver is very old and does not support features of newer servers. 
Please try the Microsoft ODBC Driver 17 for SQL Server: https://www.microsoft.com/en-us/downloads/details.aspx?id=56567
Driver={ODBC Driver 17 for SQL Server};
Driver={ODBC Driver 11 for SQL Server}
'''


import sqlite3
import pyodbc
import sys
import string, random

def generate_key(stringLength=10):
    """Objective: Generate a random string of fixed length """
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))
	
	

def DNSConnection(p_dsn = 'EDMDB', p_user = 'edm', p_password = 'Landmark1'):
    # ('DSN=mynewdsn;UID=user;PWD=password')
    connstr = 'DNS=' + p_dsn + ';UID=' + p_user + ';PWD=' + p_password
    try:
        conn =  pyodbc.connect(connstr)
        return conn
    except :
        print("Unexpected error:", sys.exc_info()[0])
        raise


def sqlite3Connection(p_dbfile):
    try:
        conn = sqlite3.connect(p_dbfile)
        cur = conn.cursor()
        return conn
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

def sqlserverConnection(p_server, p_database, p_user, p_password):
    
    connstr = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+ p_server +';DATABASE='+ p_database +';UID='+ p_user +';PWD='+ p_password
    try:
        conn = pyodbc.connect(connstr)
        return conn
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

def msaccessConnection(p_dbfile):
    connstr = r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + p_dbfile + ";"
    try:
        conn = pyodbc.connect(connstr)
        return conn
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

def main():
    #connTestMSAccess()
    conn = sqlite3Connection('mydb.db')
    print( type(conn))


if __name__ == "__main__":
    main()