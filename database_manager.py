from rich.console import Console
from rich import print as print_
import mysql.connector

def db_config():
    try:
        db = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='YOUR_PASSWORD_HERE'
        )
    except Exception as e:
        # Console.print_exception(show_locals=True)
        pass

    return db

def db_connector():
    db = mysql.connector.connect(host='localhost',user='root',passwd='YOUR_PASSWORD_HERE',database='PasswordManager')
    return db

def config(hashed_mp):
    db = db_config()
    cur = db.cursor()

    try:
        cur.execute('Create database PasswordManager')
    except Exception as e:
        print_("[red][!] An exception occurred while creating database")
        print()
        Console.print_exception(show_locals=True)

    #database for only one user, if someone asks for new user, it will result in an error and no database will be created!

    print_('[green][+][/green] Database created!')
    print()

    query = "Create table PasswordManager.secrets(master_pass text not null)"
    cur.execute(query)

    print_('[green][+][/green] Table secrets created!')


    query2 = 'Create table PasswordManager.passwords(website text not null, url text not null, email text, username text, password text not null)'
    cur.execute(query2)

    query3 = "insert into PasswordManager.secrets(master_pass) values(%s)"
    cur.execute(query3,(hashed_mp,))

    db.commit()

    db.close()


def retrieve_mp():
    db = db_connector()
    cur = db.cursor()

    query = 'Select * from PasswordManager.secrets'    
    cur.execute(query)
    
    stored_mp = cur.fetchone()[0]

    db.close()

    return stored_mp

