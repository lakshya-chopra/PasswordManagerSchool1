import tabnanny
from rich.console import Console
from rich import print as print_
from rich.table import Table
from getpass import getpass,getuser
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes
from aesutil import encrypt,decrypt
from database_manager import db_config, db_connector
import base64

console = Console()

def init_master_key(master_pass):
    mp = master_pass.encode()
    key = PBKDF2(mp,''.encode(), 32 ,count=1000000,hmac_hash_module=SHA512) #ciphers the mp and creates a key that can be used for encryption and decryption of passwords
    return key

def add_data(master_pass,site,site_url,mail_id,user):
    
    site_pass = getpass('Password: ')

    """
    New passwords will be encrypted and decrypted using the master password which is only known to user (not hashed)
    """
    master_key = init_master_key(master_pass)

    encrypted_pass = encrypt(key=master_key,source=site_pass,keyType="bytes")

    db = db_connector() #connect to the database and add data
    cur = db.cursor()

    cur.execute('Insert into passwords(website, url, email, username, password) values(%s,%s,%s,%s,%s)',(site,site_url,mail_id,user,encrypted_pass))
    db.commit()

    db.close()

    print_("[green][+][/green] Data Added!")

    #we are inserting encrypted password so that no one can view them on using mysql

def retrieve_data(mp,search_fields,decrypt_password=False):

    db = db_connector()
    cur = db.cursor()

    search_fields = (search_fields.strip()).split() 
    for idx,i in enumerate(search_fields):
        (search_fields[idx].strip()).lower()


    if len(search_fields) == 0:
        query = 'Select * from PasswordManager.passwords'

    else: #strip and split search fields, then join them from a comma and add them directly to the query.
        sf = ','.join(search_fields)
        query = "Select {} from PasswordManager.passwords;".format(sf)

        cur.execute(query)
        res = cur.fetchall() #tuple #all rows returned
        res_lst = list(res)

        if len(res) == 0:
            print_('[yellow][-][/yellow] No results found')
        elif (decrypt_password and len(res) >= 1) or (not decrypt_password and len(res) >= 1):
            
            table = Table(show_header=True, header_style='bold',title='Results')
            # if 'website' in search_fields:
            #     table.add_column('website')
            # if 'url' in search_fields:
            #     table.add_column('Url')

            table.add_column("Website")
            table.add_column("URL")
            table.add_column("Email")
            table.add_column("Username")
            table.add_column("Password")


            print(res_lst)
            n = len(res[0]) #num of elems in all the records

            if decrypt_password:
                master_key = init_master_key(mp)
                
                for idx,i in enumerate(res_lst):
                    res_lst[idx] = list(res_lst[idx])
                    password = i[n-1]
                    decrypted = decrypt(key=master_key,source=password,keyType='bytes')
                    i[n-1] = decrypted

            for idx,i in enumerate(res): #res -> rows
                table.add_row(*res[idx])

            console.print(table)
            print_('[green][+][/green] TASK FINISHED!')

        db.close()

def update_data(master_pass,username):

    db = db_connector()
    cur = db.cursor()

    que1 = "Select * from PasswordManager.passwords where username = %s;"
    cur.execute(que1,(username,))

    res = cur.fetchall() #tuple containing the record where the required username is present.

    if len(res) == 0:
        print('NO record with username = {} found!'.format(username))
    else:
        table = Table(title='Results',show_header=True, header_style='bold',padding=3)

        table.add_column("Website",justify="right", style="green")
        table.add_column("URL",justify="right", style="magenta")
        table.add_column("Email",justify="right", style="cyan")
        table.add_column("Username",justify="right", style='green')
        table.add_column("Password",justify="right", style="turquoise2")

        table.add_row(*res)

        console.print(table)

        while True:
            print('What would you like to modify?')
            inp = input()
            inp = inp.lower()

            if inp in cur.column_names:
                print('Enter new value: ')
                new_val = input()

                que = "Update PasswordManager.passwords set {} = %s where username = '{};'".format(inp,username)
                cur.execute(que,(new_val,))
                db.commit()

                print_('[green][+][/green] Value updated!')
            else:
                print('No column found!')
                continue

            more = input("Would you like to modify more values (y/n): ")
            if more == 'y':
                continue
            else:
                db.close()
                break
            
def delete_record(mp,username):

    db = db_connector()
    cur = db.cursor()

    print('Are you sure you want to delete the record with username {} '.format(username))

    inp = input('y/n: ')
    if inp == 'y':
        cur.execute("Delete from PasswordManager.passwords where username = %s",(username,))
        db.commit()
        print("Record Deleted")
    else:
        pass

    db.close()
    return 0

        
                
            
        


