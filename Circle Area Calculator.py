from tkinter import *

window = Tk()
window.geometry('500x300')
window.configure(bg="gray")  

Tittle = Label(window, text='Circle Area Calculator',bg='gray',fg='white',font=('Times New Roman',15))
Tittle.grid(row=0, column=0)

label1 = Label(window, text='Enter the radius of circle:',bg='gray',fg='white',font=('Times New Roman',6))
label1.place(x=20,y=100)

radius=DoubleVar()
textbox=Entry(window,text=radius,bg='gray',fg='white',font=('Times New Roman',6))
textbox.place(x=430,y=100)

def calculate():
     area=3.14*radius.get()*radius.get()
     emptylabel.config(text='The area is: '+str(area))
     
button=Button(window,text='Calculate',bg='gray',fg='white',font=('Times New Roman',5),command=calculate)
button.place(x=300,y=180)

emptylabel=Label(window,text='',bg='gray',fg='white',font=('Times New Roman',6))
emptylabel.place(x=280,y=300)

window.mainloop()