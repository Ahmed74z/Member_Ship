from tkinter import *
from tkinter import ttk
from sqlite3 import *
import random

if __name__ == '__main__':
    from Member_Ship.files.Functions import *
    import Member_Ship.constants as const
    from Member_Ship.files.functions_theme import *
else:
    from files.Functions import *
    import constants as const
    from files.functions_theme import *


global All_masterpage
global tree
global theme


def master_call(main, theme_l):
        
    def tree_run():
        global tree
    
        tree = ttk.Treeview(main, selectmode='extended')

        tree['column'] = ('name', 'user_name', 'passcode')
        tree.column('#0', anchor='w', width=150, minwidth=150)
        tree.column('name', anchor='w', width=50, minwidth=10)
        tree.column('user_name', anchor='w', width=50, minwidth=10)
        tree.column('passcode', anchor='w', width=50, minwidth=10)

        tree.heading('#0', anchor='w', text='ID')
        tree.heading('name', anchor='w', text='Name')
        tree.heading('user_name', anchor='w', text='User Name')
        tree.heading('passcode', anchor='w', text='Password')
        data_list = add_list_admins()
        for row in data_list:
            tree.insert(parent='', index='end', iid=row[0], text=f'{row[0]}', values=(row[1:]))

        tree.place(x=5, y=5, width=1700, height=650)

    def admin_lock(code, main, theme):
        global tree
        global widgets

        if code == const.Code:
            
            master_label.pack_forget()
            master_entry.pack_forget()
            master_button.pack_forget()
            
            tree_run()

            # add & del choice
            
            del_entry.place(x=180, y=700, width=200, height=26)
            del_entry.config(font=('Arial', 14), relief='flat')
            del_entry.insert(0, 'Username to delete')
            
            name_entry.place(x=180, y=750, width=200, height=26)
            name_entry.config(font=('Arial', 14), relief='flat')
            name_entry.insert(0, 'Name to add')
            
            username_entry.place(x=400, y=750, width=200, height=26)
            username_entry.config(font=('Arial', 14), relief='flat')
            username_entry.insert(0, 'Username')
            
            pass_entry.place(x=620, y=750, width=200, height=26)
            pass_entry.config(font=('Arial', 14), relief='flat')
            pass_entry.insert(0, 'Password')
            
            add_button.place(x=5, y=750, width=150, height=26)
            add_button.config(font=('Arial', 14), relief='flat')
            
            del_button.place(x=5, y=700, width=150, height=26)
            del_button.config(font=('Arial', 14), relief='flat')
            
            widgets = [add_button, del_button]
            theme_change(theme=theme, frames=[], widgets=widgets)
            

            
    def add_admin():
        db = connect(r'C:\Users\scorb\OneDrive\Documents\GitHub\Member_Ship\data\admins.db')
        cursor = db.cursor()
        
        cursor.execute(f'insert into admins values ("{id_gen()}", "{name_entry.get().title()}", "{username_entry.get()}", "{pass_entry.get()}")')
    
        db.commit()
        db.close()
            
        tree.destroy()
        tree_run()
        
        
        name_entry.insert(0, 'Name to add')
        username_entry.insert(0, 'Username')
        pass_entry.insert(0, 'Password')
        


    def del_admin():
        
        db = connect(r'C:\Users\scorb\OneDrive\Documents\GitHub\Member_Ship\data\admins.db')
        cursor = db.cursor()
        
        cursor.execute(f'delete from admins where user_name = "{del_entry.get()}"')

        db.commit()
        db.close()
            
        tree.destroy()
        tree_run()
        
        del_entry.insert(0, 'Username to delete')
        
    add_button = Button(main, text='Add', command=add_admin)
    del_button = Button(main, text='Delete', command=del_admin)
    
    del_entry = Entry(main)
    name_entry = Entry(main)
    username_entry = Entry(main)
    pass_entry = Entry(main)
    
    master_label = Label(main, text='Master Code', relief='flat')
    master_entry = Entry(main)
    master_button = Button(main, text='Unlock', command=lambda: admin_lock(master_entry.get(), main, theme=theme_l))

    master_label.place(x=5, y=5, width=120, height=26)
    master_label.config(font=('Arial', 11), relief='flat')

    master_entry.place(x=130, y=5, width=200, height=26)
    master_entry.config(font=('Arial', 11), relief='flat')

    master_button.place(x=5, y=40, width=150, height=35)
    master_button.config(font=('Arial', 14), relief='flat')

    All_masterpage = [master_label, master_button, add_button, del_button, name_entry, username_entry, pass_entry, del_entry]
    return All_masterpage


def add_list_admins():

    data_list = []
    db = connect(r'C:\Users\scorb\OneDrive\Documents\GitHub\Member_Ship\data\admins.db')
    cursor = db.cursor()
    cursor.execute('select * from admins')
    data_list = cursor.fetchall()
    return data_list


