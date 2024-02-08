from tkinter import *
def FromEntryToLabel(event):
    t=ent.get()
    l.configure(text=t)
def valik():
    t=var.get()
    ent.delete(0,END)
    ent.insert(END,t)

showflag=False
def showtarnid(event):
    global showflag
    if showflag:
        ent.configure(show="")
        showflag=False
    else:
        t=ent.get()
        ent.configure(show="*")
        showflag=True

aken=Tk()
aken.geometry("600x500")
aken.title("Pealkiri")
aken.iconbitmap("auto.png")
f=Frame(aken,bg="blue",border=10,height=100,width=600)
l=Label(f,text="Elemendid",bg="gold",fg="#aa4a44",font="Arial 24",height=3,width=17)
ent=Entry(f,fg="gold",bg="#aa4a44",width=17,font="Arial 18",justify=CENTER)#show="*"
btn=Button(f,text="Vajuta siia",font="Arial 18",bg="lightblue",relief=GROOVE) #SUNKEN, RAISED
var=IntVar() #StringVar()
r1=Radiobutton(f,text="Esimene",font="Algerian 14",variable=var,value=1,command=valik)
r2=Radiobutton(f,text="Teine",font="Algerian 14",variable=var,value=2,command=valik)
r3=Radiobutton(f,text="Kolmas",font="Algerian 14",variable=var,value=3,command=valik)


btn.bind("<Button-1>",FromEntryToLabel)#LKM
ent.bind("<Return>",showtarnid) #Enter

f.grid(row=0,column=0) #pack(),place()

objects=[l,ent,btn,r1,r2,r3]
for i in range(len(objects)):
    objects[i].pack()

aken.mainloop()
