from tkinter import *
from tkinter import messagebox

# Diccionario para almacenar usuarios registrados (nombre: contraseña)
users = {}

# Función para abrir la ventana de registro
def open_registration_form():
    register_window = Toplevel(base)
    register_window.geometry('500x500')
    register_window.title("Registration Form")

    labl_0 = Label(register_window, text="Registration form", width=20, font=("bold", 20))
    labl_0.place(x=90, y=53)

    labl_1 = Label(register_window, text="Username", width=20, font=("bold", 10))
    labl_1.place(x=80, y=130)

    entry_1 = Entry(register_window)
    entry_1.place(x=240, y=130)

    labl_2 = Label(register_window, text="Email", width=20, font=("bold", 10))
    labl_2.place(x=68, y=180)

    entry_02 = Entry(register_window)
    entry_02.place(x=240, y=180)

    labl_3 = Label(register_window, text="Gender", width=20, font=("bold", 10))
    labl_3.place(x=70, y=230)

    varblbl = IntVar()
    Radiobutton(register_window, text="Male", padx=5, variable=varblbl, value=1).place(x=235, y=230)
    Radiobutton(register_window, text="Female", padx=20, variable=varblbl, value=2).place(x=290, y=230)

    labl_4 = Label(register_window, text="Age:", width=20, font=("bold", 10))
    labl_4.place(x=70, y=280)

    entry_03 = Entry(register_window)
    entry_03.place(x=240, y=280)

    labl_5 = Label(register_window, text="Password", width=20, font=("bold", 10))
    labl_5.place(x=68, y=330)

    entry_04 = Entry(register_window, show='*')
    entry_04.place(x=240, y=330)

    def submit_action():
        Username = entry_1.get()
        email = entry_02.get()
        gender = 'Male' if varblbl.get() == 1 else 'Female'
        age = entry_03.get()
        password = entry_04.get()

        if Username and email and password:  # Check if all fields are filled
            # Aquí puedes agregar la lógica para registrar al usuario, por ejemplo, guardarlo en una base de datos
            users[Username] = password  # Guarda el usuario y la contraseña en el diccionario
            print(f"Username: {Username}")
            print(f"Email: {email}")
            print(f"Gender: {gender}")
            print(f"Age: {age}")
            print(f"Password: {password}")

            messagebox.showinfo("Success", "Registration successful")
            register_window.destroy()  # Cierra la ventana de registro
        else:
            messagebox.showerror("Error", "Please fill all fields")

    Button(register_window, text='Submit', width=20, bg='brown', fg='white', command=submit_action).place(x=180, y=380)

# Función para manejar el inicio de sesión
def login_action():
    username = entry_username.get()
    password = entry_password.get()

    if username in users and users[username] == password:
        messagebox.showinfo("Success", "Login successful")
        print(f"Username: {username} logged in successfully")
        base.destroy()  # Cierra la ventana de inicio de sesión
    else:
        messagebox.showerror("Error", "Invalid username or password")

base = Tk()
base.geometry('400x300')
base.title("Login Form")

Label(base, text="Login", width=20, font=("bold", 20)).pack(pady=20)

Label(base, text="Username", width=20, font=("bold", 10)).pack(pady=5)
entry_username = Entry(base)
entry_username.pack()

Label(base, text="Password", width=20, font=("bold", 10)).pack(pady=5)
entry_password = Entry(base, show='*')
entry_password.pack()

Button(base, text='Login', width=20, bg='brown', fg='white', command=login_action).pack(pady=20)
Button(base, text='Register', width=20, bg='blue', fg='white', command=open_registration_form).pack()

base.mainloop()
