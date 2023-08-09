import files.functions_theme as func
import constants as const
from files.Functions import *
from tkinter import *
from tkinter import PhotoImage
import pages.Main_page as Main
import pages.View_page as View
import pages.Master_page as Master
import datetime
import threading
import os

os.chdir(const.path)

root = Tk()
root.title('MEMBERS')
# root.geometry('1400x900')
root.state('zoomed')
root.minsize(500, 300)
root.config(background='black')

mode_list = ['Month', 'Day', 'Members']
themes_list = [const.PRISMARINE, const.LEMON, const.SAUCE, const.HERO]
theme_name = StringVar()
theme_name.set(themes_list[0])

side_var = StringVar()
month_var = StringVar()
month_var.set(const.Month)

day_var = StringVar()
day_var.set(const.months[month_var.get()])

mode_var = StringVar()

global all_wid


def theme_thread(e):
    def theme_click(theme=e):
        global all_wid

        theme_widget = func.widget_theme_pick(theme_l=theme)
        theme_frame = func.frame_theme_pick(theme_l=theme)

        All_frames[0].configure(background=theme_frame['main'])
        All_frames[1].configure(background=theme_frame['side'])
        All_frames[2].configure(background=theme_frame['header'])
        All_frames[3].configure(background=theme_frame['header'])

        for widget in All_widgets:
            if widget.widgetName == 'label':
                widget.configure(background=theme_widget['bg_label'], foreground=theme_widget['color'])
            elif widget.widgetName == 'button' or widget.widgetName == 'tk_optionMenu':
                widget.configure(background=theme_widget['bg_button'], foreground=theme_widget['color'])
            elif widget.widgetName == 'radiobutton':
                widget.configure(background=theme_widget['bg_button_side'])
            else:
                widget.configure(background=theme_widget['bg_label'], foreground=theme_widget['color'])

        choice = side_var.get()
        if choice == 'home_button':
            func.theme_change(theme=theme_name.get(), frames=all_wid[0], widgets=all_wid[1])
        elif choice == 'master_button':
            func.theme_change(theme=theme_name.get(), frames=[], widgets=all_wid)

    thread = threading.Thread(target=theme_click, args=(e,))
    thread.start()


def flex_load():
    global current, choice, all_wid
    choice = side_var.get()
    if current != choice:
        if choice == 'home_button':
            all_wid = main_load()
            func.theme_change(theme=theme_name.get(), frames=all_wid[0], widgets=all_wid[1])
        elif choice == 'view_button':
            all_wid = view_load()
        elif choice == 'master_button':
            all_wid = master_load()
            func.theme_change(theme=theme_name.get(), frames=[], widgets=all_wid)
    current = choice
    return all_wid


# Main Page load
def main_load():
    global main_frame
    for widget in main_frame.winfo_children():
        widget.destroy()

    all_mainpage = Main.home_call(main_frame)
    unlock_button = all_mainpage[0]
    days_menu.config(state='disabled')
    months_menu.config(state='disabled')
    year.config(state='disabled')
    mode_button.config(state='disabled')
    return all_mainpage


# View Page load
def view_load():
    global all_wid
    global main_frame
    for widget in main_frame.winfo_children():
        widget.destroy()

    all_wid = View.view_call(view=main_frame)

    days_menu.config(state='normal')
    months_menu.config(state='normal')
    year.config(state='normal')
    mode_button.config(state='normal')
    return all_wid


def set_month(event):
    if int(year.get()) % 4 ==0:
        months = const.months_over
    else:
        months = const.months
        
    new_days = list(range(1, months[event]+1))
    days_menu['menu'].delete(0, 'end')  # Clear current options

    for option in new_days:
        days_menu['menu'].add_command(label=option, command=lambda option=option: day_var.set(option))

    day_var.set(months[event])


def mode(choose):
    if choose == 'Month':
        data_list = View.month_retrieve(year=year.get(), month=month_var.get())
    elif choose == 'Day':
        data_list = View.day_retrieve(year=year.get(), month=month_var.get(), day=day_var.get())
    elif choose == 'Members':
        data_list = View.members_list_retrieve()


