from funciones import *
from tkinter import *
#----------------Graffic2--------------
def Raiz2():
	global draw_list
	raiz2=Tk()
	raiz2.title("Drow numbers")
	raiz2.iconbitmap("hola.ico")
	raiz2.resizable(0,0)
	if len(draw_list) > 5:
		Frame(raiz2, height="200", width="1000", bg="gray").pack(fill="both", expand="True")
	else:
		Frame(raiz2, height="200", width="300", bg="gray").pack(fill="both", expand="True")
	x,y=5,10
	for i in range(len(draw_list)):
		Label(raiz2, text=draw_list[i], font="TimesNewRoman 14", bg="gray").place(x=x, y=y)
		x+=50
	raiz2.mainloop()
#----------------button------------------
def button():
	global draw_list
	draw_list=button2(numbers) #call module function
	numbers.set("")
	Raiz2()
#----------------Graffic1---------------
raiz=Tk()
raiz.title("Drow numbers")
raiz.iconbitmap("hola.ico")
raiz.resizable(0,0)
Frame(raiz, height="200", width="275", bg="gray").pack(fill="both", expand="True")
numbers=StringVar()
Entry(raiz, justify="center", textvariable=numbers).place(x="70", y="80")
Label(raiz, text="Type numbers to draw:", font="Impact 14", bg="gray").place(x="45", y="20")
BT=Button(raiz, text="Draw", command=button)
BT.place(x="200",y="150")
raiz.mainloop()



