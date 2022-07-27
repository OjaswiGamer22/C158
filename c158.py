from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
root=Tk()
root.title("Credit card Authentication")
root.geometry("600x600")
root.config( background="yellow")
input1=Entry(root)
input1.place(relx=0.5,rely=0.2,anchor=CENTER)
img1=ImageTk.PhotoImage(Image.open("red_credit.png"))
label1=Label(root,image=img1)
label1.place(relx=0.5,rely=0.5,anchor=CENTER)
def check_credit():
    try:
        input_value=int(input1.get())
        messagebox.showinfo("Message","Credit card accepted")
    except(ValueError):
        messagebox.showinfo("Alert","Credit card not accepted please enter valid pincode")
        
    
    
button1=Button(root,text="Check credit card",command=check_credit)
button1.place(relx=0.5,rely=0.3,anchor=CENTER)
root.mainloop()