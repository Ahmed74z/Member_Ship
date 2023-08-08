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


def master_call(main):
    master_label = Label(main, text='Master Code', relief='flat')
    master_entry = Entry(main)
    master_button = Button(main, text='Unlock', command=lambda: admin_lock(master_entry.get(), main))

    master_label.place(x=5, y=5, width=120, height=26)
    master_label.config(font=('Arial', 11), relief='flat')

    master_entry.place(x=130, y=5, width=200, height=26)
    master_entry.config(font=('Arial', 11), relief='flat')

    master_button.place(x=5, y=40, width=150, height=35)
    master_button.config(font=('Arial', 14), relief='flat')

    All_masterpage = [master_label, master_button]
    return All_masterpage


def admin_lock(code, main):
    pass
    if code == const.Code:
        global tree
        tree = ttk.Treeview(main, selectmode='extended')

        tree['column'] = ('name', 'user_name', 'passcode')
        tree.column('#0', anchor='w', width=150, minwidth=150, stretch='no')
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

        tree.place(x=5, y=5, width=1700, height=850)


def add_list_admins():

    data_list = []
    db = connect(r'C:\Users\scorb\OneDrive\Documents\GitHub\Member_Ship\data\admins.db')
    cursor = db.cursor()
    cursor.execute('select * from admins')
    data_list = cursor.fetchall()
    # for row in all_rows:
    #     data_list.append((id_gen(), *row))
    return data_list


def theme_change_master(theme, widgets):
    theme_widget = widget_theme_pick(theme_l=theme)
    try:
        for widget in widgets:
            if widget.widgetName == 'label':
                widget.configure(background=theme_widget['bg_label'], foreground=theme_widget['color'])
            elif widget.widgetName == 'button' or widget.widgetName == 'tk_optionMenu':
                widget.configure(background=theme_widget['bg_button'], foreground=theme_widget['color'])
            elif widget.widgetName == 'radiobutton':
                widget.configure(background=theme_widget['bg_button_side'])
            else:
                widget.configure(background=theme_widget['bg_label'], foreground=theme_widget['color'])
    except:
        print('error at theme_change_master')
