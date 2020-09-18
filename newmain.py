import sqlite3
conn = sqlite3.connect('id.db')
import tkinter as tk
import ctypes
ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )


conn = sqlite3.connect('id.db')
conn.execute("CREATE TABLE IF NOT EXISTS idAddress(_id integer PRIMARY KEY, studentName text, ID integer)")
root = tk.Tk()
root.title("ID List")
submit_label = tk.Label(root, text="Add a New person to the Data Base : ",  font="Tahoma 17  underline")
submit_label.grid(row=0, column=0)
def submit():
    conn = sqlite3.connect('id.db')
    c = conn.cursor()
    ign = nameA.get()
    idAdr = idAdress.get()

    c.execute("SELECT * FROM idAddress WHERE studentName=? AND ID=?", (ign, int(idAdr)))
    a = c.fetchall()
    if a == []:
        c.execute("""INSERT INTO idAddress(studentName, ID) VALUES(:f_name, :id_name)""",
                  {'f_name': ign.lower(), 'id_name': idAdr})
        conn.commit()
        conn.close()
        nameA.delete(0, 'end')
        idAdress.delete(0, 'end')
        nameA.delete(0, 'end')
        idAdress.delete(0, 'end')
    else:
        nameA.delete(0, 'end')
        idAdress.delete(0, 'end')
        print("FUCK YOU")
c = conn.cursor() #Create cursor
# c.execute("""select * from id""")
#create a table
nameA = tk.Entry(root, width=40)
nameA.grid(row=1, column=2)
idAdress = tk.Entry(root, width=40)
idAdress.grid(row=2, column=2)
name_label = tk.Label(root, text="Enter full name : ",fg='blue')
name_label.grid(row=1, column=0)
id_label = tk.Label(root, text="Enter the ID number : ", fg='blue')
myButton = tk.Button(root, text="Click To Enter a new name to the data base", command=submit)
myButton.grid(row=3, column=2)
id_label.grid(row=2, column=0)
conn.commit() #Commit changes
submit_label = tk.Label(root, text="Searching given an ID : ", font=("Tahoma", 17))
submit_label.grid(row=4, column=0)
print_label1 = tk.Label(root)
def search():
    global print_label1
    print_label1.destroy()
    conn = sqlite3.connect('id.db')
    c = conn.cursor()
    idA = IdAdress.get()
    c.execute("SELECT studentName FROM idAddress WHERE ID=?", (str(idA),))
    a = str(c.fetchall())
    b = ""
    for element in a:
        if element.isalpha() or element == " ":
            b+= element

    print_label1 = tk.Label(root, text=b)
    print_label1.grid(row=6, column=0)
    conn.commit()
    conn.close()
IdAdress = tk.Entry(root, width=50)
IdAdress.grid(row=5, column=2)
IdLabel = tk.Label(root,fg='red', text="Enter the Desired ID : ")
IdLabel.grid(row=5, column=0)
myButton = tk.Button(root, text="Click To Search", command=search)
myButton.grid(row=6, column=2)
submit_label = tk.Label(root, text="Searching given Name : ", font=("Tahoma", 17))
submit_label.grid(row=7, column=0)
submit_label = tk.Label(root, text="Doesn't have to be Accurate ", font="Tahoma 8 bold")
submit_label.grid(row=9, column=0)
print_label = tk.Label(root)
def search_name():
    global print_label
    print_label.destroy()
    conn = sqlite3.connect('id.db')
    c = conn.cursor()
    idA = NameAdr.get()
    idB = "%" + idA + "%"
    c.execute("SELECT studentName, ID FROM idAddress WHERE studentName LIKE ?", (idB.lower(),))
    a = str(c.fetchall())
    listofshit = ["{", "}", "[", "]"]
    for i in listofshit:
        a = a.replace(i, "")

    print_label = tk.Label(root, text=a)
    print_label.grid(row=10, column=0)
    conn.commit()
    conn.close()
NameAdr = tk.Entry(root, width=50)
NameAdr.grid(row=8, column=2)
NameLabel = tk.Label(root, fg='purple', text="Enter the Desired Name : ")
NameLabel.grid(row=8, column=0)
myButton = tk.Button(root, text="Click To Search", command=search_name)
myButton.grid(row=9, column=2)
def delete_by_id():
    conn = sqlite3.connect('id.db')
    a = int(DeleteID.get())
    conn.execute("DELETE FROM idAddress WHERE ID=?", (a,))
    conn.commit()
    conn.close()
    DeleteID.delete(0, 'end')
DeleteID = tk.Entry(root, width=50)
DeleteID.grid(row=13 ,column=2)
DeleteLabel = tk.Label(root, text="Delete ID : ", font="Tahoma 18")
DeleteLabel.grid(row=12, column=0)
DeleteLabel2 = tk.Label(root, text="Enter the ID : ", fg="pink", font="bold")
DeleteLabel2.grid(row=13, column=0)
deletebutton = tk.Button(root, text="Enter to Delete", command=delete_by_id)
deletebutton.grid(row=14, column=2)
#Close Connection
conn.close()
# function that cleans the information

root.mainloop()


