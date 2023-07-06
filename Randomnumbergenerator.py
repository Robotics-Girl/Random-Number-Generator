from tkinter import * 
gen=Tk()
gen.configure(background="Dark Grey")
gen.title("NUMBER GENERATOR")
gen.geometry("500x575")

#Labels
tor1=Label(gen, text="NUMBER GENERATOR", font=("courier", "50"), bg='white', fg="black")
tor1.place(x=7,y=0)
#Buttons 
buttona1=Button(gen, width=30, text="Click Me!!", font=("Georgia","25"), height=10, bg="blue", fg="white")
buttona1.place(x=0,y=285)
bottona2=Button(gen, width=30, font=("Georgia","25"), bg="blue", fg="white", height=9)
bottona2.place(x=0,y=75)
gen.mainloop()