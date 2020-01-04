from tkinter import *

window = Tk()

def kg_others():
    a=float(e1_value.get())
    grams=a*1000
    t1.insert(END,grams)
    pounds=a*2.20462
    t2.insert(END,pounds)
    ounce=a*35.274
    t3.insert(END,ounce)


b1=Button(window,text="Convert",command=kg_others)
b1.grid(row=0,column=2)


Label(window,text="Kg",height=1,width=10).grid(row=0,column=0)

e1_value=StringVar()
e1=Entry(window,text=e1_value)
e1.grid(row=0,column=1)

Label(window,text="grams",height=1,width=7).grid(row=1,column=1)
t1=Text(window,height=1,width=7)
t1.grid(row=1,column=0)

Label(window,text="pounds",height=1,width=7).grid(row=1,column=3)
t2=Text(window,height=1,width=7)
t2.grid(row=1,column=2)

Label(window,text="ounces",height=1,width=7).grid(row=1,column=5)
t3=Text(window,height=1,width=7)
t3.grid(row=1,column=4)



window.mainloop()
