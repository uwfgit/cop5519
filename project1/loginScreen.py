from tkinter import *
import tkinter as tk
from tkinter import messagebox
from db import db
from mainScreen import MainScreen
from utlis.position import RootPosition
from db import check_login_to


class LoginScreen:

    def __init__(self, rt):
        self.root = rt
        RootPosition(self.root, 'Login Page', 420, 460)

        self.username = tk.StringVar()
        self.password = tk.StringVar()

        self.page = tk.Frame(self.root)
        self.page.pack()

        self.msg = "Welcome to the Fv Calculator"
        self.img = tk.PhotoImage(file="""./assets/argie-winking_200px_NEW.gif""")
        self.logo = tk.Label(self.page, text=self.msg, image=self.img, compound="bottom", pady=30)
        self.logo.grid(row=0, columnspan=2)

        # tk.Label(page).grid(row=0, column=0)

        tk.Label(self.page, text='Username', width=10).grid(row=2, column=0)
        tk.Entry(self.page, textvariable=self.username, width=25).grid(row=2, column=1)

        tk.Label(self.page, text='Password').grid(row=3, column=0, pady=10)
        tk.Entry(self.page, textvariable=self.password, width=25, show='*').grid(row=3, column=1)
        tk.Button(self.page, text='Login', command=self.login).grid(row=4, column=0, pady=10, sticky=S)
        tk.Button(self.page, text='Quit', command=self.page.quit).grid(row=4, column=1, sticky=E)

    def login(self):
        name = self.username.get()
        pwd = self.password.get()
        flag, message = db.check_login(name, pwd)
        if flag:
            self.page.destroy()
            MainScreen(self.root)
            print('Login Successfully')
        else:
            messagebox.showwarning(title='Warning', message=message)

    # TODO:增加装饰
    @check_login_to
    def login_to(self):
        self.page.destroy()
        MainScreen(self.root)
        print('Login Successfully')


if __name__ == '__main__':
    root = tk.Tk()
    LoginScreen(rt=root)
    root.resizable(False, False)
    root.mainloop()
