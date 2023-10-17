from random import randint
from tkinter import*

root=Tk()
root.title("Random Paassword Generator")
root.geometry("600x400")


def new_rand():
    password_entry.delete(0,END)
    password_length=int(entry.get())
    my_password=''
    for x in range(password_length):
        my_password += chr(randint(33,126))

    password_entry.insert(0,my_password)

def reset():
    password_entry.delete(0,END)
        
    
labelframe=LabelFrame(root, text="Random Password Generator",font="arial,40,bold")
labelframe.pack(pady=20)

entry=Entry(labelframe,font="ariel,20")
entry.pack(padx=20,pady=20)

password_entry=Entry(root,text="",font="CASTELLAR,24,italic")
password_entry.pack(pady=20)

frame=Frame(root)
frame.pack(pady=20)

btn1=Button(frame,text="Generate",command=new_rand)
btn1.grid(row=0,column=0,padx=10)

btn2=Button(frame,text="Reset",command=reset)
btn2.grid(row=6,column=0,padx=10)

root.mainloop()
