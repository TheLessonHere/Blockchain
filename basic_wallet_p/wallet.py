import tkinter as wallet
from tkinter import Text, messagebox, font
import hashlib
import requests
import sys
import json
import os

root = wallet.Tk()

titleFont = font.Font(family="Helvetica", size=16)
title = wallet.Label(root, text="LambdaCoin Wallet", font=titleFont)
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
user_transactions = []
r = requests.get(url="http://127.0.0.1:5000/user_transactions", json=request)
data = r.json()
print(data)
if isinstance(data['transactions'], list):
    user_transactions = F"{data['transactions']}"
else:
    user_transactions = "Server Error Processing Request"


transactionsLabel = wallet.Label(transactions, text="Transactions:", width=480)
transactionsLabel.pack()

transactionsList = wallet.Label(transactions, text=user_transactions, width=480)
transactionsList.pack()

user_id = wallet.Entry(root, width=30)
user_id.pack()
user_id.insert(0, "Enter your User ID")

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