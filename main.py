from getpass import getpass,getuser #module to get passwords without displaying them on terminal
import database_manager as db
import hashlib
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.tree import Tree
from rich import print as print_
from methods import add_data, retrieve_data, update_data, delete_record, modify_password
import password_gen
import datetime
from time import sleep
'''
This is a simple password manager where master password is the encryption key!
'''

divider = "-----------------------------------------------------------------------------------------------------------------------\n"
lockImg = """                               
                                   
                                                          ^jEQBQDj^             
                                                       r#@@@@@@@@@#r           
                                                       ?@@@#x_`_v#@@@x          
                                                       g@@@!     !@@@Q          
                                                       Q@@@_     _@@@B          
                                                    rgg@@@@QgggggQ@@@@ggr       
                                                    Y@@@@@@@@@@@@@@@@@@@Y       
                                                    Y@@@@@@@Qx^xQ@@@@@@@Y       
                                                    Y@@@@@@@^   ~@@@@@@@Y       
                                                    Y@@@@@@@@r r#@@@@@@@Y       
                                                    Y@@@@@@@@c,c@@@@@@@@Y       
                                                    Y@@@@@@@@@@@@@@@@@@@Y       
                                                    v###################v       
                                                   
                                                                
    """
checkImg = """                               
                                   
                                                                       `xx.  
                                                                     'k#@@@h`
                                                                   _m@@@@@@Q,
                                                                 "M@@@@@@$*  
                                                 `xk<          =N@@@@@@9=    
                                                T#@@@Qr      ^g@@@@@@5,      
                                                y@@@@@@Bv  ?Q@@@@@@s-        
                                                `V#@@@@@#B@@@@@@w'          
                                                    `}#@@@@@@@@#T`            
                                                      vB@@@@Bx               
                                                        )ER)                            
                                                                                                       
    """
vaultImg = """
                                        M@@ZzzzzzzzzzzzzzzzzzzzzzzzzzzzzZ@@6` 
                                        \@@: !vvxvvvvvvvvvvvvvvvvvvvvvxv~ :@@L 
                                        x@@` 0@@@@@@@@@@@@@@@@@@@@@@@@@@Q `@@c 
                                        x@@` $@@@@@@@@@@@@@@@@@@@@@@@@@@Q `@@c 
                                        x@@` $@@@@@@@@@@@@@@@@@@@@@@@@#Tr `@@c 
                                        x@@` $@@@@#I)!,,~L6@@@@@@@@@@@m   `@@c 
                                        x@@` $@@@v`L$@###M!-6@@@@@@@@@3   `@@c 
                                        x@@` $@@)`8@x`  ,d@zT@@@@@@@@@@MT `@@c 
                                        x@@` $@@ r@3            !@@@@@@@Q `@@c 
                                        x@@` $@@r`Q@\`  _Z@z}#@@@@@@@@0-` `@@c 
                                        x@@` $@@@)`T8@B##Z~-d@@@@@@@@@m   `@@c 
                                        x@@` $@@@@Bz*:,,!xd@@@@@@@@@@@E`  `@@c 
                                        x@@` $@@@@@@@@@@@@@@@@@@@@@@@@@@Q `@@c 
                                        x@@` $@@@@@@@@@@@@@@@@@@@@@@@@@@Q `@@c 
                                        x@@` $@@@@@@@@@@@@@@@@@@@@@@@@@@Q `@@c 
                                        \@@: !LLLLLLLLLLLLLLLLLLLLLLLLLL> :@@L 
                                        `d@@MwwwwwwwwwwwwwwwwwwwwwwwwwwwwM@@E` 
                                          ~z6Q@@@@@@$0$$$$0$$0$$0$@@@@@@B6z>   
                                            ,EEEEEd              ZEEEEE!                    
"""

console = Console()

