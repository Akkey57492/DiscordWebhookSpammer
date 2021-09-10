import requests
import json
import tkinter as tk
import tkinter.messagebox as tmb
import tkinter
from tkinter import messagebox


root = tk.Tk()

# Entry 4
#入力欄の作成
input_box = tkinter.Entry(width=40)
input_box.place(x=10, y=100)

#ラベルの作成
input_label = tkinter.Label(text="WebHookURL:")
input_label.place(x=10, y=70)

#ボタンがクリックされたら実行
def button_click():
 # input_value = input_box.get()
  while True:
      data = {
		"content": f"@everyone",
		"username": f"率直BOT"
      }
      requests.post(input_box.get(), data=data)

#ボタンの作成
button = tkinter.Button(text="実行",command=button_click)
button.place(x=10, y=130)

                    

root.title("WebHookSpamGUI")
root.mainloop()
