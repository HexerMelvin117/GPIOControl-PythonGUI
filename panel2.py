from Tkinter import *
from ttk import *
from PIL import ImageTk, Image
import tkFont
import tkMessageBox
import time
import os
import sys
import datetime

#hola
#Creating Windows
v0 = Tk()
v0.title("Dashboard GPIO")
v0.geometry("600x400+0+0")

#Function definition
def gpio17on():
	#os.system("sudo /./home/pi/gpio17on.sh")
	apagado17.place_forget()
	encendido17.place(x=40,y=130)
	os.system("sudo echo 1 >> /./home/melvin/TradCompProyecto/status17.txt")

def gpio17off():
    #os.system("sudo /./home/pi/gpio17off.sh")
	encendido17.place_forget()
	apagado17.place(x=40,y=130)
	os.system("sudo echo 0 >> /./home/melvin/TradCompProyecto/status17.txt")

def gpio27on():
	#os.system("sudo /./home/pi/gpio27on.sh")
	apagado27.place_forget()
	encendido27.place(x=340,y=130)
	os.system("sudo echo 1 >> /./home/melvin/TradCompProyecto/status27.txt")

def gpio27off():
	#os.system("sudo /./home/pi/gpio27off.sh")
	encendido27.place_forget()
	apagado27.place(x=340,y=130)
	os.system("sudo echo 0 >> /./home/melvin/TradCompProyecto/status27.txt")

def gpio22on():
	#os.system("sudo /./home/pi/gpio22on.sh")
	apagado22.place_forget()
	encendido22.place(x=240,y=280)
	os.system("sudo echo 1 >> /./home/melvin/TradCompProyecto/status22.txt")

def gpio22off():
	#os.system("sudo /./home/pi/gpio22off.sh")
	encendido22.place_forget()
	apagado22.place(x=240,y=280)
	os.system("sudo echo 0 >> /./home/melvin/TradCompProyecto/status22.txt")

#font settings
text_title=tkFont.Font(family="Helvetica",size=18)
text_normal=tkFont.Font(family="Helvetica",size=12)

#Labels zone
Label_title=Label(v0,text="GPIO PANEL",font=text_title).place(x=200,y=10)
Label_gp=Label(v0,text="GPIO",font=text_normal).place(x=10,y=50)
Label_ac=Label(v0,text="Action",font=text_normal).place(x=100,y=50)
Label_17=Label(v0,text="gpio17",font=text_normal).place(x=40,y=100)
Label_27=Label(v0,text="gpio27",font=text_normal).place(x=340,y=100)
Label_22=Label(v0,text="gpio22",font=text_normal).place(x=240,y=250)


#Image Definition
img_17on=PhotoImage(file="on.gif")
img_17off=PhotoImage(file="off.gif")

imgRoja=Image.open("greenlight.gif") 
imgVerde=Image.open("redlight.gif")
img_encendido=ImageTk.PhotoImage(imgVerde)
img_apagado=ImageTk.PhotoImage(imgRoja)


#Labels para Encendido/Apagado
encendido17=Label(image=img_encendido)
encendido17.place(x=40,y=130)

apagado17=Label(image=img_apagado)
apagado17.place(x=40,y=130)

encendido27=Label(image=img_encendido)
encendido27.place(x=340,y=130)
apagado27=Label(image=img_apagado)
apagado27.place(x=340,y=130)

encendido22=Label(image=img_encendido)
encendido22.place(x=240,y=280)
apagado22=Label(image=img_apagado)
apagado22.place(x=240,y=280)


#buttons zone
btn_17on=Button(v0,image=img_17on,command=gpio17on).place(x=100,y=100)
btn_17off=Button(v0,image=img_17off,command=gpio17off).place(x=200,y=100)

btn_27on=Button(v0,image=img_17on,command=gpio27on).place(x=400,y=100)
btn_27off=Button(v0,image=img_17off,command=gpio27off).place(x=500,y=100)

btn_22on=Button(v0,image=img_17on,command=gpio22on).place(x=300,y=250)
btn_22off=Button(v0,image=img_17off,command=gpio22off).place(x=400,y=250)
#Final
v0.mainloop()
