from luhn import *
import tkinter as tk
from tkinter import messagebox
import tkinter.filedialog
import os


class TkinterClass:
    def __init__(self):

        root = tkinter.Tk()
        root.title('LuhnCheckdigit-numbering')
        root.geometry("600x600")

        # コンソールに"Button is clicked."を出力する関数
        # button = tk.Button(root, text='ファイルダイアログを開く', font=('', 20),
        #                    width=24, height=1, bg='#999999', activebackground="#aaaaaa")
        # button.bind('<ButtonPress>', self.file_dialog)
        # button.pack(pady=40)

        # self.file_name = tk.StringVar()
        # self.file_name.set('未選択です')
        # label = tk.Label(textvariable=self.file_name, font=('', 12))
        # label.pack(pady=0)

        # 入力欄の作成
        self.input_box = tkinter.Entry(width=24)
        self.input_box.pack(pady=40)

        # ボタンの作成（text=ボタンに表示されるテキスト, command=押下時に呼び出す関数）
        button = tk.Button(root, text='実行', font=('', 20),
                           width=24, height=1, bg='#999999', activebackground="#aaaaaa")
        button.bind('<ButtonPress>', self.button_click)
        button.pack(pady=40)

        # ボタンの表示
        # button.grid()

        root.mainloop()

    # def file_dialog(self, event):
    #     fTyp = [("", "*")]
    #     iDir = os.path.abspath(os.path.dirname(__file__))
    #     file_name = tk.filedialog.askopenfilename(
    #         filetypes=fTyp, initialdir=iDir)
    #     if len(file_name) == 0:
    #         self.file_name.set('選択をキャンセルしました')
    #     else:
    #         self.file_name.set(file_name)

    def button_click(self, event):
        input_value = self.input_box.get()
        output_value = append(input_value)
        messagebox.showinfo("結果", output_value + "が入力されました。")


if __name__ == '__main__':
    TkinterClass()
