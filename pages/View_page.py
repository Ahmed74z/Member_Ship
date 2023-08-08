from tkinter import *
from tkinter import ttk
from sqlite3 import *
import random
if __name__ == '__main__':
    from Member_Ship.files.Functions import *
else:
    from files.Functions import *

global tree


def view_call(view):
    global tree
    tree = ttk.Treeview(view, selectmode='extended')

    tree['column'] = ('fname', 'lname', 'age', 'gender', 'sub', 'intime', 'state')
    tree.column('#0', anchor='w', width=150, minwidth=150, stretch='no')
    tree.column('fname', anchor='w', width=50, minwidth=10)
    tree.column('lname', anchor='w', width=50, minwidth=10)
    tree.column('sub', anchor='w', width=50, minwidth=10)
    tree.column('age', anchor='w', width=50, minwidth=10)
    tree.column('gender', anchor='w', width=50, minwidth=10)
    tree.column('intime', anchor='w', width=50, minwidth=10)
    tree.column('state', anchor='w', width=50, minwidth=10)

    tree.heading('#0', anchor='w', text='ID')
    tree.heading('fname', anchor='w', text='First Name')
    tree.heading('lname', anchor='w', text='Last Name')
    tree.heading('sub', anchor='w', text='Subscription')
    tree.heading('age', anchor='w', text='Age')
    tree.heading('gender', anchor='w', text='Gender')
    tree.heading('intime', anchor='w', text='Register Date')
    tree.heading('state', anchor='w', text='State')

    tree.place(x=5, y=5, width=1700, height=850)


def month_retrieve(year, month):
    global tree

    data_list = data_retrieve(year=year, month=month)
    for row in data_list:
        tree.insert(parent='', index='end', iid=row[0], text=f'{row[0]}', values=(row[1:]))

    tree.place(x=5, y=5)


def day_retrieve(year, month, day):
    global tree

    data_list = data_day_retrieve(year=year, month=month, day=day)
    for row in data_list:
        tree.insert(parent='', index='end', iid=row[0], text=f'{row[0]}', values=(row[1:]))

    tree.place(x=5, y=5)


def members_list_retrieve():
    try:
        db = connect(r'C:\Users\scorb\OneDrive\Documents\GitHub\Member_Ship\data\members.db')
        cursor = db.cursor()

        cursor.execute(f'''select * from members''')
        data_list = cursor.fetchall()

        for row in data_list:
            tree.insert(parent='', index='end', iid=row[0], text=f'{row[0]}', values=(row[1:]))

        tree.place(x=5, y=5)

    except:
        print('Error to get database')
