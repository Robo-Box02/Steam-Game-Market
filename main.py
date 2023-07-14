from tkinter import *
root = Tk()
root.title('Test')
root.geometry('1000x500+300+250')


lbl1 = Label(root,text = "Sign in with account name", font="Arial 13 bold")
lbl1.place(relx=0.445,rely=0.3)
lbl2 = Label(root,text = "Password",font="Arial 13 bold")
lbl2.place(relx=0.900,rely=0.11)
entry_1 = Entry(root,font="Arial 12")
entry_1.place(relx=0.450,rely=0.320)
entry_1.config(width=22,borderwidth=4)
entry_2 = Entry(root,font="Arial 12")
entry_2.place(relx=0.90,rely=0.135)
entry_2.config(width=10,borderwidth=4)
btn1 = Button(root,text="Get in", font="Arial 10",width=5)
btn1.place(relx=0.930,rely=0.170)
btn2 = Button(root,text="Registration",font="Arial 10",width=10)
btn2.place(relx=0.880,rely=0.170)






root.mainloop()