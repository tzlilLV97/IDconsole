import sqlite3
conn = sqlite3.connect('id.db')
import tkinter as tk
import ctypes
ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )
def main():

    conn = sqlite3.connect('id.db')
    conn.execute("CREATE TABLE IF NOT EXISTS idAddress(studentName text, ID integer)")
    root = tk.Tk()
    root.title("ID List")
    submit_label = tk.Label(root, text="Add a New person to the Data Base : ",  font="Tahoma 17  underline")
    submit_label.grid(row=0, column=0)
    def submit():
        conn = sqlite3.connect('id.db')
        c = conn.cursor()
        ign = nameA.get()
        idAdr = idAdress.get()
        c.execute("""INSERT INTO idAddress VALUES(:f_name, :id_name)""",{'f_name' : ign.lower(), 'id_name' : idAdr})
        conn.commit()
        conn.close()
        nameA.delete(0, 'end')
        idAdress.delete(0, 'end')
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
    def search():
        conn = sqlite3.connect('id.db')
        c = conn.cursor()
        idA = IdAdress.get()
        c.execute("SELECT studentName FROM idAddress WHERE ID=?", (str(idA),))
        a = c.fetchall()
        print_label = tk.Label(root, text=a)
        print_label.grid(row=6, column=0)
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
    def search_name():
        conn = sqlite3.connect('id.db')
        c = conn.cursor()
        idA = NameAdr.get()
        idB = "%" + idA + "%"
        c.execute("SELECT * FROM idAddress WHERE studentName LIKE ?", (idB.lower(),))
        a = c.fetchall()
        print_label = tk.Label(root, text=a)
        print_label.grid(row=9, column=0)
        conn.commit()
        conn.close()

    NameAdr = tk.Entry(root, width=50)
    NameAdr.grid(row=8, column=2)
    NameLabel = tk.Label(root, fg='purple', text="Enter the Desired Name : ")
    NameLabel.grid(row=8, column=0)
    myButton = tk.Button(root, text="Click To Search", command=search_name)
    myButton.grid(row=9, column=2)

    #Close Connection
    conn.close()
# function that cleans the information

    root.mainloop()


if __name__ == "__main__":
    main()
