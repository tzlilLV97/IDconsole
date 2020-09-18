import pandas as pd
from datetime import date
import csv
import os
import tkinter as tk
import ctypes
ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )
import sqlite3

def main():
    data = pd.read_csv("alldata.csv", header=0)
    conn = sqlite3.connect('id.db')
    main = tk.Tk()
    main.title('Main')
    frame = tk.Frame(main)
    frame.pack()
    bottomframe = tk.Frame(main)
    bottomframe.pack(side='bottom')
    def Display():
        myLabel = tk.Label(main, text=data)
        myLabel.pack()
    myButton = tk.Button(main,text="Click To Display everyone",command=Display)
    myButton.pack()

    def Search_by_name():
        main.destroy()
        root = tk.Tk()
        root.title('Search By  Name')

        def return_id():
            data = pd.read_csv("alldata.csv", header=0)
            arr = data['Name'].to_numpy(dtype=str)
            tmp = None
            for idx, i in enumerate(arr):
                if i == name.get():
                    tmp = data['ID'][idx]
            myLabel = tk.Label(root, text=tmp)
            myLabel.pack()

        name = tk.Entry(root, width=50)
        name.insert(0, "Enter a Name : ")
        name.pack()
        myButton = tk.Button(root, text="Click To Search - Please be Accurate", command=return_id)
        myButton.pack()
        myButton2 = tk.Button(root, text="Click To Exit", command=root.destroy)
        myButton2.pack(side='bottom', fill='x', padx=0, pady=5)

        tk.mainloop()
    myButton2 = tk.Button(frame,text="Click to search by name",command=Search_by_name)
    myButton2.pack(side='left')

    def search_by_ID():
        main.destroy()
        root = tk.Tk()
        root.title('Search By  Name')

        def return_name():
            data = pd.read_csv("alldata.csv", header=0)
            arr = data['ID'].to_numpy(dtype=str)
            tmp = None
            for idx, i in enumerate(arr):
                if i == name.get():
                    tmp = data['Name'][idx]
            myLabel = tk.Label(root, text=tmp)
            myLabel.pack()

        name = tk.Entry(root, width=50)
        name.insert(0, "Enter an ID : ")
        name.pack()
        myButton = tk.Button(root, text="Click To Search - Please be Accurate", command=return_name)
        myButton.pack()
        myButton2 = tk.Button(root, text="Click To Exit", command=root.destroy)
        myButton2.pack(side='bottom', fill='x', padx=0, pady=5)

        tk.mainloop()
    myButton2 = tk.Button(frame, text="Click to search by ID", command=search_by_ID)
    myButton2.pack(side='left')
    def add_new():
        main.destroy()
        root = tk.Tk()
        root.title('Search By  Name')
        name = tk.Entry(root, width=50)
        name.insert(0, "Enter a Name : ")
        name.pack()
        ID = tk.Entry(root, width=50)
        ID.insert(0, "Enter an ID : ")
        ID.pack()
        def add_new():
            with open('alldata.csv', 'a', newline='', encoding="UTF-8") as f:
                writer = csv.writer(f)
                writer.writerow([str(name.get()), ID.get()])
            f.close()

        myButton = tk.Button(root, text="Click to add to the Data Base", command=add_new)
        myButton.pack()
        myButton2 = tk.Button(root, text="Click To Exit", command=root.destroy)
        myButton2.pack(side='bottom', fill='x', padx=0, pady=5)
        root.mainloop()
    myButton2 = tk.Button(frame, text="Click to add new", command=add_new)
    myButton2.pack()
    myButton2 = tk.Button(bottomframe, text="Click To Exit", command=main.destroy)
    myButton2.pack(side='bottom')
    main.mainloop()

main()