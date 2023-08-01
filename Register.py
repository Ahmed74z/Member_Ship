from tkinter import *
from files.Functions import *
from constants import *
import subprocess

register = Tk()
register.title('Register')
register.config(background='#EDE6E3', width=500, height=600)
register.maxsize(500, 600)
register.minsize(500, 600)

master_var = StringVar()
pass_var = StringVar()
def submit():
    info = [
        name_entry.get().title(),
        user_name_entry.get(),
        pass_label_entry.get(),
        master_code_entry.get()
    ]
    auth = admin_sign(info)
    register.destroy()
    subprocess.run(['python', login_path], check=True)
    print(auth)


def pass_check_func():
    if pass_var.get() == 'on':
        pass_label_entry.config(show='*')
    elif pass_var.get() == 'off':
        pass_label_entry.config(show='')


def master_check_func():
    if master_var.get() == 'on':
        master_code_entry.config(show='*')
    elif master_var.get() == 'off':
        master_code_entry.config(show='')


name = Label(register, text='Name: ', font=('Calibri', 14), background='#EDE6E3')
name.place(x=150, y=100)

name_entry = Entry(register)
name_entry.config(font=("Arial Bold", 14))
name_entry.place(x=150, y=130, width=200,)
######################################
user_name_label = Label(register, text='User Name:', font=('Calibri', 14), background='#EDE6E3')
user_name_label.place(x=150, y=170)

user_name_entry = Entry(register)
user_name_entry.config(font=("Arial Bold", 14))
user_name_entry.place(x=150, y=200, width=200, height=30)
######################################
pass_label = Label(register, text='Password:', font=('Calibri', 14), background='#EDE6E3')
pass_label.place(x=150, y=240)

pass_label_entry = Entry(register)
pass_label_entry.config(font=("Arial Bold", 14))
pass_label_entry.place(x=150, y=270, width=200, height=30)

pass_check = Checkbutton(register, onvalue='on', offvalue='off',
                         background='#EDE6E3', relief='flat', command=pass_check_func, variable=pass_var)
pass_check.place(x=350, y=270)
pass_var.set(value='off')
######################################
master_code = Label(register, text='Master Code', font=('Calibri', 14), background='#EDE6E3')
master_code.place(x=150 ,y=310)

master_code_entry = Entry(register)
master_code_entry.config(font=("Arial Bold", 14))
master_code_entry.place(x=150, y=340, width=200,)

master_check = Checkbutton(register, onvalue='on', offvalue='off',
                         background='#EDE6E3', relief='flat', command=master_check_func, variable=master_var)
master_check.place(x=350, y=340)
master_var.set(value='off')
######################################
result = Label(register, font=('Candra', 8), background='#EDE6E3', foreground='red', text='')
result.place(x=150, y=370)

submit = Button(register, text='Sign Up', relief='flat', command=submit)
submit.config(background='#00BD9D', font=('Britannic Bold', 18), foreground='white')
submit.place(x=150, y=400, width=200, height=40)

register.mainloop()
