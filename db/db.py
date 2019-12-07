import sqlite3 as sql

DB_FILE = 'database.db'

#create table
def create_db():
    try:
        conn = sql.connect(DB_FILE)
        print("Opened database successfully")
        conn.execute('CREATE TABLE users (user_name TEXT, first_name TEXT,  last_name TEXT,user_pass TEXT)')
        print("Table created successfully")
        conn.close()
    except:
        print("Table created failed")

#insert user to database
def insert_user(entities):
    try:
        with sql.connect(DB_FILE) as con:
            cur = con.cursor()
            cur.execute('INSERT INTO users (user_name,first_name,last_name,user_pass)  VALUES(?, ?, ?,?)', entities)            
            con.commit()
            msg = "Record successfully added"
    except sql.Error as error:
        con.rollback()
        msg = "error in insert operation",error
        
    finally:
        print(msg)
        con.close()
#check user and password is valid
def check_user(user_name,user_pass):
    try:
        with sql.connect(DB_FILE) as con:
            cur = con.cursor()
            cur.execute('SELECT count(*) FROM users WHERE user_name =? AND user_pass =?', (user_name,user_pass))
            rows = cur.fetchall()
            #print(cur.rowcount)
            for row in rows:
                if user_name in row:
                    msg = "valid user"
                else:
                    msg = "Invalid user"
            
    except:
        msg = "error in retrive operation"
        
    finally:
        print(msg)
        con.close()
if __name__ == "__main__":
    user_name = "admin" 
    first_name = "Nazrul"
    last_name = "Islam" 
    user_pass = "1234"
    entities =(user_name,first_name,last_name,user_pass)
    #insert_user(entities)
    check_user(user_name,user_pass)