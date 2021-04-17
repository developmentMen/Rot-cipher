#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================
# Author	--> DevMen
# Date created	--> 09/04/2021
# Last modified	--> 17/04/2021
# Version	--> Python 3.8.5
# =============================
# col	_|__0___|___1___|___2___|
# row	0|<-_string to encrypt->|
#	1|rot-  ROT Button  rot+|
#	2|<-- output  string -->|
#	3| Check GitHub Button	|
'''
 esta es la GUI de rotCipher.py
	'''
# =============================
# Imports
import webbrowser as gb
from tkinter import *
from tkinter import ttk
# =============================

class GUIbruteRot(Frame):

	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.pySefiGUI()

	def pySefiGUI(self):
		self.f = Frame(self,bg="red")
		self.f.pack(expand=True,fill="both")

		self.myGh = Frame(self, bg="black")
		self.myGh.pack(expand=True,fill='both',side=BOTTOM)

# ============================
# Row 0
		textEnc = StringVar(self, value="text to encrypt")
		self.stringToEncrypt = Entry(self.f,width=45,bg="black",
			fg="white",bd=5,highlightcolor="red",justify=
			"center",cursor="target",relief="ridge",
			textvariable=textEnc,highlightbackground="white"
			,selectbackground="red",selectforeground="yellow")
		self.stringToEncrypt.grid(column=0,row=0,columnspan=3,
			padx=15,sticky="news",ipady=9)
# ============================
# Row 1
		self.rotMenos 	= Button(self.f,text="Rot -",
			width=6,activebackground="black",bg="red",
			activeforeground="white",font=", 20",
			highlightcolor="yellow",command=self.menos
			).grid(column=0,row=1,sticky="ew",pady=6)
		self.rotActual 	= Button(self.f, text="13",bd=3,
			bg="black",fg="white",activebackground="red",
			font=", 25", relief="flat",command=self.encrypt)
		self.rotActual.grid(column=1,row=1,sticky="nsew",
			padx=4,pady=4)
		self.rotMas 	= Button(self.f,text="Rot +",
			width=6,activebackground="black",bg="red",
			command=self.mas,activeforeground="white",
			font=", 20").grid(column=2, row=1,sticky="we")
# ===========================
# Row 2
		self.encrypted = Label(self.f,text="output here",
			font="Terminal",bg="black",fg="yellow")
		self.encrypted.grid(column=0,row=2,columnspan=3,sticky=
			"ew"
			)
# ==========================
# Row 3
# Check my github Button
		self.photo = PhotoImage(file=r"img/githubButton.png").subsample(
			30,33)
		self.ghButon = Button(self.myGh,highlightthickness=0,
			text="Check my GitHub --->",highlightcolor=
			"black",bg="black",borderwidth=0,activebackground=
			"black",relief="flat",activeforeground="white",
			command=self.gitHub,fg="white",image=self.photo,
			compound="right"
			).pack(expand=True,fill="x")

	def gitHub(self):
		gb.open("https://github.com/developmentMen")
	def menos(self):
		if int(self.rotActual["text"]) > 1:self.rotActual["text"] = str(int(self.rotActual["text"])-1)
		self.encrypt()
	def mas(self):
		self.rotActual["text"] = str(int(self.rotActual["text"])+1)
		self.encrypt()
	def generateKey(self,rotNum):
		ALPHABET = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
		]
		key={}
		for i, ch in enumerate(ALPHABET):
			if (i + int(rotNum)) < len(ALPHABET):
				key[ch] = ALPHABET[i + int(rotNum)]
			else:
				key[ch] = ALPHABET[(i + int(rotNum)) % len(ALPHABET)]
		return(key)
	def encrypt(self,):
		key = self.generateKey(self.rotActual["text"])
		encryptedText = ''
		for word in self.stringToEncrypt.get().split(' '):
			encryptedText += ' '
			for ch in word:
				if ch in key:
					encryptedText += key[ch]
				elif ch.lower() in key:
					encryptedText += key[ch.lower()].upper()
				else:
					encryptedText += ch
		self.encrypted["text"] = encryptedText


r = Tk()
r.wm_title("BruteRot")
r.resizable(False,False)
app = GUIbruteRot(r)
app.mainloop()
