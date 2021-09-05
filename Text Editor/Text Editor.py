from tkinter import *
from tkinter import filedialog, messagebox
import os
from tkinter.filedialog import asksaveasfile

root = Tk()
root.geometry('400x500')
root.title('Untitled-Jotter')


# Creating global variables
global text_area
global open_status_name
global selected
file_name = ''


def create_widgets():
    global text_area
    text_area = Text(root, font='Constantia 11', undo=True)
    text_area.pack(expand=True, fill=BOTH)
    scrollbar = Scrollbar(text_area, command=text_area.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    text_area['yscrollcommand'] = scrollbar.set


# Creating menu bar
    main_menu = Menu(root)
    m1 = Menu(root, tearoff=0)
    m1.add_command(label='New', command=new_file)
    m1.add_command(label='Save', command=save_file)
    m1.add_command(label='Save As...', command=save_file_as)
    m1.add_command(label='Open...', command=open_file)
    m1.add_separator()
    m1.add_command(label='Exit', command=close_window)
    root.config(menu=main_menu)
    main_menu.add_cascade(label='File', menu=m1)

    m2 = Menu(root, tearoff=0)
    m2.add_command(label='Undo', command=text_area.edit_undo)
    m2.add_command(label='Redo', command=text_area.edit_redo)
    m2.add_separator()
    m2.add_command(label='Cut', command=lambda: cut_text(False))
    m2.add_command(label='Copy', command=lambda: copy_text(False))
    m2.add_command(label='Paste', command=lambda: paste_text(False))
    m2.add_command(label='Delete', command=lambda: delete_text())
    root.config(menu=main_menu)
    main_menu.add_cascade(label='Edit', menu=m2)

    m3 = Menu(root, tearoff=0)
    m3.add_command(label='About Jotter', command=about)
    root.config(menu=main_menu)
    main_menu.add_cascade(label='Help', menu=m3)


def new_file():
    global text_area
    root.title('Untitled-Jotter')
    text_area.delete(1.0, END)
    global open_status_name
    open_status_name = False


def save_file_as():
    global text_area
    save_text_as = asksaveasfile(mode='w', defaultextension='.txt')
    if save_text_as:
        text_to_save = text_area.get('1.0', 'end-1c')
        save_text_as.write(text_to_save)
        save_text_as.close()
    else:
        messagebox.showinfo("Error", "Cancelled")


def save_file():
    global file_name
    global text_area
    if file_name:
        text_area_text = text_area.get('1.0', 'end-1c')
        save_text = open(file_name, 'w')
        save_text.write(text_area_text)
        save_text.close()
    else:
        messagebox.showinfo("Error", "No file open")


def open_file():
    global file_name
    global text_area
    file_name = filedialog.askopenfile(defaultextension='.txt', filetypes=[('All files', '*.*'), ('Text documents',
                                                                                                  '.txt')])
    file_name = file_name.name
    if file_name:
        global open_status_name
        open_status_name = file_name
    if file_name == "":
        file_name = None
    else:
        root.title(os.path.basename(file_name) + '-Jotter')
        text_area.delete(1.0, END)
        with open(file_name, 'r') as txt_r:
            data = txt_r.read()
            text_area.insert(END, data)


def close_window():
    root.destroy()


def cut_text(a):
    global text_area
    global selected
    if a:
        selected = root.clipboard_get()
    else:
        if text_area.selection_get():
            selected = text_area.selection_get()
            text_area.delete('sel.first', 'sel.last')
            root.clipboard_clear()
            root.clipboard_append(selected)


def copy_text(a):
    global selected
    global text_area
    if a:
        selected = root.clipboard_get()

    if text_area.selection_get():
        selected = text_area.selection_get()
        root.clipboard_clear()
        root.clipboard_append(selected)


def paste_text(a):
    global text_area
    global selected
    if a:
        selected = root.clipboard_get()
    else:
        if selected:
            position = text_area.index(INSERT)
            text_area.insert(position, selected)


def delete_text():
    global text_area
    global selected
    text_area.delete('1.0', END)


root.bind('<Control-x>', cut_text)
root.bind('<Control-c>', copy_text)
root.bind('<Control-v>', paste_text)


def about():
    messagebox.showinfo('About', "Developed by Aditya.")


create_widgets()
root.mainloop()
