import tkinter as tk
from tkinter import *
from db import db
from enum import Enum
import numpy_financial as npf


class EntryFrame(tk.Frame):
    # tk.Frame 的参数是要求传入 root 参数的
    def __init__(self, root):
        super().__init__(root)
        # 问题框架
        self.interestR = None
        self.comFrequency = None
        self.numOY = None
        self.totalMonthlyPmt = None
        self.initialA = None
        self.futureValue = None
        self.inRateDict = {0: "8", 1: "10"}
        self.numYrDict = {0: "10", 1: "20"}
        self.f1 = tk.Frame(root, width=300, height=370)
        self.f1.place(x=60, y=50)
        self.f2 = tk.Frame(root)
        self.f2.place(x=450, y=60)
        self.f3 = tk.Frame(root)
        self.f3.place(x=570, y=430)
        self.optionVarI = IntVar()
        self.optionVarI.set(0)
        self.optionVarY = IntVar()
        self.optionVarY.set(0)

        # 存储变量
        self.name = tk.StringVar()
        self.initialAmount = tk.StringVar()
        self.pmtEmpeeMonthly = tk.StringVar()
        self.pmtEmperMonthly = tk.StringVar()
        self.interestRate = tk.StringVar()
        self.numOfYears = tk.StringVar()
        self.finalFutureValue = tk.StringVar()
        self.status = tk.StringVar()
        self.create_page()

    def radio_button_option(self, options: dict, option_var, x, y):
        i = 0
        for idx, option in options.items():
            Radiobutton(self.f1, text=option, variable=option_var, value=idx).place(x=x + i, y=y)
            i += 100

    def optionSelection(self):
        tk.Label(self.f2, text='Interest rate: ' + self.inRateDict[self.optionVarI.get()] + '%').grid(row=5, column=1, sticky=W)
        print(self.inRateDict[self.optionVarI.get()])
        print(self.numYrDict[self.optionVarY.get()])

    def create_page(self):
        tk.Label(self.f1).grid(row=0, pady=10)
        tk.Label(self.f1, text='Name').grid(row=1, column=1, pady=15, sticky=W)
        tk.Entry(self.f1, textvariable=self.name).grid(row=1, column=2)
        tk.Label(self.f1, text='Initial Amount').grid(row=2, column=1, pady=15, sticky=W)
        tk.Entry(self.f1, textvariable=self.initialAmount).grid(row=2, column=2)
        tk.Label(self.f1, text='Mo. payments EMPL').grid(row=3, column=1, pady=15, sticky=W)
        tk.Entry(self.f1, textvariable=self.pmtEmperMonthly).grid(row=3, column=2)
        tk.Label(self.f1, text='Mo. Payments EMP').grid(row=4, column=1, pady=15, sticky=W)
        tk.Entry(self.f1, textvariable=self.pmtEmpeeMonthly).grid(row=4, column=2)
        tk.Label(self.f1, text='Total Mo. PMT').grid(row=5, column=1, pady=15, sticky=W)
        tk.Label(self.f1, text='12 months').grid(row=5, column=2, pady=15, sticky=N)
        tk.Label(self.f1, text='Interest Rate %').grid(row=6, column=1, pady=15, sticky=W)
        self.radio_button_option(self.inRateDict, self.optionVarI, 155, 315)
        tk.Label(self.f1, text='Numbers of Years').grid(row=7, column=1, pady=15, sticky=W)
        self.radio_button_option(self.numYrDict, self.optionVarY, 155, 366)
        tk.Label(self.f1, textvariable=self.status).grid(row=8, column=2, pady=15)
        tk.Button(self.f3, text='Calculate', command=self.show_result_final, border=0, borderwidth=0).grid(row=0, padx=20, pady=40)

    def show_result_live(self):
        tk.Label(self.f2).grid(row=0, pady=10)
        tk.Label(self.f2, textvariable=self.name).grid(row=1, column=1, sticky=W)
        tk.Label(self.f2, textvariable=self.initialAmount).grid(row=2, column=1, sticky=W)
        tk.Label(self.f2, textvariable=self.pmtEmperMonthly).grid(row=4, column=1, sticky=W)
        tk.Label(self.f2, textvariable=self.pmtEmpeeMonthly).grid(row=3, column=1, sticky=W)
        tk.Label(self.f2, textvariable=self.interestRate).grid(row=5, column=1, sticky=W)
        tk.Label(self.f2, textvariable=self.numOfYears).grid(row=6, column=1, sticky=W)

    def show_result_final(self):
        # 在 frame 2 中显示
        tk.Label(self.f2).grid(row=0, pady=10)
        tk.Label(self.f2, text=self.name.get()).grid(row=1, column=1, sticky=W)
        tk.Label(self.f2, text='The initialAmount: $' + self.initialAmount.get()).grid(row=2, column=1, sticky=W)
        tk.Label(self.f2, text='Recurring monthly payments (employer): $' + self.pmtEmperMonthly.get()).grid(row=3, column=1, sticky=W)
        tk.Label(self.f2, text='Recurring monthly Payments (employee): $' + self.pmtEmpeeMonthly.get()).grid(row=4, column=1, sticky=W)
        tk.Label(self.f2, text='Total recurring monthly payments: $' + str('%.2f' % ((float(self.pmtEmperMonthly.get()) + float(self.pmtEmpeeMonthly.get())) * 12))).grid(row=5, column=1, sticky=W)
        tk.Label(self.f2, text='Interest rate: ' + str(float(self.inRateDict[self.optionVarI.get()]) / 100)).grid(row=6, column=1, sticky=W)
        tk.Label(self.f2, text='Total number of years: ' + self.numYrDict[self.optionVarY.get()]).grid(row=7, column=1, sticky=W)
        self.status.set('Successfully submitted')
        self.calculation()
        tk.Label(self.f2, text='Future Value: $' + self.finalFutureValue.get()).grid(row=8, column=1, sticky=W)
        # self.name.set('')
        # self.initialAmount.set('')
        # self.pmtEmperMonthly.set('')
        # self.pmtEmpeeMonthly.set('')

    def record_info(self):
        consumer_info = {"name": self.name.get(),
                         "initial amount": self.initialAmount.get(),
                         "recurring monthly payments (employer)": self.pmtEmperMonthly.get(),
                         "recurring monthly Payments (employee)": self.pmtEmpeeMonthly.get(),
                         "interest rate": str(float(self.inRateDict[self.optionVarI.get()]) / 100),
                         "total number of years": self.numYrDict[self.optionVarY.get()],
                         "future value": self.finalFutureValue.get()}
        db.insert_records(consumer_info)
        db.write_into()

    def calculation(self):
        self.interestR = float(self.inRateDict[self.optionVarI.get()]) / 100
        self.comFrequency = 12
        self.numOY = self.numYrDict[self.optionVarY.get()]
        self.totalMonthlyPmt = '%.2f' % ((float(self.pmtEmperMonthly.get()) + float(self.pmtEmpeeMonthly.get())) * 12)
        self.initialA = float(self.initialAmount.get())
        # FIXME: need to get the right function
        self.futureValue = npf.irr([self.interestR / self.comFrequency, self.numOY * self.comFrequency, self.totalMonthlyPmt, self.initialA])
        self.finalFutureValue.set(str(round(self.futureValue, 2)))
        self.record_info()
