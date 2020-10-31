from luhn import *
import tkinter as tk
from tkinter import messagebox
import tkinter.filedialog
import os
import re


class TkinterClass:
    def __init__(self):

        root = tk.Tk()
        root.title('LuhnCheckdigit-numbering')
        root.geometry("525x550")

        # 入力欄の作成
        label1 = tk.Label(root, text='入力', font=('', 20))
        label1.place(x=40, y=100)

        self.input_box = tk.Entry(width=17, font=('', 20))
        self.input_box.place(x=220, y=100)

        # チェックデジットラベル
        label2 = tk.Label(root, text='チェックデジット', font=('', 20))
        label2.place(x=40, y=200)

        # チェックデジット表示
        self.check_box = tk.Entry(width=17, font=('', 20))
        self.check_box.place(x=220, y=200)

        # 出力欄の作成
        label3 = tk.Label(root, text='16桁番号', font=('', 20))
        label3.place(x=40, y=300)

        self.out_box = tk.Entry(width=17, font=('', 20))
        self.out_box.place(x=220, y=300)

        button = tk.Button(root, text='実行', font=('', 20),
                           width=24, height=1, bg='#999999', activebackground="#aaaaaa")
        button.bind('<ButtonPress>', self.button_click)
        button.place(x=70, y=400)

        root.mainloop()


    def button_click(self, event):
        input_value = self.input_box.get()

        if len(input_value) != 15:
            messagebox.showerror("ERROR", "桁数が間違ってます")
        elif re.search("[0-9]{15}", input_value) is None:
            messagebox.showerror("ERROR", "数値以外が入力されてます")
        else:
            output_checkdigit_value = generate(input_value)
            output_total_vale = append(input_value)

            # チェックデジット
            self.check_box.delete(0, tk.END)
            self.check_box.insert(tk.END, output_checkdigit_value)

            # 16桁番号の結果
            self.out_box.delete(0, tk.END)
            self.out_box.insert(tk.END, output_total_vale)


if __name__ == '__main__':
    TkinterClass()
