import tkinter as tk
from tkinter import messagebox as mb
import random

root = tk.Tk()

#ウィンドウ定義

root.title("じゃんけんゲーム")
root.minsize(800,400)
root.config(cursor = 'hand2')

#中身
frame1 = tk.Frame(root)
label1 = tk.Label(frame1,text = "私とじゃんけんをしましょう！").pack()
label2 = tk.Label(frame1,text = "最初はグー！じゃんけん・・・").pack()
frame1.pack()

#ランダムにじゃんけんの手を指定
janken_list = ["グー","チョキ","パー"]
versus = random.choice(janken_list)

#じゃんけんのルール

win = 0
lose = 0

def button1_click():
    if versus == "グー":
        mb.showinfo("じゃんけん結果","私は" + versus + "をだしました。あいこですね。")
    elif versus == "チョキ":
        win = win + 1
        mb.showinfo("じゃんけん結果","私は" + versus + "を出しました。あなたの勝ちです")
    else :
        mb.showinfo("じゃんけん結果","私は" + versus + "をだしました。私の勝ちですね。")
        lose = lose + 1
def button2_click():
    if versus == "チョキ":
        mb.showinfo("じゃんけん結果","私は" + versus + "をだしました。あいこですね。")
    elif versus == "パー":
        win = win + 1
        mb.showinfo("じゃんけん結果","私は" + versus + "を出しました。あなたの勝ちです")
    else :
        lose = lose + 1
        mb.showinfo("じゃんけん結果","私は" + versus + "をだしました。私の勝ちですね。")
def button3_click():
    if versus == "パー":
        win = win + 1
        mb.showinfo("じゃんけん結果","私は" + versus + "をだしました。あいこですね。")
    elif versus == "グー":
        mb.showinfo("じゃんけん結果","私は" + versus + "を出しました。あなたの勝ちです")
    else :
        lose = lose + 1
        mb.showinfo("じゃんけん結果","私は" + versus + "をだしました。私の勝ちですね。")

frame2 = tk.Frame(root)
button1 = tk.Button(frame2,text  = "グー", command = button1_click).grid(row = 4, column=0)
button2 = tk.Button(frame2,text = "チョキ", command = button2_click).grid(row = 4, column = 1)
button3 = tk.Button(frame2,text = "パー", command = button3_click).grid(row = 4, column = 2)
frame2.pack()

root.mainloop()