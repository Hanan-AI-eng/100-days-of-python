from tkinter import *
from tkinter import messagebox
import random
import pyperclip

FONT="Arial",10,"bold"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_generator():

    #Password Generator Project

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letter=[random.choice(letters) for _ in range(nr_letters)]
    symbol=[random.choice(symbols) for _ in range(nr_symbols)]
    num=[random.choice(numbers) for _ in range(nr_numbers)]
    password_list = letter+symbol+num
    random.shuffle(password_list)

    password="".join(password_list)

    password_Entry.delete(0,END)
    password_Entry.insert(0,password)
    pyperclip.copy(password_Entry.get())


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if len(website_Entry.get())==0 or len(password_Entry.get())==0:
        messagebox.showwarning(title="Oops",message="Please don't leave any fields empty! ")
    else:

        is_ok=messagebox.askokcancel(title=website_Entry.get(),message=f"Theses are the details entered: \nEmail: {email_Entry.get()} \nPassword: {password_Entry.get()} \n Is it okay to save?")
        if is_ok:
            with open("data.txt","a") as f:
                f.write(f"{website_Entry.get()} | {email_Entry.get()} | {password_Entry.get()}\n")
            website_Entry.delete(0,END)
            password_Entry.delete(0,END)



# ---------------------------- UI SETUP ------------------------------- #

# use a windo
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

# image
canvas=Canvas(width=200, height=200)
key_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=key_img)
canvas.grid(column=1,row=0)

# labels
website_label=Label(text="Website:",font=FONT)
website_label.grid(column=0,row=1)

email_label=Label(text="Email/Username:",font=FONT)
email_label.grid(column=0,row=2)

password_label=Label(text="Password",font=FONT)
password_label.grid(column=0,row=3)

#Entry
website_Entry=Entry(width=35)
website_Entry.grid(column=1,row=1,columnspan=2)
website_Entry.focus()

email_Entry=Entry(width=35)
email_Entry.insert(0,"1234@gmail.com")
email_Entry.grid(column=1,row=2,columnspan=2)


password_Entry=Entry(width=21)
password_Entry.grid(column=1,row=3)

#button
Add_button=Button(width=30,text="Add",command=save)
Add_button.grid(column=1,row=4,columnspan=2)

generate_password_button=Button(text="Generate Password",command=pass_generator)
generate_password_button.grid(column=2,row=3)




window.mainloop()
