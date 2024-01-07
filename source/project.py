from tkinter import *
import tkinter.messagebox as mb
from threading import Thread
import time
from tkinter import font
from tkinter import filedialog
import os
import base64

root = Tk()
root.title("EasyNotepad")
root.geometry("800x300")
root.option_add("*tearOff", FALSE)

tip = Label(root, text="Введите текст:", font=('Arial', 18, "bold"))
tip.place(y=0)
text_font = ('Arial', 14)
add_min = 1

user_text = Text(root, font=text_font, background="#486C00")
user_text.place(y=30, height=290)
user_text.pack(fill=BOTH, expand=True)
user_text.insert(0.1, "Добро пожаловать в EasyNotepad!\nСохраните или откройте файл во вкладке \"Файл\"; Настройте вид текста во вкладке \"Редактировать\"; Включите автосохранение во вкладке \"Автосохранение\".")

# НОВОЕ ОКНО

def new_window():
    os.system("en.exe")
    print("Открытие окна: окно было успешно открыто")

# НОВОЕ ОКНО

# СОХРАНЕНИЕ / ОТКРЫТИЕ

def text_save():
    global user_text
    filepath = filedialog.asksaveasfilename()
    if filepath != "":
        text = user_text.get("1.0", END)
        file = open(filepath, "w", encoding='utf-8')
        file.write(text)
        file.close
        mb.showinfo('Успешно!', 'Файл успешно сохранён!')

def text_open():
    global user_text
    filepath = filedialog.askopenfilename()
    if filepath != "":
        user_text.delete(0.1, END)
        file = open(filepath, "r", encoding='utf-8')
        text = file.read()
        user_text.insert(0.1, text)
        file.close
        mb.showinfo('Успешно!', 'Файл успешно прочитан!')

# СОХРАНЕНИЕ / ОТКРЫТИЕ

autosave_works = False

# АВТОСОХРАНЕНИЕ

def autosave_turn():
    global autosave_works
    autosave_works = True
    print(autosave_works)
    th = Thread(target=autosave)
    th.start()

def autosave_off():
    global autosave_works
    autosave_works = False
    print(autosave_works)

def autosave():
    global autosave_works
    while autosave_works == True:
        global user_text
        time.sleep(3)
        t = user_text.get(0.1, END)
        filepath = filedialog.asksaveasfilename()
        if filepath != "":
            text = user_text.get("1.0", END)
            file = open(filepath, "w", encoding='utf-8')
            file.write(text)
            file.close
            print("Автосохранение: всё исправно работает!")

# АВТОСОХРАНЕНИЕ

clearT = lambda x=0.1, y=END : user_text.delete(x, y)

# РАЗМЕРЫ ТЕКСТА

def px18():
    global user_text
    text_font = ('Arial', 18)
    user_text.configure(font=text_font)

def px10():
    global user_text
    text_font = ('Arial', 10)
    user_text.configure(font=text_font)

def px15():
    global user_text
    text_font = ('Arial', 15)
    user_text.configure(font=text_font)

def px24():
    global user_text
    text_font = ('Arial', 24)
    user_text.configure(font=text_font)

# РАЗМЕРЫ ТЕКСТА

# ЭФФЕКТЫ ТЕКСТА

def bold():
    global user_text
    text_font = ('Arial', 14, 'bold')
    user_text.configure(font=text_font)

def italic():
    global user_text
    text_font = ('Arial', 14, 'italic')
    user_text.configure(font=text_font)

def underline_text():
    global user_text
    text_font = font.Font(size=14, underline=True)
    user_text.configure(font=text_font)

def overstrike_text():
    global user_text
    text_font = font.Font(size=14, overstrike=True)
    user_text.configure(font=text_font)

def reset_font(): # Сброс
    global user_text
    text_font = ('Arial', 14)
    user_text.configure(font=text_font)

# ЭФФЕКТЫ ТЕКСТА
    
actbg = "#486C00"
actfg = "#334C00"
bg = "#486C00"

# ЗАПУСК СКРИПТОВ

def python():
    global user_text
    filepath = filedialog.asksaveasfilename()
    if filepath != "":
        text = user_text.get("1.0", END)
        file = open(filepath, "w", encoding='utf-8')
        file.write(text)
        file.close()
        os.system(f"python {filepath}")
    
def cpp():
    global user_text
    filepath = filedialog.asksaveasfilename()
    if filepath != "":
        text = user_text.get("1.0", END)
        file = open(filepath, "w", encoding='utf-8')
        file.write(text)
        file.close()
        os.system(f"g++ {filepath} -o easynotepad")
        os.system(f"easynotepad.exe")

# ЗАПУСК СКРИПТОВ
    
# ГОТОВЫЕ СКРИПТЫ

def script01(): # Гипотеза Коллатца
    global user_text
    script = open('script/script1.py', "r", encoding='utf-8')
    user_text.delete(0.1, END)
    user_text.insert(0.1, script.read())
    script.close()
    print("Готовые скрипты: успешное чтение")

# ГОТОВЫЕ СКРИПТЫ

# МЕНЮ ШИФРОВАНИЯ

def readme_encrypt():
    mb.showwarning('Внимание!', 'При нажатии на одну из кнопок шифрования, весь текст в поле ввода будет зашифрован и текст будет заменён!!!')

def ascii85_encrypt():
    global user_text
    t = bytes(user_text.get(0.1, END), encoding = 'utf-8')
    user_text.delete(0.1, END)
    user_text.insert(0.1, base64.a85encode(t))

