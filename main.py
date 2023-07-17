from tkinter import*
from PIL import Image, ImageTk
root = Tk()
root.geometry('1920x1080')
frame_menu = Frame(root,width = 1920,height = 1080,bg = '#0f1948')
frame_menu.place(x=1,y=1)
frame_login = Frame(root,width=1920,height=1080)
frame_login.config(background="#0f1948")
lbl= Label(frame_menu,text="Login",font="Arial 14 bold")
lbl.place(relx=0.1,rely=0.1)

def main_menu():
    frame_menu.place_forget()
    root.geometry('1920x1080')
    frame_login.place(relx=0,rely=0.1)
    frame_menu.pack()





<<<<<<< HEAD
def enter_account():
    frame_menu.place_forget()
    frame_login.place(relx=0,rely=0)


img1 = Image.open("Photo/steam-icon-2048x2048-rbyixh0f.png")
resized_image = img1.resize((150,100))
photo = ImageTk.PhotoImage(resized_image)
label1 = Label(frame_menu, image=photo)
label1.image = photo
label1.place(relx=0, rely=0)

img = Image.open("Photo/Screenshot 2023-07-17 194419.png")
resized_image0 = img.resize((200,250))
photo0 = ImageTk.PhotoImage(resized_image0)
label0 = Label(frame_menu, image=photo0)
label0.image = photo0
label0.place(relx=0.298, rely=0.350)

img2 = Image.open("Photo/Capture.PNG")
resized_image2 = img2.resize((215,250))
photo1 = ImageTk.PhotoImage(resized_image2)
label2 = Label(frame_menu, image=photo1)
label2.bind("<ButtonPlus>",)
label2.image=photo1
label2.place(relx=0.184, rely=0.350)

img3 = Image.open("Photo/Capture3.PNG")
resized_image3 = img3.resize((420,200))
photo3 = ImageTk.PhotoImage(resized_image3)
label3=Label(frame_menu, image=photo3)
label3.image=photo3
label3.place(relx=0.184, rely=0.160)

img4 = Image.open("Photo/Capture4.PNG")
resized_image4 = img4.resize((420,200))
photo4 = ImageTk.PhotoImage(resized_image4)
label4=Label(frame_menu, image=photo4)
label4.image=photo4
label4.place(relx=0.184, rely=0.590)

Bt_S= Button(frame_menu,text = "Shop",font="Arial 12 bold",borderwidth=4).place(relx=0.35,rely =0.030)
Btn_L = Button(frame_menu,text="Library",font="Arial 12 bold",borderwidth=4).place(relx=0.45,rely=0.030)
Btn_A = Button(frame_menu,text="Account",font="Arial 12 bold",borderwidth=4,command=enter_account).place(relx=0.55,rely=0.030)
Btn_E = Button(frame_menu,text="Exit",font="Arial 12 bold",borderwidth=4).place(relx=0.65,rely=0.030)
btn = Button(frame_menu,text= "click",command = main_menu)
btn.place(relx=0.56,rely=0.5)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

=======
>>>>>>> 8632e7a41d913d049df16c54482f8af071ecb76d
root.mainloop()
