import tkinter as wallet
from tkinter import *
import hashlib
import requests
import sys
import json
import os

root = wallet.Tk()

title = wallet.Label(root, text="LambdaCoin Wallet", font="Helvetica 16")
title.pack()

canvas = wallet.Canvas(root, height=600, width=600, bg="#263D42")
canvas.pack()

balance = wallet.Frame(root, bg="white")
balance.place(relwidth=0.8, relheight=0.075, relx=0.1, rely=0.05)

balanceLabel = wallet.Label(balance, text="Current Balance:", width=480)
balanceLabel.pack()

transactions = wallet.Frame(root, bg="white")
transactions.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.125)

uidFile = open('my_id.txt', 'r')
currentUID = uidFile.read()

request = {"id": currentUID}
user_transactions = StringVar()
r = requests.get(url="http://127.0.0.1:5000/user_transactions", json=request)
data = r.json()
print(data)
if isinstance(data['transactions'], list):
    user_transactions.set(F"{data['transactions']}")
else:
    user_transactions.set("Server Error Processing Request")


transactionsLabel = wallet.Label(transactions, text="Transactions:", width=480)
transactionsLabel.pack()

transactionsList = wallet.Label(transactions, textvariable=user_transactions, width=480)
transactionsList.pack()

uidLabel = wallet.Label(root, text="Change User ID:", width=30)
uidLabel.pack()
user_id = wallet.Entry(root, width=30)
user_id.pack()

def saveUID():
    f = open('my_id.txt', 'w')
    f.write(F'{user_id.get()}')
    currentUID = user_id.get()
    f.close()
    messagebox.showwarning("Saved", "User ID Saved")

save_uid = wallet.Button(root, text="Save", command=saveUID)
save_uid.pack()

root.title('LambdaCoinWallet')
root.mainloop()