def header():
    grid = Table.grid(expand=True)
    grid.add_column(justify="center", ratio=1)
    grid.add_column(justify="right")
    grid.add_row(
        "[b]Rich[/b] Layout application",
        datetime.datetime.now().ctime().replace(":", "[blink]:[/]"),
        )
    return Panel(grid, style="white on blue")

def menu(master_pass):
    
    while True:
        print(checkImg)
        print(divider)
        user_cmd = print_(
            """\n(a)dd profile | (r)etrieve data | (g)enerate password | (u)pdate records | (d)elete records| (m)odify password | e(x)it\n"""
        )
        user_inp = input("What would you like to do? ")
        print()

        if user_inp == "(a)":
            site = input('Enter website name: ')
            site_url = input('Enter site url: ')
            mail_id = input('Enter email id: ')
            username = input('Enter username: ')
            add_data(master_pass,site,site_url,mail_id,username)
            print('Password safely locked')
            print(lockImg)
        
        if user_inp == '(u)':
            print("Enter the username of the record which you would like to modify: ")
            name = input()

            update_data(master_pass,name)

        if user_inp == '(d)':
            print('Enter the username of the record which you would like to delete: ')
            name = input()
            
            delete_record(master_pass,name)

        if user_inp == '(r)':
            print('Enter the search fields, separated by a single space(ex: website url email)')
            search_fields = input()

            print('Would you like to decrypt all the passwords: ')
            yes_no = input('y/n: ')
            retrieve_data(master_pass,search_fields,True if yes_no.lower() == 'y' else False)

        if user_inp == '(m)':
            print('Enter the username of the record whose password you would like to modify: ')
            user = input()
            master_pass = input('Enter master password: ')

            mp_hashed = hashlib.sha256(master_pass.encode()).hexdigest()

            if mp_hashed == db.retrieve_mp():
                modify_password(master_pass,user)
            else:
                print_('[Red][!]wrong master password') 
            


        if user_inp == '(x)':
            break
        if user_inp == '(g)':
            print('Enter the amount of characters you want in the password: ')
            chars = int(input())

        with console.status("[bold green]Fetching data...",spinner='bouncingBall') as status:
            sleep(1)
            console.log(f"[green]Finished generating the password! Here it is: [/green]")


            print(password_gen.generate_password(chars))
            print_('[bold][green][+][/green]Success! Secure password generated')
            # console.log(f'[bold][red]Done!')



def main():
    
    #application tree:
    
    tree = Tree("Application Tree")
    tree.add("Master Password")
    tree.add("MySQL Database")
    tree.add("Master Password Key").add("Encryption/Decryption")
    tree.add("[red]Update").add("[green]Delete")
    tree.add("[blue]Retrieval")

    print_(tree)




    print('To begin with the app, please create a master password(1) or type 2 if you already have an account')
    inp = int(input())

    print('Make sure you store the master password in a safe location or else your account will be unrecoverable\n')
    while True:
            if inp == 1:
                master_pass = getpass(prompt='Enter the master pass: ')
                verification = getpass(prompt='Enter it again(to verify): ')
                
                print()
                if verification != master_pass and master_pass.strip() != '':
                    print_('[yellow][-] Enter the master pass again')
                    continue
                else:
                    hashed_mp = hashlib.sha256(master_pass.encode()).hexdigest()
                    db.config(hashed_mp)

                    break

            elif inp == 2:
                print('Enter your master password')    
                master_pass = getpass(prompt='Master password')
                stored_pass = db.retrieve_mp()
                hashed_mp = hashlib.sha256(master_pass.encode()).hexdigest()

                if hashed_mp == stored_pass:
                    print_('[green][+][/green] Password matched')
                    print()
                    break
                else:
                    print_("[red][!] Password unmatched")
                    print_(":warning:")
                    print()
                    continue
            print()
            print_('[green][+][/green] Password hashed!')
            


    menu(master_pass) #do not pass hashed master password as any one can see it and use it to decrypt and encrypt the stored passwords, however master_pass is plain text, and hashed mp cannot be un-hashed. 


if __name__ == "__main__":
    print_(header())
    main()