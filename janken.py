import tkinter as tk

root = tk.Tk()

#ウィンドウ定義

root.title("じゃんけんゲーム")
root.minsize(800,400)
root.config(cursor = 'hand2')

#中身
##画像表示
frame0 = tk.Frame(root)
canvas = tk.Canvas(frame0,bg = "white",width = 800, height = 492).place(x=0,y=0)
img = tk.PhotoImage(file="janken.png")
canvas.create_image(0,0,image = img,anchor = tk.NW)
frame0.pack()

frame1 = tk.Frame(root)
label1 = tk.Label(frame1,text = "私とじゃんけんをしましょう！").pack()
label2 = tk.Label(frame1,text = "最初はグー！じゃんけん・・・").pack()
frame1.pack()

frame2 = tk.Frame(root)
button1 = tk.Button(frame2,text  = "グー").grid(row = 4, column=0)
button2 = tk.Button(frame2,text = "チョキ").grid(row = 4, column = 1)
button3 = tk.Button(frame2,text = "パー").grid(row = 4, column = 2)
frame2.pack()

root.mainloop()