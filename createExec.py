'''
Filename: createExec.py
Created Date: Monday, May 12th 2025, 9:40:10 am
Author: Pepe Alkalina
'''

from tkinter import *
from tkinter import messagebox
import datetime
import sys
import os
from cx_Freeze import setup, Executable
from createUserUbuntu import createUserSSH

### The scrcpy server IPv4
serverIP = ''

### Sudo use and passwd for create new user remotely
sshSudoUser = ''
sshSudoPasswd = ''

### change this variable if you want to put a inco to the .app file
appIconFile = ''

### change this for select build distribution option, check cx_Freeze docs
dist = ''

### Check passwd format for secure password
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

### Check input password an config password
def checkPassword(password, passwordConfirm):
	if not checkPasswdFormat(password):
		return 1
	elif password != passwordConfirm:
		return 2
	else:
		return 0

### check expire date format YYY-MM-DD
def checkExpireDate():
	try:
		datetime.date.fromisoformat(expireDate.get())
		return 0
	except ValueError:
		return 1

### generate the python binary to connect remotely
def generateBinary(scriptName):
	buildExeOptions = dict(
		include_msvcr=True
	)

	buildMacOptions = dict(
		iconfile=appIconFile, # change if you want to put a logo
		bundle_name=scriptName
	)

	if sys.platform == 'win32':
		base = 'Win32GUI' 
	else:
		base = None

	executables = [
		Executable(scriptName+ ".py")
	]

	setup(
		name="Remote Scrcpy",
		version="0.1",
		description="Connect to an remote scrcpy server with a ssh tunnel",
		options=dict(build_exe=buildExeOptions, bdist_mac=buildMacOptions), 
		executables=executables,
		script_args=["build", dist]
		)

### Copy to a file the connection script to generate a temp script
def generateScript(scriptName):

	script = f"""
from remoteScrcpyUtils import connectScrcpySSH


if __name__ == '__main__':
	connectScrcpySSH('{serverIP}', '{user.get()}', '{password.get()}', '{serial.get()}')
	"""

	with open(scriptName, 'w') as file:
		file.write(script)

### Check UI input and generates new user an generates the binary file
def checkAndCreateExec():
	if checkPassword(password.get(), passwordConfirm.get()) == 1:
		messagebox.showerror("ERROR", "Formato de la contraseña erroneo, esta tiene que tener de 8 a 12 caracteres, al menos un numero, una mayuscula y una minuscula")
	elif checkPassword(password.get(), passwordConfirm.get()) == 2:
		messagebox.showerror("ERROR", "Las contraseñas no coinciden")
	elif checkExpireDate() == 1:
		messagebox.showerror("ERROR", "El formato de la fecha de expiracion no es correcto, es YYYY-MM-DD")
	else:
		# Creates a temp SSH user for crete the tunnel
		createUserSSH(user=user.get(), password=password.get(), expirationDate=expireDate.get(), sshUser=sshSudoUser, sshPasswd=sshSudoPasswd, sshIP=serverIP)

		scriptName = user.get() + serial.get() + "RemoteScrcpy"
		generateScript(scriptName+ ".py")

		# generates the binary and delete the temp script
		messagebox.showinfo("INFO", "El usuario " + user.get() + " se ha creado correctamente, pulsa ok para generar el binario")
		generateBinary(scriptName)
		messagebox.showinfo("INFO", "Binario generado puede cerrar el programa")
		os.remove(scriptName + ".py")


### Creates a tkinter interface to get user create data and device serial
root = Tk()
root.geometry("300x500")
root.title("Remote Scrcpy")

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
