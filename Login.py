from tkinter import *
from tkinter import PhotoImage
from files.Functions import *
from constants import *
import subprocess

login = Tk()
login.config(background='#EDE6E3', width=500, height=600)
login.title('Login')
login.maxsize(500, 600)
login.minsize(500, 600)

show_pass_var = StringVar()

image = PhotoImage(file=const.logo_path)
image_label = Label(login, image=image, background='#EDE6E3')
image_label.place(x=175, y=50)

def main_call():
    login.destroy()
    subprocess.run(['python', path_main], check=True)


def register_click():
    login.destroy()
    subprocess.run(['python', register_path], check=True)


def check_admin():
    info = [
        user_name_entry.get(),
        pass_label_entry.get()
    ]
    check = admin_check(info)
    if check == 'Found':
        main_call()
    elif check == 'Not found':
        result.config(text='Invalid User name or Password!')
        pass


def pass_check():
    if show_pass_var.get() == 'on':
        pass_label_entry.config(show='*')
    elif show_pass_var.get() == 'off':
        pass_label_entry.config(show='')


user_name_label = Label(login, text='User Name:', font=('Calibri', 14), background='#EDE6E3')
user_name_label.place(x=150, y=180)

user_name_entry = Entry(login)
user_name_entry.config(font=("Arial Bold", 14))
user_name_entry.place(x=150, y=210, width=200, height=30)

pass_label = Label(login, text='Password:', font=('Calibri', 14), background='#EDE6E3')
pass_label.place(x=150, y=250)

show_pass = Checkbutton(login, command=pass_check, onvalue='on',
                        offvalue='off', variable=show_pass_var, relief='flat', background='#EDE6E3')
show_pass.place(x=350, y=280)
show_pass_var.set(value='off')

pass_label_entry = Entry(login)
pass_label_entry.config(font=("Arial Bold", 14))
pass_label_entry.place(x=150, y=280, width=200, height=30)

result = Label(login, font=('Candra', 8), background='#EDE6E3', foreground='red')
result.place(x=150, y=310)

submit = Button(login, text='Login', relief='flat', command=check_admin)
submit.config(background='#00BD9D', font=('Britannic Bold', 18), foreground='white')
submit.place(x=150, y=380, width=200, height=40)

register = Label(login, text='Register', cursor='hand2', fg='#3F3244', font=('Arial', 10), background='#EDE6E3')
register.place(x=435, y=570)
register.bind('<Button-1>', lambda event: register_click())

info = [
    user_name_entry.get(),
    pass_label_entry.get()
]


# "raised", "sunken", "flat", "ridge", "solid", "groove"
login.mainloop()
