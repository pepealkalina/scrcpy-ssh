'''
Filename: createExec.py
Created Date: Monday, May 12th 2025, 9:40:10 am
Author: Pepe Alkalina
'''

from tkinter import *
from tkinter import messagebox
import datetime
import sys
from cx_Freeze import setup, Executable
from createUserUbuntu import createUserSSH

serverIP = '10.11.23.166'

def checkPasswdFormat(passw):

    if not 8 <= len(passw) <= 12:
        return False

    numeros = 0
    mayusculas = 0
    minusculas = 0

    for carac in passw:
        if carac.isspace():
            return False
        elif carac.isdigit():
            numeros += 1
        elif carac.isupper():
            mayusculas += 1
        elif carac.islower():
            minusculas += 1

    return numeros != 0 and mayusculas !=0 and minusculas != 0

def checkPassword(password, passwordConfirm):
	if not checkPasswdFormat(password):
		return 1
	elif password != passwordConfirm:
		return 2
	else:
		return 0

def checkExpireDate():
	try:
		datetime.date.fromisoformat(expireDate.get())
		return 0
	except ValueError:
		return 1

def generateBinary(scriptName):
	buildOptions = dict(
		include_msvcr=True
	)

	if sys.platform == 'win32':
		base = 'Win32GUI' 
	else:
		base = None

	executables = [
		Executable(scriptName)
	]

	setup(
		name="Remote Scrcpy Morse",
		version="0.1",
		description="Connect to an remote scrcpy server with a ssh tunnel",
		options=dict(build_exe=buildOptions), 
		executables=executables,
		script_args=["build"]
		)

def generateScript(scriptName):

	script = f"""
from remoteScrcpyUtils import connectScrcpySSH


if __name__ == '__main__':
	connectScrcpySSH('{serverIP}', '{user.get()}', '{password.get()}', '{serial.get()}')
	"""

	with open(scriptName, 'w') as file:
		file.write(script)


def checkAndCreateExec():
	if checkPassword(password.get(), passwordConfirm.get()) == 1:
		messagebox.showerror("ERROR", "Formato de la contraseña erroneo, esta tiene que tener de 8 a 12 caracteres, al menos un numero, una mayuscula y una minuscula")
	elif checkPassword(password.get(), passwordConfirm.get()) == 2:
		messagebox.showerror("ERROR", "Las contraseñas no coinciden")
	elif checkExpireDate() == 1:
		messagebox.showerror("ERROR", "El formato de la fecha de expiracion no es correcto, es YYYY-MM-DD")
	else:
		print(password.get())
		createUserSSH(user=user.get(), password=password.get(), expirationDate=expireDate.get(), sshUser='morse', sshPasswd='lab333', sshIP=serverIP)
		scriptName = user.get() + "RemoteScrcpy.py"
		generateScript(scriptName)
		messagebox.showinfo("INFO", "El usuario " + user.get() + " se ha creado correctamente, pulsa ok para generar el binario")
		generateBinary(scriptName)
		messagebox.showinfo("INFO", "Binario generado puede cerrar el programa")



root = Tk()
root.geometry("300x500")
root.title("morse")

Label(root, text="Nombre de Usuario").pack(pady=5)
user = Entry(root)
user.pack(pady=5)

Label(root, text="Contraseña:").pack(pady=5)
password = Entry(root, show="*")
password.pack(pady=5)

Label(root, text="Repita contraseña:").pack(pady=5)
passwordConfirm = Entry(root, show="*")
passwordConfirm.pack(pady=5)

Label(root, text="Intoduzca la fecha de expiracion de la cuenta\n(Si esta es temporal):").pack(pady=5)
expireDate = Entry(root)
expireDate.insert(0, "YYYY-MM-DD")
expireDate.pack(pady=5)

Label(root, text="Serial del dispositivo").pack(pady=5)
serial = Entry(root)
serial.pack(pady=5)

crearUsuario = Button(root, text="Generar Binario", width=15, command=checkAndCreateExec)
crearUsuario.pack(pady=40)

root.mainloop()
