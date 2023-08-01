# Functions file
from tkinter import *
import ttkbootstrap as ttb


def widget_theme_pick(theme_l):
    theme = {}

    if theme_l == 'Prismarine':
        theme = {
            'bg_label': '#467982',
            'bg_button': '#35ccbe',
            'bg_button_side': '#a6ded9',
            'text_box': '#86a9b0',
            'color': '#ffffff',
            'width': 5
        }

    elif theme_l == 'Lemon':
        theme = {
            'bg_label': '#c9db6e',
            'bg_button': '#fede00',
            'bg_button_side': '#e3ddb6',
            'text_box': '#bdc2a7',
            'color': '#595959',
            'width': 5
        }

    elif theme_l == 'Sauce':
        theme = {
            'bg_label': '#f2ebc9',
            'bg_button': '#c4b3b3',
            'bg_button_side': '#d1c0c1',
            'text_box':'#cccbc8',
            'color': '#454545',
            'width': 5
        }

    elif theme_l == 'Hero':
        theme = {
            'bg_label': '#9fd2e3',
            'bg_button': '#5f99ba',
            'bg_button_side': '#a9c3d1',
            'text_box': '#b3c2c7',
            'color': '#454545',
            'width': 5
        }

    return theme


def frame_theme_pick(theme_l):
    theme = {}

    if theme_l == 'Prismarine':
        theme = {
            'main': '#3C7782',
            'side': '#AECDCB',
            'header': '#DFE8E6'
        }

    elif theme_l == 'Lemon':
        theme = {
            'main': '#c6d18c',
            'side': '#DBE8D8',
            'header': '#174a2b'
        }

    elif theme_l == 'Sauce':
        theme = {
            'main': '#c9c4ab',
            'side': '#918E80',
            'header': '#433F30'
        }

    elif theme_l == 'Hero':
        theme = {
            'main': '#B1D4E0',
            'side': '#145DA0',
            'header': '#0C2D48'
        }

    return theme


def theme_change(theme, frames: Frame, widgets: Widget):
    theme_widget = widget_theme_pick(theme_l=theme)
    theme_frame = frame_theme_pick(theme_l=theme)
    
    frames[0].configure(background=theme_frame['main'])
    frames[1].configure(background=theme_frame['side'])
    frames[2].configure(background=theme_frame['header'])
    frames[3].configure(background=theme_frame['header'])


    for widget in widgets:
        if widget.widgetName == 'label':
            widget.configure(background=theme_widget['bg_label'], foreground=theme_widget['color'])
        elif widget.widgetName == 'button' or widget.widgetName == 'tk_optionMenu':
            widget.configure(background=theme_widget['bg_button'], foreground=theme_widget['color'])
        elif widget.widgetName == 'radiobutton':
            widget.configure(background=theme_widget['bg_button_side'])
        else:
            widget.configure(background=theme_widget['bg_label'], foreground=theme_widget['color'])



