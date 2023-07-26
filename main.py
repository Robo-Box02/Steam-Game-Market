from tkinter import*
from PIL import Image, ImageTk
from tkinter.messagebox import *
import json
root = Tk()
root.title("Steam")
root.geometry('1920x1080')
#Frame Menyu
frame_menu = Frame(root,width = 1920,height = 1080,bg = '#0f1948')
frame_menu.place(x=1,y=1)
#Frame Login
frame_login = Frame(root,width=1920,height=1080)
frame_login.config(background="#0f1948")
#Frame Registratiom
frame_registration = Frame(root,width = 1920,height = 1080,bg = '#0f1948')
frame_registration.config(background="#0f1948")
#Frame Account Info
frame_acc_info = Frame(root,width=1920,height=1080,bg="#0f1948")
frame_acc_info.config(background="#0f1948")




def main_menu():
    frame_menu.place_forget()
    root.geometry('1920x1080')
    frame_login.place(relx=0,rely=0.1)
    frame_menu.pack()

def Registration():
    frame_login.place_forget()
    frame_registration.place(relx=0,rely=0)


def back_to_menyu():
    with open("Files/son.json","r")as FileHandler:
        users = json.loads(FileHandler.readline())
    for i in users:
        if i ["login"] == entry1.get() and i["password"] == entry2.get():
            frame_login.place_forget()
            frame_menu.place(relx=0, rely=0)
            user={
                "login": i["login"],
                "password": i ["password"],
                "gmail": i ["gmail"]
            }
            acc_open(user)
def acc_open(user):


    Login_lbl = Label(frame_menu,text =user["login"],font= "Arial 14 bold",bg="#0f1948",fg="White")
    Login_lbl.place(relx=0.6,rely=0.15)





def register():
    if "@gmail.com" in entry_G.get():
        print(entry_G.get())
    else:
        showerror("Error", "Пожалуйста добавьте маил")
    if len(entry_P.get()) > 8:
        print(entry_P.get())
    else:
        showerror("Error","Колличество символов должно быть больше 8")
    if entry_CP.get() == entry_P.get():
        print(entry_CP.get())
    else:
        showerror("Error", "Пароль не совпадают")

    user={
        "gmail":entry_G.get(),
        "login":entry_L.get(),
        "password":entry_P.get()
    }

    with open("Files/son.json","r")as FileHandler:
        users=json.loads(FileHandler.readline())

    users.append(user)

    with open("Files/son.json","w")as FileHandler:
        json.dump(users,FileHandler)
    frame_registration.place_forget()
    frame_login.place(relx=0,rely=0)

#Registration Board
lbl_G = Label(frame_registration,text = "GMAIL",font= "Arial 14 bold",bg="#0f1948",fg="Yellow")
lbl_G.place(relx=0.440,rely=0.200)
entry_G = Entry(frame_registration,font="Arial 14 bold")
entry_G.place(relx=0.440,rely=0.225,height=30)
lbl_L = Label(frame_registration,text = "LOGIN",font= "Arial 14 bold",bg="#0f1948",fg="Yellow")
lbl_L.place(relx=0.440,rely=0.255)
entry_L = Entry(frame_registration,font="Arial 14 bold")
entry_L.place(relx=0.440,rely=0.280)
lbl_P = Label(frame_registration,text="PASSWORD",font= "Arial 14 bold",bg="#0f1948",fg="Yellow")
lbl_P.place(relx=0.440,rely=0.310)
entry_P = Entry(frame_registration,font="Arial 14 bold")
entry_P.place(relx=0.440,rely=0.335)
lbl_CP = Label(frame_registration,text="CONFIRM PASSWORD",font= "Arial 14 bold",bg="#0f1948",fg="Yellow")
lbl_CP.place(relx=0.440,rely=0.360)
entry_CP = Entry(frame_registration,font="Arial 14 bold")
entry_CP.place(relx=0.440,rely=0.385)
btn = Button(frame_registration,text="Press for Registration",width=15,height=2,command=register)
btn.place(relx=0.465,rely=0.415)

def enter_account():
    frame_menu.place_forget()
    frame_login.place(relx=0,rely=0)

def switch():
    if int_var.get() == 1:
         entry2 ['show'] = '*'
    else:
         entry2 ['show'] = ''

def clear():
    entry2.delete(0,'end')
    entry1. delete(0,'end')

def Photo0():
    ...

def Login():
    if entry1.get() == entry_L.get():
        print("OK")
    else:
        showerror("Error","Логин не верный, пожалуйста повторите попытку")
    if entry2.get() == entry_P.get():
        print("OK")
    else:
        showerror("Error","Пороль введен не правельно, пожалуйста повторите попытку")



#Вход в Магазин
lbl1 = Label(frame_login,text="Login",font="Arial 14 bold",bg="#0f1948",fg="Yellow")
lbl1.place(relx=0.480,rely=0.390)
entry1 = Entry(frame_login,font= "Arial 14")
entry1.place(relx=0.455,rely=0.415,height=20)
entry1.config(width=15)

lbl2 = Label(frame_login,text="Password",font="Arial 14 bold",bg="#0f1948",fg="Yellow")
lbl2.place(relx=0.470,rely=0.440)
entry2 = Entry(frame_login,font= "Arial 14")
entry2.place(relx=0.455,rely=0.465,height=20)
entry2.config(width=15)
# Вход в мазазин
btn1 = Button(frame_login,text="Registration",font="Arial 12 bold",bg="Yellow",command=Registration)
btn1.place(relx=0.455,rely=0.490)
btn2 = Button(frame_login,text = "Enter",font="Arial 12 bold",bg= "Yellow",command=back_to_menyu)
btn2.place(relx=0.515,rely=0.490)

int_var = IntVar()
check_btn = Checkbutton(frame_login, text='Switch states', variable=int_var, command=switch, font="Arial 10 bold", width=10,fg="Black")
check_btn.place(relx=0.470, rely=0.530)

# Список с играми
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
label0.bind("<Enter>")
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

# Виджеты для переходов страниц
Bt_Shop= Button(frame_menu,text = "Shop",font="Arial 12 bold",borderwidth=4).place(relx=0.35,rely =0.030)
Btn_Library = Button(frame_menu,text="Library",font="Arial 12 bold",borderwidth=4).place(relx=0.45,rely=0.030)
Btn_Account = Button(frame_menu,text="Account",font="Arial 12 bold",borderwidth=4,command=enter_account).place(relx=0.55,rely=0.030)
Btn_Exit = Button(frame_menu,text="Exit",font="Arial 12 bold",borderwidth=4).place(relx=0.65,rely=0.030)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
root.mainloop()

isLogined = False