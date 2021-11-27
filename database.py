import sqlite3

def getConnection():
    pass

def main():
    #connTestMSAccess()
    try:
        conn = sqlite3.connect('mydb.db')
        cur = conn.cursor()
        return conn
    except:
        return None

if __name__ == "__main__":
    main()