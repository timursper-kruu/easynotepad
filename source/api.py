import project
from tkinter import *
import config

config.author = "API" # изменение автора
config.version = "1.0" # изменение версии
config.yoomoney = "нет" # изменение реквизитов ЮMoney

project.user_text.delete(0.1, END) # Удаление исходного текста
project.user_text.insert(0.1, "Это тест API!") # Добавление нового текста

project.user_text.configure(background="#FFFFF1", foreground="#000000")

project.start()