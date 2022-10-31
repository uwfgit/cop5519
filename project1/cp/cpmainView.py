import tkinter as tk
from tkinter import *
from db import db


# ResultFrame 类继承 tk.Frame
class EntryFrame(tk.Frame):
    # tk.Frame 的参数是要求传入 root 参数的
    def __init__(self, root):  # ①这是子类自己的 init 函数
        super().__init__(root)  # ②子类继承父类的 init 函数
        # 问题框架
        self.finalTotal = None
        self.numOY = None
        self.interestR = None
        self.pmtEr = None
        self.pmtE = None
        self.initialA = None
        self.f1 = tk.Frame(root, width=300, height=370)
        self.f1.place(x=60, y=50)
        # 答案框架
        # self.f2 = tk.Frame(root, borderwidth=2, border=2, highlightbackground="black", highlightthickness=1, width=300,height=370)
        self.f2 = tk.Frame(root)
        self.f2.place(x=450, y=60)

        # 按键 Frame
        # self.f3 = tk.Frame(root, highlightbackground="black", highlightthickness=1)
        self.f3 = tk.Frame(root)
        self.f3.place(x=570, y=430)

        # 存储变量
        self.name = tk.StringVar()
        self.initialAmount = tk.StringVar()
        self.pmtEmpee = tk.StringVar()
        self.pmtEmper = tk.StringVar()
        self.interestRate = tk.StringVar()
        self.numOfYears = tk.StringVar()
        self.total = tk.StringVar()
        self.status = tk.StringVar()
        self.create_page()
        # self.show_result_live()

    # 创建显示页面
    def create_page(self):
        tk.Label(self.f1).grid(row=0, pady=10)
        tk.Label(self.f1, text='Name').grid(row=1, column=1, pady=15, sticky=W)
        tk.Entry(self.f1, textvariable=self.name).grid(row=1, column=2)

        tk.Label(self.f1, text='Initial Amount').grid(row=2, column=1, pady=15, sticky=W)
        tk.Entry(self.f1, textvariable=self.initialAmount).grid(row=2, column=2)

        tk.Label(self.f1, text='Employee Payment').grid(row=3, column=1, pady=15, sticky=W)
        tk.Entry(self.f1, textvariable=self.pmtEmpee).grid(row=3, column=2)

        tk.Label(self.f1, text='Employer Payment').grid(row=4, column=1, pady=15, sticky=W)
        tk.Entry(self.f1, textvariable=self.pmtEmper).grid(row=4, column=2)

        tk.Label(self.f1, text='Interest Rate').grid(row=5, column=1, pady=15, sticky=W)
        tk.Entry(self.f1, textvariable=self.interestRate).grid(row=5, column=2)

        tk.Label(self.f1, text='Numbers of Years').grid(row=6, column=1, pady=15, sticky=W)
        tk.Entry(self.f1, textvariable=self.numOfYears).grid(row=6, column=2)

        # 提示成功
        tk.Label(self.f1, textvariable=self.status).grid(row=7, column=2)

        # tk.Label(self.f1, text='Total').grid(row=7, column=1, pady=15, sticky=W)
        tk.Button(self.f3, text='Calculate', command=self.show_result_final, border=0, borderwidth=0).grid(row=0,
                                                                                                           padx=10)
        tk.Button(self.f3, text='Export', border=0, borderwidth=0).grid(row=0, column=1)

    # 实时显示
    def show_result_live(self):
        tk.Label(self.f2).grid(row=0, pady=10)
        tk.Label(self.f2, textvariable=self.name).grid(row=1, column=1, sticky=W)
        tk.Label(self.f2, textvariable=self.initialAmount).grid(row=2, column=1, sticky=W)
        tk.Label(self.f2, textvariable=self.pmtEmper).grid(row=4, column=1, sticky=W)
        tk.Label(self.f2, textvariable=self.pmtEmpee).grid(row=3, column=1, sticky=W)
        tk.Label(self.f2, textvariable=self.interestRate).grid(row=5, column=1, sticky=W)
        tk.Label(self.f2, textvariable=self.numOfYears).grid(row=6, column=1, sticky=W)

    def show_result_final(self):
        # 在 frame 2 中显示
        tk.Label(self.f2).grid(row=0, pady=10)
        tk.Label(self.f2, text=self.name.get()).grid(row=1, column=1, sticky=W)
        tk.Label(self.f2, text='The initialAmount: $' + self.initialAmount.get()).grid(row=2, column=1, sticky=W)
        tk.Label(self.f2, text='Recurring monthly payments (employer): $' + self.pmtEmper.get()).grid(row=3, column=1,
                                                                                                      sticky=W)
        tk.Label(self.f2, text='Recurring monthly Payments (employee): $' + self.pmtEmpee.get()).grid(row=4, column=1,
                                                                                                      sticky=W)
        tk.Label(self.f2, text='Interest rate: ' + self.interestRate.get() + '%').grid(row=5, column=1, sticky=W)
        tk.Label(self.f2, text='Total number of years: ' + self.numOfYears.get()).grid(row=6, column=1, sticky=W)

        self.status.set('Successfully submitted')
        self.calculation()
        # tk.Label(self.f2, textvariable=self.total).grid(row=7, column=1, sticky=W)
        tk.Label(self.f2, text='Total amount: $' + self.total.get()).grid(row=7, column=1, sticky=W)

        # 如果要保存数据的话这里清空位置很重要
        self.name.set('')
        self.initialAmount.set('')
        self.pmtEmper.set('')
        self.pmtEmpee.set('')
        self.interestRate.set('')
        self.numOfYears.set('')

    def record_info(self):
        consumer_info = {"name": self.name.get(), "initial amount": self.initialAmount.get(),
                         "recurring monthly payments (employer)": self.pmtEmper.get(),
                         "recurring monthly Payments (employee)": self.pmtEmpee.get(),
                         "interest rate": str(self.interestRate.get()),
                         "total number of years": self.numOfYears.get(),
                         "total amount": self.total.get()}
        db.insert_records(consumer_info)
        db.write_into()

    def calculation(self):
        self.initialA = int(self.initialAmount.get())
        self.pmtE = int(self.pmtEmper.get())
        self.pmtEr = int(self.pmtEmpee.get())
        self.interestR = float(self.interestRate.get()) / 100
        self.numOY = int(self.numOfYears.get())
        self.finalTotal = (self.initialA + self.pmtE + self.pmtEr) * self.interestR * self.numOY
        # self.total.set('Total Amount $' + str(round(self.finalTotal, 2)))
        self.total.set(str(round(self.finalTotal, 2)))
        self.record_info()
        # tk.Label(self.f2, text='$' + str(self.total.get())).grid(row=7, column=1, sticky=W)
        # tk.Label(self.f2, textvariable=self.total).grid(row=7, column=1, sticky=W)