def base64_encrypt():
    global user_text
    t = bytes(user_text.get(0.1, END), encoding = 'utf-8')
    user_text.delete(0.1, END)
    user_text.insert(0.1, base64.b64encode(t))

def base32_encrypt():
    global user_text
    t = bytes(user_text.get(0.1, END), encoding = 'utf-8')
    user_text.delete(0.1, END)
    user_text.insert(0.1, base64.b32encode(t))

# МЕНЮ ШИФРОВАНИЯ
    
# МЕНЮ РАСШИФРОВАНИЯ

def base64_decode():
    global user_text
    t = bytes(user_text.get(0.1, END), encoding = 'utf-8')
    user_text.delete(0.1, END)
    user_text.insert(0.1, base64.b64decode(t))

def base32_decode():
    global user_text
    t = bytes(user_text.get(0.1, END), encoding = 'utf-8')
    user_text.delete(0.1, END)
    user_text.insert(0.1, base64.b32decode(t))

def ascii85_decode():
    global user_text
    t = bytes(user_text.get(0.1, END), encoding = 'utf-8')
    user_text.delete(0.1, END)
    user_text.insert(0.1, base64.a85decode(t))

# МЕНЮ РАСШИФРОВАНИЯ

encrypt_menu = Menu(activebackground=actbg, activeforeground=actfg, background=bg)
encrypt_menu.add_command(label="Ascii85", command=ascii85_encrypt)
encrypt_menu.add_command(label="Base64", command=base64_encrypt)
encrypt_menu.add_command(label="Base32", command=base32_encrypt)
encrypt_menu.add_command(label="README", command=readme_encrypt)

decode_menu = Menu(activebackground=actbg, activeforeground=actfg, background=bg)
decode_menu.add_command(label="Ascii85", command=ascii85_decode)
decode_menu.add_command(label="Base64", command=base64_decode)

script_start_menu = Menu(activebackground=actbg, activeforeground=actfg, background=bg)
script_start_menu.add_command(label="Python", command=python)
script_start_menu.add_command(label="C++ (компилятор g++)", command=cpp)

scripts_menu = Menu(activebackground=actbg, activeforeground=actfg, background=bg)
scripts_menu.add_command(label="Гипотеза Коллатца", command=script01)

dev_menu = Menu(activebackground=actbg, activeforeground=actfg, background=bg)
dev_menu.add_cascade(label="Запуск скрипта", menu=script_start_menu)
dev_menu.add_cascade(label="Готовые скрипты (Python)", menu=scripts_menu)
dev_menu.add_cascade(label="Шифрование", menu=encrypt_menu)
dev_menu.add_cascade(label="Расшифровка", menu=decode_menu)

file_menu = Menu(activebackground=actbg, activeforeground=actfg, background=bg)
file_menu.add_command(label="Сохранить", command=text_save)
file_menu.add_command(label="Открыть", command=text_open)
file_menu.add_command(label="Создать новое окно", command=new_window)

font_size_menu = Menu(activebackground=actbg, activeforeground=actfg, background=bg)
font_size_menu.add_command(label="10px", command=px10)
font_size_menu.add_command(label="15px", command=px15)
font_size_menu.add_command(label="18px", command=px18)
font_size_menu.add_command(label="24px", command=px24)

weight_text_menu = Menu(activebackground=actbg, activeforeground=actfg, background=bg)
weight_text_menu.add_command(label='Жирный', command=bold)
weight_text_menu.add_command(label="Наклонистый", command=italic)
weight_text_menu.add_command(label="Подчёркивание", command=underline_text)
weight_text_menu.add_command(label="Зачёркивание", command=overstrike_text)

font_menu = Menu(activebackground=actbg, activeforeground=actfg, background=bg)
font_menu.add_cascade(label="Размеры текста", menu=font_size_menu)
font_menu.add_cascade(label="Эффекты текста", menu=weight_text_menu)
font_menu.add_command(label="Сбросить настройки", command=reset_font)

edit_menu = Menu(activebackground=actbg, activeforeground=actfg, background=bg)
edit_menu.add_command(label="Очистить", command=clearT)
edit_menu.add_cascade(label="Шрифт", menu=font_menu)

autosave_menu = Menu(activebackground=actbg, activeforeground=actfg, background=bg)
autosave_menu.add_command(label="Включить", command=autosave_turn)
autosave_menu.add_command(label="Выключить", command=autosave_off)

def about():
    about_wnd = Tk()
    about_wnd.title("О программе")
    about_wnd.geometry("300x100")
    about_wnd.resizable(False,False)

    author = "SperApps PC"
    authorL = Label(about_wnd, text=f"Сделано {author} в 2024 году\nНа языке программирования Python\nПрограмма бесплатна на 100%\nВерсия: 050124")
    authorL.pack()

    yoomoney = "4100116326035946"
    donateL = Label(about_wnd, text=f"ЮMoney для донатов: {yoomoney}")
    donateL.pack()

    about_wnd.mainloop()

main_menu = Menu(activebackground=actbg, activeforeground=actfg, background=bg)
main_menu.add_cascade(label="Файл", menu=file_menu)
main_menu.add_cascade(label="Редактировать", menu=edit_menu)
main_menu.add_cascade(label="Автосохранение", menu=autosave_menu)
main_menu.add_cascade(label="Режим разработчика", menu=dev_menu)
main_menu.add_command(label="О программе", command=about)

root.config(menu=main_menu, background="#486C00")
root.mainloop()