# Master load
def master_load():
    global all_wid
    global main_frame
    for widget in main_frame.winfo_children():
        widget.destroy()

    all_wid = Master.master_call(main_frame, theme_l=theme_name.get())

    days_menu.config(state='disabled')
    months_menu.config(state='disabled')
    year.config(state='disabled')
    mode_button.config(state='disabled')
    return all_wid


main_frame = Frame(root, borderwidth=5, width=4000, height=2500)
main_frame.grid(row=1, column=1, sticky=NSEW)
side_frame = Frame(root, borderwidth=5, width=200)
side_frame.grid(row=1, column=0, sticky=NS)
header_frame = Frame(root, borderwidth=5, width=500, height=150)
header_frame.grid(row=0, column=0, columnspan=2, sticky=EW)

# image
image = PhotoImage(file=const.logo_path)
image_label = Label(header_frame, image=image)
image_label.place(x=170, y=20)

# theme button
theme_button = OptionMenu(header_frame, theme_name, *themes_list, command=theme_thread)
theme_button.place(x=1700, y=80, width=150, height=30)
theme_button.config(font=('Arial', 11), relief='flat')

# Days menu
days_menu = OptionMenu(header_frame, day_var, *const.Days)
days_menu.place(x=990, y=80, width=80, height=30)
days_menu.config(font=('Arial', 11), relief='flat', state='disabled')

days_label = Label(header_frame, text='Days')
days_label.place(x=870, y=82, width=120, height=26)
days_label.config(font=('Arial', 11), relief='flat')

# Month menu
months_menu = OptionMenu(header_frame, month_var, *const.months, command=set_month)
months_menu.place(x=1240, y=80, width=120, height=30)
months_menu.config(font=('Arial', 11), relief='flat', state='disabled')

month_label = Label(header_frame, text='Month')
month_label.place(x=1120, y=82, width=120, height=26)
month_label.config(font=('Arial', 11), relief='flat')

# Year entry
year = Entry(header_frame)
year.insert(0, str(const.Year))
year.place(x=1500, y=82, width=80, height=26)
year.config(font=('Arial', 11), relief='flat', state='disabled')

year_label = Label(header_frame, text='Year')
year_label.place(x=1418, y=82, width=80, height=26)
year_label.config(font=('Arial', 11), relief='flat')

# Mode
mode_button = OptionMenu(header_frame, mode_var, *mode_list, command=mode)
mode_var.set(mode_list[0])
mode_button.place(x=600, y=82, width=120, height=26)
mode_button.config(font=('Arial', 11), relief='flat', state='disabled')

# home button in side menu
home_button = Radiobutton(side_frame, variable=side_var, text='Home', offrelief='flat', overrelief='flat'
                          , background='#5293ab', command=flex_load,
                          indicatoron=False, relief='flat', value='home_button', foreground='#333333')
home_button.config(font=('Arial', 11))
home_button.place(x=0, y=100, width=200, height=45)

# view button in side menu
view_button = Radiobutton(side_frame, variable=side_var, text='View', indicatoron=False, background='#5293ab',
                          relief='flat', value='view_button', offrelief='flat',
                          overrelief='flat', foreground='#333333', command=flex_load)
view_button.config(font=('Arial', 11))
view_button.place(x=0, y=150, width=200, height=45)

# master button in side menu
master_button = Radiobutton(side_frame, variable=side_var, text='Master', indicatoron=False, background='red',
                            relief='flat', value='master_button', offrelief='flat',
                            overrelief='flat', foreground='#333333', command=flex_load)
master_button.config(font=('Arial', 11))
master_button.place(x=0, y=200, width=200, height=45)

side_var.set(value='home_button')

# main page
All_frames = [main_frame, side_frame, header_frame, image_label]
All_widgets = [theme_button, home_button, view_button, master_button, year_label, month_label,
               months_menu, theme_button, days_menu, days_label, mode_button]

# theme apply at launch
side_var.set('home_button')
choice = side_var.get()
current = 'view_button'
flex_load()
theme_thread(const.PRISMARINE)
root.mainloop()
