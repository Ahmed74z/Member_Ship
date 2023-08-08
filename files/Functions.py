# functions file
import random
from sqlite3 import *
import datetime
if __name__ == '__name__':
    import Member_Ship.constants as const
else:
    import constants as const


def id_gen():
    i = 0
    id_num = ''
    while i < 10:
        id_num = f'{id_num}{random.randint(0, 9)}'
        i = i + 1
    return int(id_num)


def data_day_retrieve(year, month, day):
    data_list = []

    try:
        db = connect(f'/data/{year}/{month}.db')
        cursor = db.cursor()

        data_list = cursor.execute(f'''select * from {day}''')
    except:
        print('Error to get database')

    return data_list


def data_retrieve(year, month):
    data_list = []
    try:
        db = connect(f'/data/{year}/{month}.db')
        cursor = db.cursor()

        if year % 4 == 0:
            days = const.months
        else:
            days = const.months_heavey

        for day in days:
            data_list.append(cursor.execute(f'''select * from {day}'''))
    except:
        print('Error to get database')
    return data_list


def member_retrieve(member_id):
    pass


def member_addition(info):
    try:
        db = connect(r'C:\Users\scorb\OneDrive\Documents\GitHub\Member_Ship\data\members.db')
        cursor = db.cursor()
        id_num_n = id_gen()
        cursor.execute('''create table if not exists members (id integer, 
                        fname text, lname text, age text, gender text, 
                        sub text, intime text, state text)''')
    except Error as e:
        print(f'error: {e}')

    try:
        cursor.execute(f'''insert into members values ({id_num_n} ,"{info[0].title()}", "{info[1].title()}", 
                        "{info[2]}", "{info[3].title()}", 
                        "{info[4].title()}", "{datetime.datetime.now().date()}", "{info[5]}")''')
    except Error as e:
        print(f'error: {e}')

    db.commit()
    db.close()


def member_deletion(info):
    try:
        db = connect(r'C:\Users\scorb\OneDrive\Documents\GitHub\Member_Ship\data\members.db')
        cursor = db.cursor()
    except Error as e:
        print(e)

    try:
        cursor.execute(f'''delete from members where fname="{info[0].title().strip()}" and lname="{info[1].title().strip()}"''')
        db.commit()
        db.close()
    except Error as e:
        print(e)


def member_edit_show(info):
    try:
        db = connect(r'C:\Users\scorb\OneDrive\Documents\GitHub\Member_Ship\data\members.db')
        cursor = db.cursor()
    except Error as e:
        print(e)

    try:
        cursor.execute(f'''select * from members where fname="{info[0].title()}" and lname="{info[1].title()}" ''')
        data = cursor.fetchone()
    except Error as e:
        print(e)

    return data


def member_edit_save(info):
    try:
        db = connect(r'C:\Users\scorb\OneDrive\Documents\GitHub\Member_Ship\data\members.db')
        cursor = db.cursor()
    except Error as e:
        print(e)
    try:
        cursor.execute(f'''update members set  age="{info[2]}", sub="{info[3].title().strip()}", state="{info[4].title().title().strip()}" 
                        where fname ="{info[0].title().title().strip()}" and lname="{info[1].title().title().strip()}" ''')
        db.commit()
        db.close()
    except Error as e:
        print(e)


def member_check(info):
    try:
        db = connect(r'C:\Users\scorb\OneDrive\Documents\GitHub\Member_Ship\data\members.db')
        cursor = db.cursor()
        cursor.execute(f'select * from members where fname = "{info[0].title().strip()}" and lname = "{info[1].title().strip()}" ')
        data = cursor.fetchone()
    except Error as e:
        print(e)

    return data


def admin_check(info):
    try:
        auth = 'Not found'
        db = connect(r'C:\Users\scorb\OneDrive\Documents\GitHub\Member_Ship\data\admins.db')
        cursor = db.cursor()
    except Error as e:
        print(e)

    try:
        cursor.execute(f'select * from admins')
        data = cursor.fetchall()
        for row in data:
            if info[0] == row[2]:
                auth = 'Found'
            if info[1] == row[3]:
                auth = 'Found'

    except Error as e:
        print(f'error: {e}')

    return auth


def admin_sign(info):
    try:
        auth = 'Added'
        db = connect(r'C:\Users\scorb\OneDrive\Documents\GitHub\Member_Ship\data\admins.db')
        cursor = db.cursor()
        cursor.execute('create table if not exists admins (id integer, name text, user_name text, password text)')
    except Error as e:
        print(e)

    try:
        cursor.execute('select name from admins')
        names = cursor.fetchall()
        if names:
            for row in names:
                if info[0] in row:
                    auth = 'Found'
                else:
                    if info[3] == const.Code:
                        cursor.execute(f'''insert into admins (id, name, user_name, password) 
                                        values ({id_gen()}, "{info[0]}", "{info[1]}", "{info[2]}")''')
                        db.commit()
                        db.close()
                    else:
                        auth = 'Invalid master'
        else:
            if info[3] == const.Code:
                cursor.execute(f'''insert into admins (id, name, user_name, password) 
                                values ({id_gen()}, "{info[0]}", "{info[1]}", "{info[2]}")''')
                db.commit()
                db.close()
    except Error as e:
        print(f'error: {e}')

    return auth

def if_true_return(inp):
    if inp:
        return inp
    