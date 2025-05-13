'''
Filename: createExec.py
Created Date: Monday, May 12th 2025, 9:40:10 am
Author: Pepe Alkalina
'''

from tkinter import *
from tkinter import messagebox
import datetime
from sys import exit
from createUserUbuntu import createUserSSH

def checkPassword(password, passwordConfirm):
    if password == passwordConfirm:
        return 0
    else:
        return 1

def checkExpireDate():
    try:
        datetime.date.fromisoformat(expireDate.get())
        return 0
    except ValueError:
        return 1

def checkAndCreateExec():
    if checkPassword(password.get(), passwordConfirm.get()) == 1:
        messagebox.showerror("ERROR", "Las contraseñas no coinciden")
    elif checkExpireDate() == 1:
        messagebox.showerror("ERROR", "El formato de la fecha de expiracion no es correcto, es YYYY-MM-DD")
    else:
        createUserSSH(user=user.get(), password=password.get(), expirationDate=expireDate.get(), sshUser='usuario', sshPasswd='1234', sshIP='192.168.64.5')
        messagebox.showinfo("INFO", "El usuario " + user.get() + " se ha creado correctamente")



root = Tk()
root.geometry("500x400")
root.title("morse")

Label(root, text="Nombre de Usuario").pack(pady=5)
user = Entry(root)
user.pack(pady=5)

Label(root, text="Contraseña:").pack(pady=5)
password = Entry(root, show="*")
password.pack(pady=5)
password.bind()

Label(root, text="Repita contraseña:").pack(pady=5)
passwordConfirm = Entry(root, show="*")
passwordConfirm.pack(pady=5)

Label(root, text="Intoduzca la fecha de expiracion de la cuenta (Si esta es temporal):").pack(pady=5)
expireDate = Entry(root)
expireDate.insert(0, "YYYY-MM-DD")
expireDate.pack(pady=5)

crearUsuario = Button(root, text="Crear usuario", width=15, command=checkAndCreateExec)
crearUsuario.pack(pady=40)

root.mainloop()
