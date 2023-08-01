from tkinter import *
from tkinter import ttk
from files.Functions import *
from files.functions_theme import *
import constants as const

global All_frames_mainpage
global All_widgets_mainpage
def home_call(main):
    gender_var = StringVar()
    gender_var.set('Male')
    state_var = StringVar()

    def member_add():

        data = [
            fname_add_entry.get(), lname_add_entry.get(),
            int(age_add_entry.get()), gender_var.get(),
            sub_add_entry.get(), 'Subscribed'
        ]
        fname_add_entry.delete(0, 'end')
        lname_add_entry.delete(0, 'end')
        age_add_entry.delete(0, 'end')
        sub_add_entry.delete(0, 'end')
        member_addition(data)

        text_box.config(state='normal')
        text_box.delete("1.0", 'end')
        text_box.insert("1.0", 'Addition Done!')
        text_box.config(state='disabled')

    def member_del():
        info = [
            fname_del_entry.get(),
            lname_del_entry.get()
        ]
        fname_del_entry.delete(0, 'end')
        lname_del_entry.delete(0, 'end')
        member_deletion(info)

        text_box.config(state='normal')
        text_box.delete("1.0", 'end')
        text_box.insert("1.0", 'Deletion Done!')
        text_box.config(state='disabled')

    def edit_show():
        info = [
            fname_edit_entry.get(),
            lname_edit_entry.get()
        ]
        data = member_edit_show(info)
        sub_state.config(state='normal')
        unsub_state.config(state='normal')
        state_var.set('Subscribed')
        save_edit_button.config(state='normal')
        show_edit_button.config(state='disabled')

        fname_edit_entry.delete(0, 'end')
        lname_edit_entry.delete(0, 'end')

        fname_edit_entry.insert(0, data[1])
        lname_edit_entry.insert(0, data[2])

        fname_edit_entry.config(state='disabled')
        lname_edit_entry.config(state='disabled')

        age_edit_entry.insert(0, data[3])
        sub_edit_entry.insert(0, data[5])

        text = f'ID: {data[0]}\nFirst Name: {data[1]}\nLast Name: {data[2]}\nAge: {data[3]}\nGender: {data[4]}\nSubscription: {data[5]}\nRegistration Time: {data[6]}\nState: {data[7]}'

        text_box.config(state='normal')
        text_box.delete("1.0", 'end')
        text_box.insert("1.0", text)
        text_box.config(state='disabled')

    def edit_save():
        info = [
            fname_edit_entry.get(),
            lname_edit_entry.get(),
            age_edit_entry.get(),
            sub_edit_entry.get(),
            state_var.get()
        ]
        member_edit_save(info)

        fname_edit_entry.config(state='normal')
        lname_edit_entry.config(state='normal')
        show_edit_button.config(state='normal')

        fname_edit_entry.delete(0, 'end')
        lname_edit_entry.delete(0, 'end')
        age_edit_entry.delete(0, 'end')
        sub_edit_entry.delete(0, 'end')

        sub_state.config(state='disabled')
        unsub_state.config(state='disabled')
        save_edit_button.config(state='disabled')

    def check():
        info = [
            fname_chk_entry.get(),
            lname_chk_entry.get()
        ]
        data = member_check(info)

    theme_frame = frame_theme_pick(const.PRISMARINE)
    theme_widget = widget_theme_pick(const.PRISMARINE)

    #############################################
    # Add Frame
    add_frame = Frame(master=main)
    add_frame.place(x=0, y=0*160, width=4000, height=1000)

    fname_add_label = Label(add_frame, text='First Name', font=('Arial', 11))
    lname_add_label = Label(add_frame, text='Last Name', font=('Arial', 11))
    age_add_label = Label(add_frame, text='Age', font=('Arial', 11))
    sub_add_label = Label(add_frame, text='Subscription', font=('Arial', 11))
    male = Radiobutton(add_frame, variable=gender_var, value='Male', text='Male', indicatoron=False)
    female = Radiobutton(add_frame, variable=gender_var, value='Female', text='Female', indicatoron=False)

    fname_add_label.place(x=20, y=15, width=100)
    lname_add_label.place(x=20, y=40, width=100)
    age_add_label.place(x=20, y=65, width=100)
    sub_add_label.place(x=20, y=90, width=100)
    male.place(x=350, y=65, width=100)
    female.place(x=350, y=95, width=100)
    sep_add_add = ttk.Separator(add_frame)

    fname_add_entry = Entry(add_frame, relief='flat')
    lname_add_entry = Entry(add_frame, relief='flat')
    age_add_entry = Entry(add_frame, relief='flat')
    sub_add_entry = Entry(add_frame, relief='flat')  # not rendered

    # Placement of Info
    fname_add_entry.place(x=140, y=15, width=150)
    lname_add_entry.place(x=140, y=40, width=150)
    age_add_entry.place(x=140, y=65, width=150)
    sub_add_entry.place(x=140, y=90, width=150)
    sep_add_add.place(x=0, y=140, width=700)

    add_add_button = Button(add_frame, text='Add', relief='flat', command=member_add)
    add_add_button.place(x=350, y=15, width=100)
    #############################################
    # Delete Frame
    del_frame = Frame(master=main)
    del_frame.place(x=0, y=1*160, width=4000, height=1000)

    fname_del_label = Label(del_frame, text='First Name', font=('Arial', 11))
    lname_del_label = Label(del_frame, text='Last Name', font=('Arial', 11))
    del_button = Button(del_frame, text='Delete', font=('Arial', 11), command=member_del)
    sep_del = ttk.Separator(del_frame)

    fname_del_label.place(x=20, y=15, width=100)
    lname_del_label.place(x=20, y=40, width=100)
    sep_del.place(x=0, y=140, width=700)
    del_button.place(x=140, y=70, width=60)

    fname_del_entry = Entry(del_frame, relief='flat')
    lname_del_entry = Entry(del_frame, relief='flat')

    fname_del_entry.place(x=140, y=15, width=150)
    lname_del_entry.place(x=140, y=40, width=150)

    # Edit Frame
    edit_frame = Frame(master=main)
    edit_frame.place(x=0, y=2*160, width=4000, height=1000)

    fname_edit_label = Label(edit_frame, text='First Name', font=('Arial', 11))
    lname_edit_label = Label(edit_frame, text='Last Name', font=('Arial', 11))
    age_edit_label = Label(edit_frame, text='Age', font=('Arial', 11))
    sub_edit_label = Label(edit_frame, text='Subscription', font=('Arial', 11))

    fname_edit_label.place(x=20, y=15, width=100)
    lname_edit_label.place(x=20, y=40, width=100)
    age_edit_label.place(x=20, y=65, width=100)
    sub_edit_label.place(x=20, y=90, width=100)
    sep_edit_add = ttk.Separator(edit_frame)

    fname_edit_entry = Entry(edit_frame, relief='flat')
    lname_edit_entry = Entry(edit_frame, relief='flat')
    age_edit_entry = Entry(edit_frame, relief='flat')
    sub_edit_entry = Entry(edit_frame, relief='flat')
    show_edit_button = Button(edit_frame, text='Show', relief='flat', command=edit_show)
    save_edit_button = Button(edit_frame, text='Save', relief='flat', command=edit_save)
    sub_state = Radiobutton(edit_frame, text='Subscribed', variable=state_var,
                            value='Subscribed', indicatoron=False)
    unsub_state = Radiobutton(edit_frame, text='Unsubscribed', variable=state_var,
                              value='Unsubscribed', indicatoron=False)

    # Placement of Info
    fname_edit_entry.place(x=140, y=15, width=150)
    lname_edit_entry.place(x=140, y=40, width=150)
    age_edit_entry.place(x=140, y=65, width=150)
    sub_edit_entry.place(x=140, y=90, width=150)
    show_edit_button.place(x=350, y=15, width=100)
    save_edit_button.place(x=350, y=40, width=100)
    sub_state.place(x=350, y=65, width=100)
    unsub_state.place(x=350, y=90, width=100)
    sep_edit_add.place(x=0, y=140, width=700)

    sub_state.config(state='disabled')
    unsub_state.config(state='disabled')
    save_edit_button.config(state='disabled')

    # Check Frame
    chk_frame = Frame(master=main)
    chk_frame.place(x=0, y=3*160, width=4000, height=1000)

    fname_chk_label = Label(chk_frame, text='First Name', font=('Arial', 11))
    lname_chk_label = Label(chk_frame, text='Last Name', font=('Arial', 11))
    chk_button = Button(chk_frame, text='Check', font=('Arial', 11), command=check)
    sep_chk = ttk.Separator(chk_frame)

    fname_chk_label.place(x=20, y=15, width=100)
    lname_chk_label.place(x=20, y=40, width=100)
    sep_chk.place(x=0, y=140, width=700)
    chk_button.place(x=140, y=70, width=60)

    fname_chk_entry = Entry(chk_frame, relief='flat')
    lname_chk_entry = Entry(chk_frame, relief='flat')

    fname_chk_entry.place(x=140, y=15, width=150)
    lname_chk_entry.place(x=140, y=40, width=150)

    # Text Box
    text_box = Text(master=main, state='disabled', wrap='word', relief='flat', font=('Arial', 24))
    text_box.place(x=710, y=5, width=995, height=850)

    ################################################################
    sep_ver = ttk.Separator(main, orient='vertical')
    sep_ver.place(x=700, height=4000)

    All_frames_mainpage = [add_frame, del_frame, edit_frame, chk_frame]
    All_widgets_mainpage = [fname_add_label, lname_add_label, age_add_label, sub_add_label, add_add_button,
                            fname_del_label, lname_del_label, del_button,
                            fname_edit_label, lname_edit_label, age_edit_label, sub_edit_label, show_edit_button,
                            save_edit_button, fname_chk_label, lname_chk_label, chk_button, text_box]

    return [All_frames_mainpage, All_widgets_mainpage]


def theme_change_main(theme, frames, widgets):

    theme_widget = widget_theme_pick(theme_l=theme)
    theme_frame = frame_theme_pick(theme_l=theme)
    try:
        for frame in frames:
            frame.configure(background=theme_frame['main'])
    except:
        print('error at theme_change_main')
    try:
        for widget in widgets:
            if widget.widgetName == 'label':
                widget.configure(background=theme_widget['bg_label'], foreground=theme_widget['color'])
            elif widget.widgetName == 'button':
                widget.configure(background=theme_widget['bg_button'], foreground=theme_widget['color'])
            elif widget.widgetName == 'radiobutton':
                widget.configure(background=theme_widget['bg_button_side'], foreground=theme_widget['color'])
            elif widget.widgetName == 'text':
                widget.configure(background=theme_widget['text_box'])
    except:
        print('error at theme_change_main')




