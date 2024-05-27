from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext 
from tkinter import colorchooser
from tkinter.filedialog import asksaveasfile 
import webbrowser
import os

opoveschenie = ">оповещение: программа запущена и готова к работе!"
opoveschenie2 = ">оповещение: не забывайте после просмотра вашего сайта в браузере удалять файл output.html!"
opertation1 = ">операция: вставка текста из буфера обмена выполнена"
operation2 = ">операция: полная очистка выполнена"
operation3 = ">операция: идёт открытие html файла. Открытие скоро будет завершено"
operation4 = ">скопировано в буфер обмена"

root = tk.Tk()
root.title("WSengine (WebSite engine)")
root.pack_slaves()
root.geometry("1900x900")


def clear_text():
    txt.delete("1.0", tk.END)
    terminal.insert(1, operation2)

def save_project():
    text = txt.get("1.0", "end")
    file_path = filedialog.asksaveasfilename(defaultextension=".html", filetypes=[("HTML files", "*.html")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text)    
    

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("HTML files", "*.html")])
    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()
        txt.insert(tk.END, html_content)
        terminal.insert(1, operation3)

def open_text():
    file_path_two = filedialog.askopenfilename(filetypes=[("TEXT files", "*.txt")])
    with open(file_path_two, "r", encoding="utf-8") as file:
        text_content = file.read()
        txt.insert(tk.END, text_content)

def choose_color():
    color = colorchooser.askcolor(title="Выберите цвет")
    color_code = color[1]
    color_lab.config(bg=color_code)
    colors_list.insert(0, color_code)
    terminal.insert(1, ">операция: операция по выбору цвета начата. Цветовой код вашего выбранного цвета:" + color_code)


def paste_text(event):
    text = root.clipboard_get()
    cursor_position = txt.index(tk.INSERT)
    txt.insert(cursor_position, text)
    terminal.insert(1, opertation1)

def paste_text_two():
    text = root.clipboard_get()
    txt.insert(tk.END, text)
    terminal.insert(1, opertation1)

def clear_terminal():
    terminal.delete(tk.END)

def copy_to_clipboard():
    root.clipboard_append(txt.get('1.0', tk.END).rstrip())
    terminal.insert(1, operation4)

def exit():
    root.destroy()

def open_in_browser():
    text_content = txt.get("1.0", tk.END) 
    with open(f"output.html", "w") as file:
        file.write(text_content)
    webbrowser.open("output.html")

def delere():
    os.remove("output.html")

def base():
    txt.insert(tk.END, "<!DOCKTYPE html>\n<head>\n\n</head>\n<body>\n\n</body>")
    
    
txt = scrolledtext.ScrolledText(root, width=200, height=50)
txt.pack()
txt.place(x=100, y=0)
txt.bind("<Button-3>", paste_text)
btn_save = Button(root, text="сохранить", width=10, bg="yellow", command=save_project)
btn_save.grid(row=0)
btn_clear = Button(root, text="очистить всё", width=10, bg="red", command=clear_text)
btn_clear.grid(row=1)
btn_open = Button(root, text="открыть\nhtml\nфайл", width=10, bg="orange", command=open_file)
btn_open.grid(row=2)
btn_paste = Button(root, text="вставить\nиз буфера\nобмена", width=10, bg="gold", command=paste_text_two)
btn_paste.grid(row=3)
color_lab = Label(root, width=22, height=20, bg="gray")
color_lab.place(x=1725, y=0)
btn_color = Button(root, text="цвета", width=22, command=choose_color)
btn_color.place(x=1725, y=310)
Label(root, text="цветовой код:", bg="white").place(x=1765, y=340)
colors_list = Listbox(root, width=15, height=1)
colors_list.place(x=1760, y=365)
terminal = Listbox(root, width=270, height=12)
terminal.grid()
terminal.place(x=100, y=810)
terminal.insert(1, opoveschenie)
terminal.insert(1, opoveschenie2)
btn_clear_two = Button(root, text="очистить\nтерминал", bg="red", width=10, command=clear_terminal)
btn_clear_two.grid(row=4)
btn_copy = Button(root, text="копировать\nтекст", width=10, bg="magenta", command=copy_to_clipboard)
btn_copy.grid(row=5)
btn_quit = Button(root, text="выйти из\nпрограммы", width=10, bg="red", command=exit)
btn_quit.grid(row=6)
btn_browser = Button(root, text="смотреть\nв браузере", bg="cyan", width=10, command=open_in_browser)
btn_browser.grid(row=7)
btn_delete_browser = Button(root, text="удалить\noutput.html", width=10, bg="cyan", command=delere)
btn_delete_browser.grid(row=8)
btn_osnova = Button(root, text="создать\nоснову", width=10, bg="green", command=base)
btn_osnova.grid(row=9)
btn_open_txt = Button(root, text="открыть\ntxt\nфайл", bg="orange", width=10, command=open_text)
btn_open_txt.grid(row=10)

root.mainloop()
