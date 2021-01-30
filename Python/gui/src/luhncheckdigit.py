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

        # メニューバーの作成
        menubar = tk.Menu(root)
        root.configure(menu=menubar)
        # ファイルメニュー
        filemenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Menu", menu=filemenu)
        # 終了
        filemenu.add_command(label="Exit", command=lambda: root.destroy())

        # 入力欄ラベル
        label1 = tk.Label(root, text='15桁番号入力', font=('', 20))
        label1.place(x=40, y=100)

        # 入力欄の表示
        self.input_box = tk.Entry(width=17, font=('', 20))
        self.input_box.place(x=220, y=100)

        # チェックデジット欄ラベル
        label2 = tk.Label(root, text='チェックデジット', font=('', 20))
        label2.place(x=40, y=200)

        # チェックデジット欄の表示
        self.check_box = tk.Entry(width=17, font=('', 20))
        self.check_box.place(x=220, y=200)

        # 出力欄ラベル
        label3 = tk.Label(root, text='16桁番号', font=('', 20))
        label3.place(x=40, y=300)

        # 出力欄の表示
        self.out_box = tk.Entry(width=17, font=('', 20))
        self.out_box.place(x=220, y=300)

        button = tk.Button(root, text='実行', font=('', 20),
                           width=24, height=1, bg='#999999', activebackground="#aaaaaa")
        button.bind('<ButtonPress>', self.button_click)
        button.place(x=70, y=400)

        root.mainloop()

    """Sumary
    実行ボタン押下

    Parameters
    ----------
    event : tkinter.Event
    
    """

    def button_click(self, event):
        input_value = self.input_box.get()
        # 入力データの確認
        if len(input_value) != 15:
            messagebox.showerror("ERROR", "桁数が間違ってます")
        elif re.search("[0-9]{15}", input_value) is None:
            messagebox.showerror("ERROR", "数値以外が入力されてます")
        else:
            # チェックデジットの値を取得
            total_value = self.check_digit(input_value)
            output_checkdigit_value = total_value[0]
            output_total_vale = total_value[1]

            # チェックデジット結果出力
            self.check_box.delete(0, tk.END)
            self.check_box.insert(tk.END, output_checkdigit_value)

            # 16桁番号の結果出力
            self.out_box.delete(0, tk.END)
            self.out_box.insert(tk.END, output_total_vale)

    """Sumary
    チェックデジットの値を取得する

    Parameters
    ----------
    input_value : int
        対象の入力データ

    Returns
    -------
    output_checkdigit : int
        対象のチェックデジット
    output_total_value : int
        対象の入力データとチェックデジットをアペンドした情報
    """

    def check_digit(self, input_value):
        # チェックデジットの生成
        output_checkdigit_value = generate(input_value)
        # inputにチェックデジットを生成
        output_total_vale = append(input_value)
        return output_checkdigit_value, output_total_vale


if __name__ == '__main__':
    TkinterClass()
